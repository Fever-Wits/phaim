#!/usr/bin/env python3
"""
shunt — daemon.py · NONSECURE transport (TCP + token), for a TRUSTED LAN.
For an untrusted network use ssh mode (no daemon, no token, no open port there).

Protocol (TCP, stdlib): client → {"token","cmd","cwd","sid","mark"}\\n ;
daemon → raw stdout/stderr stream + trailer <mark><exit>__PWD__<cwd>\\n.
cwd is kept PER-SESSION (by sid). The marker comes FROM THE CLIENT (random per connection) →
a command that prints a fixed string does not break the protocol.

Security:
- bind 127.0.0.1 by default; explicit opt-in for LAN via SHUNT_HOST.
- constant-time token comparison (hmac.compare_digest).
- run as a NON-root user (the systemd unit does this); root → warning.

Config (ENV): SHUNT_TOKEN (required) · SHUNT_PORT (8766) · SHUNT_HOST (127.0.0.1).
"""
import os, sys, json, signal, socketserver, subprocess, threading, time, hmac, shlex

TOKEN = os.environ.get("SHUNT_TOKEN", "")
PORT  = int(os.environ.get("SHUNT_PORT", "8766"))
HOST  = os.environ.get("SHUNT_HOST", "127.0.0.1")
HOME  = os.path.expanduser("~")
_CWD  = {}            # per-session: sid -> last cwd
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

        # trap EXIT captures the code + prints the marker on EVERY exit (incl. `exit N` in the command)
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

        def watch():                 # client disconnected → kill the process group (for `-f`)
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
                        _CWD[sid] = nc       # remember cwd for THIS session
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
        sys.stderr.write("shunt daemon: REFUSED — SHUNT_TOKEN is not set.\n")
        sys.exit(2)
    if os.geteuid() == 0:
        sys.stderr.write("shunt daemon: WARNING — running as root; a non-root user is recommended.\n")
    sys.stderr.write("shunt daemon: listening on %s:%d\n" % (HOST, PORT))
    Server((HOST, PORT), Handler).serve_forever()
