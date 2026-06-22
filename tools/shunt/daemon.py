#!/usr/bin/env python3
"""
shunt — daemon.py · NONSECURE транспорт (TCP + токен), за ДОВЕРЕНА LAN.
За недоверена мрежа ползвай ssh режим (там няма демон, няма токен, няма отворен порт).

Протокол (TCP, stdlib): клиент → {"token","cmd","cwd","sid","mark"}\\n ;
демон → суров stdout/stderr поток + финал <mark><exit>__PWD__<cwd>\\n.
cwd се пази PER-SESSION (по sid). Маркерът идва ОТ КЛИЕНТА (случаен на връзка) →
команда, която печата фиксиран низ, не чупи протокола.

Сигурност:
- bind 127.0.0.1 по подразбиране; изричен opt-in за LAN чрез SHUNT_HOST.
- constant-time сравнение на токена (hmac.compare_digest).
- стартирай като НЕ-root потребител (systemd unit-ът го прави); root → предупреждение.

Конфиг (ENV): SHUNT_TOKEN (задължителен) · SHUNT_PORT (8766) · SHUNT_HOST (127.0.0.1).
"""
import os, sys, json, signal, socketserver, subprocess, threading, time, hmac, shlex

TOKEN = os.environ.get("SHUNT_TOKEN", "")
PORT  = int(os.environ.get("SHUNT_PORT", "8766"))
HOST  = os.environ.get("SHUNT_HOST", "127.0.0.1")
HOME  = os.path.expanduser("~")
_CWD  = {}            # per-session: sid -> последен cwd
_LOCK = threading.Lock()


class Handler(socketserver.BaseRequestHandler):
    def _send(self, data):
        try:
            self.request.sendall(data); return True
        except (BrokenPipeError, ConnectionResetError, OSError):
            return False

    def handle(self):
        rfile = self.request.makefile("rb")
        try:
            raw = rfile.readline()
            if not raw:
                return
            req = json.loads(raw.decode("utf-8", "replace"))
        except Exception:
            self._send(b"shunt: bad request\n")
            return

        mark = req.get("mark") or "__SHUNT_END__"

        def end(code, cwd):
            return (mark + str(code) + "__PWD__" + cwd + "\n").encode()

        tok = req.get("token", "")
        if not TOKEN or not hmac.compare_digest(str(tok), TOKEN):
            self._send(b"shunt: invalid token\n" + end(126, HOME))
            return

        cmd = req.get("cmd", "")
        sid = req.get("sid") or "default"
        with _LOCK:
            cwd = req.get("cwd") or _CWD.get(sid) or HOME
        if not os.path.isdir(cwd):
            cwd = HOME

        # trap EXIT хваща кода + печата маркера при ВСЯКО излизане (вкл. `exit N` в командата)
        trap_action = ('rc=$?; printf "%s%s__PWD__%s\\n" ' + shlex.quote(mark)
                       + ' "$rc" "$(pwd)"')
        wrapped = (
            "cd " + shlex.quote(cwd) + " 2>/dev/null || cd ~\n"
            + "trap " + shlex.quote(trap_action) + " EXIT\n"
            + cmd
        )

        proc = subprocess.Popen(
            ["bash", "-c", wrapped],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL, start_new_session=True,
        )

        alive = threading.Event(); alive.set()

        def watch():                 # клиент изключи → убий процес-групата (за `-f`)
            try:
                while alive.is_set():
                    if not self.request.recv(1):
                        break
            except Exception:
                pass
            _kill(proc)
        threading.Thread(target=watch, daemon=True).start()

        try:
            fd = proc.stdout.fileno()
            tail = b""
            while True:
                chunk = os.read(fd, 4096)
                if not chunk:
                    break
                tail = (tail + chunk)[-512:]
                if not self._send(chunk):
                    _kill(proc); break
            mi = tail.rfind(b"__PWD__")
            if mi >= 0:
                nc = tail[mi + len(b"__PWD__"):].decode("utf-8", "replace").strip()
                if nc and os.path.isdir(nc):
                    with _LOCK:
                        _CWD[sid] = nc       # запомни cwd за ТАЗИ сесия
        finally:
            alive.clear()
            try: proc.stdout.close()
            except Exception: pass
            proc.wait()


def _kill(proc):
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        time.sleep(0.3)
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except Exception:
        pass


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    if not TOKEN:
        sys.stderr.write("shunt daemon: ОТКАЗ — SHUNT_TOKEN не е зададен.\n")
        sys.exit(2)
    if os.geteuid() == 0:
        sys.stderr.write("shunt daemon: ПРЕДУПРЕЖДЕНИЕ — вървиш като root; препоръчва се не-root потребител.\n")
    sys.stderr.write("shunt daemon: слушам %s:%d\n" % (HOST, PORT))
    Server((HOST, PORT), Handler).serve_forever()
