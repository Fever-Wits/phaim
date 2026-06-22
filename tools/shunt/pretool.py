#!/usr/bin/env python3
"""
shunt — pretool.py · PreToolUse hook (matcher: Bash)

Transparently redirects the agent's bash commands to a chosen remote machine.
Switching: @<alias> / @local / @status — PER-SESSION (does not clash across parallel sessions).

Two transports (configured per-host in ~/.config/shunt/hosts):
  ssh     — SECURE: ssh + ControlMaster (zero open ports, zero shared token,
            encrypted). Proven: cwd state-file per session, live streaming, speed.
  daemon  — NONSECURE: TCP + token (fast on a trusted LAN). The token is passed via the ENV
            of the inline client (not argv → not visible in `ps` to other local users).
            NB: the command (with the ENV assignment) ends up in the transcript → daemon mode is
            only for a trusted LAN; for an untrusted network use ssh mode (no token there).

Why hook + updatedInput (rather than replacing the shell): official, documented mechanism;
we stay independent of undocumented env settings.

CRITICAL: the rewritten command runs in a strict sandbox (root, no ~/.config/shunt, BUT network
OK). That's why the daemon client is SELF-CONTAINED inline (zero files); the ssh client uses the
`ssh` binary, which is available in the sandbox.
"""
import json, sys, os, shlex, binascii

CONF = os.environ.get("SHUNT_CONF", os.path.expanduser("~/.config/shunt"))

# --- self-contained inline daemon client (token comes via ENV SHUNT_TOK, not via argv) ---
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
    """Return a rewritten command to Claude Code and exit."""
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {"command": command}}}))
    sys.exit(0)


def echo(msg):
    emit("echo " + shlex.quote(msg))


def resolve_host(alias):
    """hosts line: `<alias> <transport> <target> [key=...]` → dict or None."""
    for line in conf_read("hosts").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) >= 3 and p[0] == alias:
            return {"alias": p[0], "transport": p[1], "target": p[2], "opts": p[3:]}
    return None


def ssh_command(host, cmd, sid):
    """SECURE: ssh + ControlMaster; cwd is kept per session via a remote state-file."""
    key = None
    for o in host["opts"]:
        if o.startswith("key="):
            key = os.path.expanduser(o[4:])
    sock = "/tmp/shunt-cm-%s-%%h-%%p.sock" % sid  # per-session AND PER-DESTINATION (%h/%p from ssh) —
    # otherwise @84 then @82 in the same session → shared socket → commands go to the wrong host
    state = "/tmp/shunt-cwd-%s" % sid
    # trap EXIT captures the code + updates cwd on EVERY exit (incl. `exit N` in the command)
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
    """NONSECURE: self-contained inline TCP client; random per-connection marker."""
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

    # guard against double rewriting (an already-rewritten command carries the transport marker)
    if "__SHUNT_END_" in cmd or "ControlPath=/tmp/shunt-cm-" in cmd:
        sys.exit(0)

    s = cmd.strip()

    # shunt CLI commands run LOCALLY (they do the transport themselves) → do not redirect
    if s == "shunt" or s.startswith("shunt "):
        sys.exit(0)

    def read_target():
        try:
            with open(target_file) as f:
                return f.read().strip()
        except Exception:
            return ""

    # --- switches ---
    if s == "@local":
        try:
            os.remove(target_file)
        except OSError:
            pass
        echo("[shunt] mode: LOCAL")

    if s == "@status":
        t = read_target()
        echo("[shunt] " + (("REMOTE → " + t) if t else "LOCAL"))

    if s.startswith("@") and len(s) > 1 and " " not in s:
        alias = s[1:]
        host = resolve_host(alias)
        if not host:
            echo("[shunt] unknown host: " + alias)
        os.makedirs(CONF, exist_ok=True)
        try:
            with open(target_file, "w") as f:
                f.write(alias)
        except Exception:
            sys.exit(0)
        echo("[shunt] mode: REMOTE → %s (%s, %s)"
             % (alias, host["target"], host["transport"]))

    # --- remote execution depending on transport ---
    alias = read_target()
    if alias:
        host = resolve_host(alias)
        if not host:               # host disappeared from the config → fall back to local
            sys.exit(0)
        if host["transport"] == "ssh":
            emit(ssh_command(host, cmd, sid))
        elif host["transport"] == "daemon":
            emit(daemon_command(host, cmd, sid))

    sys.exit(0)


if __name__ == "__main__":
    main()
