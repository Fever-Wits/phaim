#!/usr/bin/env python3
"""
shunt — CLI for operations on remote machines that the hook does not cover.

pretool.py (hook) = transparent EXECUTION of bare bash commands (@host mode).
shunt CLI (this file) = the special operations:

  shunt hosts                              the configured hosts
  shunt read  @host <file> [start:end]     content with line numbers (for orientation)
  shunt edit  @host <file> OLD NEW         edit by CONTENT (edit_helper on the other side)
              [--expected N] [--dry-run]
  shunt edit  @host <file> --stdin         JSON {old,new,expected,base_sha} from stdin (multi-line)
  shunt cp    <src> <dst>                  rsync (one side @host:/path)
  shunt bg    @host <cmd>                  long task (systemd-run); prints JOB=<unit>
  shunt bg    @host --list|--status JOB|--stop JOB
  shunt get   @host <url> [dest]           wget -b (background download on the server itself)

hosts (~/.config/shunt/hosts): `<alias> <transport> <target> [key=...]`
CLI operations go through ssh → require an ssh-reachable host.
"""
import sys, os, json, base64, shlex, subprocess, secrets

CONF = os.environ.get("SHUNT_CONF", os.path.expanduser("~/.config/shunt"))
SELF_DIR = os.path.dirname(os.path.realpath(__file__))
HELPER = os.path.join(SELF_DIR, "edit_helper.py")
SOCK = "/tmp/shunt-cm-cli-%r@%h:%p.sock"  # PER-DESTINATION (%r/%h/%p filled in by ssh) —
# otherwise a shared socket → ControlMaster sends one host's commands to another (silent, dangerous bug)


def die(msg, code=2):
    sys.stderr.write("shunt: " + msg + "\n")
    sys.exit(code)


def resolve_host(alias):
    alias = alias.lstrip("@")
    try:
        with open(os.path.join(CONF, "hosts")) as f:
            lines = f.read().splitlines()
    except Exception:
        die("no hosts config: %s/hosts" % CONF)
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) >= 3 and p[0] == alias:
            return {"alias": p[0], "transport": p[1], "target": p[2], "opts": p[3:]}
    die("unknown host: %s" % alias)


def _key(host):
    for o in host["opts"]:
        if o.startswith("key="):
            return os.path.expanduser(o[4:])
    return None


def ssh_argv(host):
    if host["transport"] != "ssh":
        die("the operation requires an ssh-reachable host; '%s' is %s" % (host["alias"], host["transport"]))
    a = ["ssh"]
    k = _key(host)
    if k:
        a += ["-i", k]
    a += ["-o", "StrictHostKeyChecking=accept-new", "-o", "ControlMaster=auto",
          "-o", "ControlPath=" + SOCK, "-o", "ControlPersist=300",
          "-o", "BatchMode=yes", host["target"]]
    return a


# ── subcommands ──────────────────────────────────────────────────────────────
def cmd_hosts(argv):
    try:
        with open(os.path.join(CONF, "hosts")) as f:
            sys.stdout.write(f.read())
    except Exception:
        die("no hosts config: %s/hosts" % CONF)
    return 0


def cmd_read(argv):
    if len(argv) < 2:
        die("usage: shunt read @host <file> [start:end]")
    host = resolve_host(argv[0])
    f = argv[1]
    if len(argv) > 2 and ":" in argv[2]:
        a, b = argv[2].split(":", 1)
        remote = ("awk 'NR>=%d && NR<=%d{printf \"%%6d\\t%%s\\n\", NR, $0}' %s"
                  % (int(a), int(b), shlex.quote(f)))
    else:
        remote = "cat -n -- %s" % shlex.quote(f)
    return subprocess.run(ssh_argv(host) + [remote]).returncode


def cmd_edit(argv):
    if len(argv) < 2:
        die("usage: shunt edit @host <file> OLD NEW [--expected N] [--dry-run] | --stdin")
    host = resolve_host(argv[0])
    f = argv[1]
    rest = argv[2:]
    if "--stdin" in rest:
        payload = json.load(sys.stdin)
        payload["file"] = f
    else:
        dry = "--dry-run" in rest
        rest = [x for x in rest if x != "--dry-run"]
        expected = 1
        if "--expected" in rest:
            i = rest.index("--expected")
            expected = int(rest[i + 1])
            rest = rest[:i] + rest[i + 2:]
        if len(rest) < 2:
            die("usage: shunt edit @host <file> OLD NEW [--expected N] [--dry-run]")
        payload = {"file": f, "old": rest[0], "new": rest[1],
                   "expected": expected, "dry_run": dry}
    b64 = base64.b64encode(json.dumps(payload).encode()).decode()
    helper_src = open(HELPER, "rb").read()
    # inline deployment: helper source via stdin (python3 -), JSON as base64 argv
    r = subprocess.run(ssh_argv(host) + ["python3", "-", b64], input=helper_src)
    return r.returncode


def cmd_cp(argv):
    if len(argv) < 2:
        die("usage: shunt cp <src> <dst> (one side @host:/path)")
    host = {"ref": None}

    def conv(p):
        if p.startswith("@") and ":" in p:
            alias, _, path = p[1:].partition(":")
            h = resolve_host(alias)
            host["ref"] = h
            return h["target"] + ":" + path
        return p

    rsrc, rdst = conv(argv[0]), conv(argv[1])
    h = host["ref"]
    if not h:
        die("at least one side must be @host:/path")
    e = "ssh -o ControlPath=%s -o StrictHostKeyChecking=accept-new" % SOCK
    k = _key(h)
    if k:
        e += " -i " + shlex.quote(k)
    return subprocess.run(["rsync", "-az", "--info=progress2", "-e", e, rsrc, rdst]).returncode


def cmd_bg(argv):
    if len(argv) < 2:
        die("usage: shunt bg @host <cmd> | --list | --status JOB | --stop JOB")
    host = resolve_host(argv[0])
    sa = ssh_argv(host)
    rest = argv[1:]
    if rest[0] == "--list":
        return subprocess.run(sa + ["systemctl list-units 'shunt-*' --type=service --no-legend || true"]).returncode
    if rest[0] == "--status":
        if len(rest) < 2:
            die("usage: shunt bg @host --status JOB")
        job = shlex.quote(rest[1])
        remote = ("journalctl -u %s --no-pager -n 60 2>/dev/null; echo '----'; "
                  "systemctl show %s -p ExecMainStatus -p ExecMainCode -p Result -p SubState"
                  % (job, job))
        return subprocess.run(sa + [remote]).returncode
    if rest[0] == "--stop":
        if len(rest) < 2:
            die("usage: shunt bg @host --stop JOB")
        job = shlex.quote(rest[1])
        return subprocess.run(sa + ["systemctl stop %s; systemctl reset-failed %s 2>/dev/null; echo stopped" % (job, job)]).returncode
    # start: system-level (root on our hosts) — survives disconnect, preserves exit code
    cmd = " ".join(rest)
    unit = "shunt-" + base64.b16encode(os.urandom(4)).decode().lower()
    remote = ("systemd-run --collect --remain-after-exit --unit=%s bash -lc %s "
              ">/dev/null && echo 'JOB=%s'" % (unit, shlex.quote(cmd), unit))
    return subprocess.run(sa + [remote]).returncode


def cmd_get(argv):
    if len(argv) < 2:
        die("usage: shunt get @host <url> [dest_dir]")
    host = resolve_host(argv[0])
    url = argv[1]
    dest = argv[2] if len(argv) > 2 else "."
    log = "/tmp/shunt-wget-%s.log" % base64.b16encode(os.urandom(3)).decode().lower()
    remote = ("cd %s && wget -b -o %s %s && echo 'downloading in background; progress: shunt read @%s %s or tail -f %s'"
              % (shlex.quote(dest), shlex.quote(log), shlex.quote(url),
                 host["alias"], shlex.quote(log), shlex.quote(log)))
    return subprocess.run(ssh_argv(host) + [remote]).returncode


def _write_hosts_line(alias, line):
    """hosts line (idempotent — replaces a line with the same alias)."""
    os.makedirs(CONF, exist_ok=True)
    hp = os.path.join(CONF, "hosts")
    keep = []
    if os.path.exists(hp):
        keep = [l for l in open(hp).read().splitlines() if l.strip() and l.split()[0] != alias]
    keep.append(line)
    with open(hp, "w") as f:
        f.write("\n".join(keep) + "\n")
    print("✓ hosts line: %s" % line)


def _print_hook_hint():
    """hook instruction (we do NOT touch someone else's settings.json automatically)."""
    print("\nTo activate, add to ~/.claude/settings.json → hooks.PreToolUse (if not already there):")
    print('  { "matcher": "Bash", "hooks": [ { "type": "command",')
    print('    "command": "python3 %s/pretool.py" } ] }' % SELF_DIR)
    print("  (requires restarting the Claude Code session)")


def cmd_install(argv):
    """shunt install <user>@<host> [--alias A] [--key PATH] [--mode secure|nonsecure]

    secure (default)  — ssh + ControlMaster: zero open ports, zero shared token.
    nonsecure         — daemon (TCP + token) on the server: fast on a TRUSTED LAN.
    """
    if not argv or "@" not in argv[0]:
        die("usage: shunt install <user>@<host> [--alias A] [--key PATH] [--mode secure|nonsecure]")
    dest = argv[0]
    rest = argv[1:]
    alias = rest[rest.index("--alias") + 1] if "--alias" in rest else None
    key = os.path.expanduser(rest[rest.index("--key") + 1]) if "--key" in rest else None
    mode = rest[rest.index("--mode") + 1] if "--mode" in rest else "secure"
    if mode not in ("secure", "nonsecure"):
        die("unknown --mode: %s (secure|nonsecure)" % mode)
    port = int(rest[rest.index("--port") + 1]) if "--port" in rest else 8766
    host_ip = dest.split("@", 1)[1]
    if not alias:
        alias = host_ip.replace(".", "-")
    sb = ["ssh", "-o", "StrictHostKeyChecking=accept-new"]
    if key:
        sb[1:1] = ["-i", key]
    sb.append(dest)
    # 1) python3 on the server (needed for edit_helper / daemon)
    r = subprocess.run(sb + ["python3 --version"], capture_output=True)
    if r.returncode != 0:
        die("python3 missing on %s: %s" % (host_ip, (r.stderr or b"").decode()[:200]))
    print("✓ python3 on %s: %s" % (host_ip, (r.stdout or r.stderr).decode().strip()))

    if mode == "nonsecure":
        return _install_nonsecure(dest, host_ip, alias, key, sb, port)

    # ── secure (ssh) ──────────────────────────────────────────────────────────
    # 2) hosts line (idempotent — replaces a line with the same alias)
    line = "%s ssh %s%s" % (alias, dest, (" key=" + key) if key else "")
    _write_hosts_line(alias, line)
    # 3) hook instruction (we do NOT touch someone else's settings.json automatically)
    _print_hook_hint()
    # 4) connection test
    print("\nTest:")
    subprocess.run(sb + ["echo '  ✓ connected to' $(hostname)"])
    return 0


def _install_nonsecure(dest, host_ip, alias, key, sb, port=8766):
    """nonsecure (daemon) — generates a token, uploads daemon.py, brings up systemd, opens a port.

    ⚠ The daemon listens on 0.0.0.0:<port> → gives a shell to ANYONE with the token on the network.
    For production → ssh tunnel/Tailscale + non-root User= in the unit (DESIGN §6).
    """
    token = secrets.token_hex(16)
    # pre-flight: is the port already taken on the server? (catches the silent crash-loop on a clash — e.g. an old rh)
    chk = subprocess.run(sb + ["ss -ltn 2>/dev/null | grep -q ':%d ' && echo BUSY || echo FREE" % port],
                         capture_output=True)
    if b"BUSY" in (chk.stdout or b""):
        die("port %d is already taken on %s (another daemon?). Stop it or use a DIFFERENT --port." % (port, host_ip))
    daemon_src = os.path.join(SELF_DIR, "daemon.py")
    unit_src = os.path.join(SELF_DIR, "systemd", "shunt-daemon.service")
    if not os.path.exists(daemon_src):
        die("missing daemon.py: %s" % daemon_src)
    if not os.path.exists(unit_src):
        die("missing unit template: %s" % unit_src)
    # scp uses the same key as ssh; -O forces the scp protocol (stable for simple paths)
    scp = ["scp", "-O", "-o", "StrictHostKeyChecking=accept-new"]
    if key:
        scp[1:1] = ["-i", key]

    # 1) /opt/shunt + daemon.py on the server
    r = subprocess.run(sb + ["mkdir -p /opt/shunt /etc/shunt"])
    if r.returncode != 0:
        die("failed to create /opt/shunt and /etc/shunt on %s" % host_ip)
    r = subprocess.run(scp + [daemon_src, dest + ":/opt/shunt/daemon.py"])
    if r.returncode != 0:
        die("scp of daemon.py failed")
    print("✓ daemon.py → %s:/opt/shunt/daemon.py" % host_ip)

    # 2) /etc/shunt/daemon.env (chmod 600) — SHUNT_HOST=0.0.0.0 (LAN access)
    env_body = "SHUNT_TOKEN=%s\nSHUNT_PORT=%d\nSHUNT_HOST=0.0.0.0\n" % (token, port)
    remote_env = ("umask 177 && cat > /etc/shunt/daemon.env <<'SHUNT_EOF'\n"
                  + env_body + "SHUNT_EOF\nchmod 600 /etc/shunt/daemon.env")
    r = subprocess.run(sb + [remote_env])
    if r.returncode != 0:
        die("failed to write /etc/shunt/daemon.env")
    print("✓ /etc/shunt/daemon.env (chmod 600, SHUNT_HOST=0.0.0.0, port %d)" % port)

    # 3) systemd unit → daemon-reload → enable --now
    r = subprocess.run(scp + [unit_src, dest + ":/etc/systemd/system/shunt-daemon.service"])
    if r.returncode != 0:
        die("scp of the unit file failed")
    r = subprocess.run(sb + ["systemctl daemon-reload && systemctl enable --now shunt-daemon"])
    if r.returncode != 0:
        die("systemctl enable --now shunt-daemon failed")
    print("✓ systemd: shunt-daemon enabled + started")

    # 4) local: hosts line (daemon transport, target = host:port) + token (chmod 600)
    _write_hosts_line(alias, "%s daemon %s:%d" % (alias, host_ip, port))
    os.makedirs(CONF, exist_ok=True)
    tp = os.path.join(CONF, "token")
    with open(tp, "w") as f:
        f.write(token + "\n")
    os.chmod(tp, 0o600)
    print("✓ token → %s (chmod 600)" % tp)

    # 5) hook instruction
    _print_hook_hint()

    # ⚠ threat-model warning (DESIGN §6)
    print("\n⚠ WARNING (nonsecure): the daemon listens on 0.0.0.0:%d → gives a shell to" % port)
    print("  ANYONE with the token on the network. Only for a TRUSTED LAN.")
    print("  For production → SSH tunnel/Tailscale + non-root User= in the unit; otherwise use --mode secure.")

    # 6) connection test
    print("\nTest:")
    subprocess.run(sb + ["echo '  ✓ connected to' $(hostname); systemctl is-active shunt-daemon"])
    return 0


def main():
    if len(sys.argv) < 2:
        die("usage: shunt {hosts|read|edit|cp|bg|get|install} ...")
    sub, argv = sys.argv[1], sys.argv[2:]
    fns = {"hosts": cmd_hosts, "read": cmd_read, "edit": cmd_edit,
           "cp": cmd_cp, "bg": cmd_bg, "get": cmd_get, "install": cmd_install}
    fn = fns.get(sub)
    if not fn:
        die("unknown subcommand: %s" % sub)
    sys.exit(fn(argv) or 0)


if __name__ == "__main__":
    main()
