#!/usr/bin/env python3
"""
shunt — pretool.py · PreToolUse hook (matcher: Bash)

Прозрачно отклонява bash командите на агента към избрана отдалечена машина.
Превключване: @<alias> / @local / @status — PER-SESSION (не застъпва паралелни сесии).

Два транспорта (зададени per-host в ~/.config/shunt/hosts):
  ssh     — SECURE: ssh + ControlMaster (нула отворен порт, нула споделен токен,
            криптирано). Доказано: cwd state-file per session, live streaming, скорост.
  daemon  — NONSECURE: TCP + токен (бърз на доверена LAN). Токенът минава през ENV
            на inline клиента (не argv → не се вижда в `ps` за други локални потребители).
            NB: командата (с ENV-присвояване) влиза в transcript-а → daemon режим е само
            за доверена LAN; за нечувствителна мрежа ползвай ssh режим (там няма токен).

Защо hook + updatedInput (а не подмяна на shell-а): официален, документиран механизъм;
независим сме от недокументирани env-настройки.

КРИТИЧНО: пренаписаната команда тече в строг sandbox (root, без ~/.config/shunt, НО мрежа
OK). Затова daemon клиентът е SELF-CONTAINED inline (нула файлове); ssh клиентът ползва
`ssh` binary, който е наличен в sandbox-а.
"""
import json, sys, os, shlex, binascii

CONF = os.environ.get("SHUNT_CONF", os.path.expanduser("~/.config/shunt"))

# --- self-contained inline daemon клиент (token идва през ENV SHUNT_TOK, не през argv) ---
# argv: cmd host port sid mark
INLINE_DAEMON = r'''
import socket,json,sys,os
cmd,host,port,sid,mark=sys.argv[1:6]
tok=os.environ.get("SHUNT_TOK","")
try: s=socket.create_connection((host,int(port)),timeout=15)
except Exception as e: sys.stderr.write("shunt: connect %s\n"%e); sys.exit(255)
s.sendall((json.dumps({"token":tok,"cmd":cmd,"cwd":"","sid":sid,"mark":mark})+"\n").encode())
M=mark.encode(); buf=b""; ec=0; o=sys.stdout.buffer
while True:
 d=s.recv(4096)
 if not d:
  if buf: o.write(buf)
  break
 buf+=d; i=buf.find(M)
 if i>=0:
  o.write(buf[:i]); o.flush()
  t=buf[i+len(M):].decode("utf-8","replace"); e,_,_=t.partition("__PWD__")
  try: ec=int(e)
  except Exception: ec=0
  break
 elif len(buf)>len(M):
  o.write(buf[:-len(M)]); o.flush(); buf=buf[-len(M):]
o.flush(); sys.exit(ec)
'''


def conf_read(name):
    try:
        with open(os.path.join(CONF, name)) as f:
            return f.read()
    except Exception:
        return ""


def emit(command):
    """Върни пренаписана команда към Claude Code и излез."""
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {"command": command}}}))
    sys.exit(0)


def echo(msg):
    emit("echo " + shlex.quote(msg))


def resolve_host(alias):
    """hosts ред: `<alias> <transport> <target> [key=...]` → dict или None."""
    for line in conf_read("hosts").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) >= 3 and p[0] == alias:
            return {"alias": p[0], "transport": p[1], "target": p[2], "opts": p[3:]}
    return None


def ssh_command(host, cmd, sid):
    """SECURE: ssh + ControlMaster; cwd се пази per session чрез remote state-file."""
    key = None
    for o in host["opts"]:
        if o.startswith("key="):
            key = os.path.expanduser(o[4:])
    sock = "/tmp/shunt-cm-%s-%%h-%%p.sock" % sid  # per-session И PER-DESTINATION (%h/%p от ssh) —
    # иначе @84 после @82 в същата сесия → споделен socket → командите отиват на грешен хост
    state = "/tmp/shunt-cwd-%s" % sid
    # trap EXIT хваща кода + обновява cwd при ВСЯКО излизане (вкл. `exit N` в командата)
    trap_action = "rc=$?; pwd > %s 2>/dev/null; exit $rc" % shlex.quote(state)
    remote = (
        'cd "$(cat %s 2>/dev/null || echo "$HOME")" 2>/dev/null || cd ~\n' % shlex.quote(state)
        + "trap " + shlex.quote(trap_action) + " EXIT\n"
        + cmd
    )
    opts = ["-o", "StrictHostKeyChecking=accept-new",
            "-o", "ControlMaster=auto", "-o", "ControlPath=" + sock,
            "-o", "ControlPersist=300", "-o", "BatchMode=yes"]
    if key:
        opts = ["-i", key] + opts
    return ("ssh " + " ".join(shlex.quote(o) for o in opts)
            + " " + shlex.quote(host["target"])
            + " " + shlex.quote(remote))


def daemon_command(host, cmd, sid):
    """NONSECURE: self-contained inline TCP клиент; случаен маркер на връзка."""
    h, _, port = host["target"].partition(":")
    port = port or "8766"
    tok = conf_read("token").strip()
    mark = "__SHUNT_END_%s__" % binascii.hexlify(os.urandom(5)).decode()
    return ("SHUNT_TOK=" + shlex.quote(tok)
            + " python3 -c " + shlex.quote(INLINE_DAEMON)
            + " " + shlex.quote(cmd) + " " + shlex.quote(h) + " " + shlex.quote(port)
            + " " + shlex.quote(sid) + " " + shlex.quote(mark))


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    if data.get("tool_name") != "Bash":
        sys.exit(0)

    sid = data.get("session_id") or "default"
    target_file = os.path.join(CONF, "target." + sid)
    cmd = (data.get("tool_input") or {}).get("command", "")

    # guard срещу двойно пренаписване (вече-пренаписаната носи маркер на транспорта)
    if "__SHUNT_END_" in cmd or "ControlPath=/tmp/shunt-cm-" in cmd:
        sys.exit(0)

    s = cmd.strip()

    # shunt CLI командите се изпълняват ЛОКАЛНО (сами правят транспорта) → не пренасочвай
    if s == "shunt" or s.startswith("shunt "):
        sys.exit(0)

    def read_target():
        try:
            with open(target_file) as f:
                return f.read().strip()
        except Exception:
            return ""

    # --- превключватели ---
    if s == "@local":
        try:
            os.remove(target_file)
        except OSError:
            pass
        echo("[shunt] режим: ЛОКАЛЕН")

    if s == "@status":
        t = read_target()
        echo("[shunt] " + (("ОТДАЛЕЧЕН → " + t) if t else "ЛОКАЛЕН"))

    if s.startswith("@") and len(s) > 1 and " " not in s:
        alias = s[1:]
        host = resolve_host(alias)
        if not host:
            echo("[shunt] непознат хост: " + alias)
        os.makedirs(CONF, exist_ok=True)
        try:
            with open(target_file, "w") as f:
                f.write(alias)
        except Exception:
            sys.exit(0)
        echo("[shunt] режим: ОТДАЛЕЧЕН → %s (%s, %s)"
             % (alias, host["target"], host["transport"]))

    # --- отдалечено изпълнение според транспорта ---
    alias = read_target()
    if alias:
        host = resolve_host(alias)
        if not host:               # хостът изчезна от конфига → fallback локално
            sys.exit(0)
        if host["transport"] == "ssh":
            emit(ssh_command(host, cmd, sid))
        elif host["transport"] == "daemon":
            emit(daemon_command(host, cmd, sid))

    sys.exit(0)


if __name__ == "__main__":
    main()
