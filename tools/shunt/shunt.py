#!/usr/bin/env python3
"""
shunt — CLI за операции над отдалечени машини, които hook-ът не покрива.

pretool.py (hook) = прозрачно ИЗПЪЛНЕНИЕ на голи bash команди (@host режим).
shunt CLI (този файл) = специалните операции:

  shunt hosts                              конфигурираните хостове
  shunt read  @host <file> [start:end]     съдържание с номера на редове (за ориентация)
  shunt edit  @host <file> OLD NEW         редакция по СЪДЪРЖАНИЕ (edit_helper отсреща)
              [--expected N] [--dry-run]
  shunt edit  @host <file> --stdin         JSON {old,new,expected,base_sha} от stdin (многоредови)
  shunt cp    <src> <dst>                  rsync (едната страна @host:/път)
  shunt bg    @host <cmd>                  дълга задача (systemd-run); печата JOB=<unit>
  shunt bg    @host --list|--status JOB|--stop JOB
  shunt get   @host <url> [dest]           wget -b (фоново сваляне на самия сървър)

hosts (~/.config/shunt/hosts): `<alias> <transport> <target> [key=...]`
CLI операциите минават през ssh → искат ssh-достъпен хост.
"""
import sys, os, json, base64, shlex, subprocess, secrets

CONF = os.environ.get("SHUNT_CONF", os.path.expanduser("~/.config/shunt"))
SELF_DIR = os.path.dirname(os.path.realpath(__file__))
HELPER = os.path.join(SELF_DIR, "edit_helper.py")
SOCK = "/tmp/shunt-cm-cli-%r@%h:%p.sock"  # PER-DESTINATION (%r/%h/%p попълвани от ssh) —
# иначе споделен socket → ControlMaster праща командите за един хост към друг (тих, опасен бъг)


def die(msg, code=2):
    sys.stderr.write("shunt: " + msg + "\n")
    sys.exit(code)


def resolve_host(alias):
    alias = alias.lstrip("@")
    try:
        with open(os.path.join(CONF, "hosts")) as f:
            lines = f.read().splitlines()
    except Exception:
        die("няма hosts конфиг: %s/hosts" % CONF)
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) >= 3 and p[0] == alias:
            return {"alias": p[0], "transport": p[1], "target": p[2], "opts": p[3:]}
    die("непознат хост: %s" % alias)


def _key(host):
    for o in host["opts"]:
        if o.startswith("key="):
            return os.path.expanduser(o[4:])
    return None


def ssh_argv(host):
    if host["transport"] != "ssh":
        die("операцията иска ssh-достъпен хост; '%s' е %s" % (host["alias"], host["transport"]))
    a = ["ssh"]
    k = _key(host)
    if k:
        a += ["-i", k]
    a += ["-o", "StrictHostKeyChecking=accept-new", "-o", "ControlMaster=auto",
          "-o", "ControlPath=" + SOCK, "-o", "ControlPersist=300",
          "-o", "BatchMode=yes", host["target"]]
    return a


# ── подкоманди ───────────────────────────────────────────────────────────────
def cmd_hosts(argv):
    try:
        with open(os.path.join(CONF, "hosts")) as f:
            sys.stdout.write(f.read())
    except Exception:
        die("няма hosts конфиг: %s/hosts" % CONF)
    return 0


def cmd_read(argv):
    if len(argv) < 2:
        die("употреба: shunt read @host <file> [start:end]")
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
        die("употреба: shunt edit @host <file> OLD NEW [--expected N] [--dry-run] | --stdin")
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
            die("употреба: shunt edit @host <file> OLD NEW [--expected N] [--dry-run]")
        payload = {"file": f, "old": rest[0], "new": rest[1],
                   "expected": expected, "dry_run": dry}
    b64 = base64.b64encode(json.dumps(payload).encode()).decode()
    helper_src = open(HELPER, "rb").read()
    # inline deployment: helper source през stdin (python3 -), JSON като base64 argv
    r = subprocess.run(ssh_argv(host) + ["python3", "-", b64], input=helper_src)
    return r.returncode


def cmd_cp(argv):
    if len(argv) < 2:
        die("употреба: shunt cp <src> <dst> (едната страна @host:/път)")
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
        die("поне едната страна трябва да е @host:/път")
    e = "ssh -o ControlPath=%s -o StrictHostKeyChecking=accept-new" % SOCK
    k = _key(h)
    if k:
        e += " -i " + shlex.quote(k)
    return subprocess.run(["rsync", "-az", "--info=progress2", "-e", e, rsrc, rdst]).returncode


def cmd_bg(argv):
    if len(argv) < 2:
        die("употреба: shunt bg @host <cmd> | --list | --status JOB | --stop JOB")
    host = resolve_host(argv[0])
    sa = ssh_argv(host)
    rest = argv[1:]
    if rest[0] == "--list":
        return subprocess.run(sa + ["systemctl list-units 'shunt-*' --type=service --no-legend || true"]).returncode
    if rest[0] == "--status":
        if len(rest) < 2:
            die("употреба: shunt bg @host --status JOB")
        job = shlex.quote(rest[1])
        remote = ("journalctl -u %s --no-pager -n 60 2>/dev/null; echo '----'; "
                  "systemctl show %s -p ExecMainStatus -p ExecMainCode -p Result -p SubState"
                  % (job, job))
        return subprocess.run(sa + [remote]).returncode
    if rest[0] == "--stop":
        if len(rest) < 2:
            die("употреба: shunt bg @host --stop JOB")
        job = shlex.quote(rest[1])
        return subprocess.run(sa + ["systemctl stop %s; systemctl reset-failed %s 2>/dev/null; echo stopped" % (job, job)]).returncode
    # старт: system-level (root на нашите хостове) — преживява откачане, пази exit код
    cmd = " ".join(rest)
    unit = "shunt-" + base64.b16encode(os.urandom(4)).decode().lower()
    remote = ("systemd-run --collect --remain-after-exit --unit=%s bash -lc %s "
              ">/dev/null && echo 'JOB=%s'" % (unit, shlex.quote(cmd), unit))
    return subprocess.run(sa + [remote]).returncode


def cmd_get(argv):
    if len(argv) < 2:
        die("употреба: shunt get @host <url> [dest_dir]")
    host = resolve_host(argv[0])
    url = argv[1]
    dest = argv[2] if len(argv) > 2 else "."
    log = "/tmp/shunt-wget-%s.log" % base64.b16encode(os.urandom(3)).decode().lower()
    remote = ("cd %s && wget -b -o %s %s && echo 'сваля се фоново; прогрес: shunt read @%s %s или tail -f %s'"
              % (shlex.quote(dest), shlex.quote(log), shlex.quote(url),
                 host["alias"], shlex.quote(log), shlex.quote(log)))
    return subprocess.run(ssh_argv(host) + [remote]).returncode


def _write_hosts_line(alias, line):
    """hosts ред (идемпотентно — подменя ред със същия alias)."""
    os.makedirs(CONF, exist_ok=True)
    hp = os.path.join(CONF, "hosts")
    keep = []
    if os.path.exists(hp):
        keep = [l for l in open(hp).read().splitlines() if l.strip() and l.split()[0] != alias]
    keep.append(line)
    with open(hp, "w") as f:
        f.write("\n".join(keep) + "\n")
    print("✓ hosts ред: %s" % line)


def _print_hook_hint():
    """hook инструкция (НЕ пипаме чужд settings.json автоматично)."""
    print("\nЗа активиране добави в ~/.claude/settings.json → hooks.PreToolUse (ако още го няма):")
    print('  { "matcher": "Bash", "hooks": [ { "type": "command",')
    print('    "command": "python3 %s/pretool.py" } ] }' % SELF_DIR)
    print("  (изисква нов старт на Claude Code сесия)")


def cmd_install(argv):
    """shunt install <user>@<host> [--alias A] [--key PATH] [--mode secure|nonsecure]

    secure (default)  — ssh + ControlMaster: нула отворен порт, нула споделен токен.
    nonsecure         — демон (TCP + токен) на сървъра: бърз на ДОВЕРЕНА LAN.
    """
    if not argv or "@" not in argv[0]:
        die("употреба: shunt install <user>@<host> [--alias A] [--key PATH] [--mode secure|nonsecure]")
    dest = argv[0]
    rest = argv[1:]
    alias = rest[rest.index("--alias") + 1] if "--alias" in rest else None
    key = os.path.expanduser(rest[rest.index("--key") + 1]) if "--key" in rest else None
    mode = rest[rest.index("--mode") + 1] if "--mode" in rest else "secure"
    if mode not in ("secure", "nonsecure"):
        die("непознат --mode: %s (secure|nonsecure)" % mode)
    port = int(rest[rest.index("--port") + 1]) if "--port" in rest else 8766
    host_ip = dest.split("@", 1)[1]
    if not alias:
        alias = host_ip.replace(".", "-")
    sb = ["ssh", "-o", "StrictHostKeyChecking=accept-new"]
    if key:
        sb[1:1] = ["-i", key]
    sb.append(dest)
    # 1) python3 на сървъра (нужен за edit_helper / демон)
    r = subprocess.run(sb + ["python3 --version"], capture_output=True)
    if r.returncode != 0:
        die("python3 липсва на %s: %s" % (host_ip, (r.stderr or b"").decode()[:200]))
    print("✓ python3 на %s: %s" % (host_ip, (r.stdout or r.stderr).decode().strip()))

    if mode == "nonsecure":
        return _install_nonsecure(dest, host_ip, alias, key, sb, port)

    # ── secure (ssh) ──────────────────────────────────────────────────────────
    # 2) hosts ред (идемпотентно — подменя ред със същия alias)
    line = "%s ssh %s%s" % (alias, dest, (" key=" + key) if key else "")
    _write_hosts_line(alias, line)
    # 3) hook инструкция (НЕ пипаме чужд settings.json автоматично)
    _print_hook_hint()
    # 4) тест на връзката
    print("\nТест:")
    subprocess.run(sb + ["echo '  ✓ свързан с' $(hostname)"])
    return 0


def _install_nonsecure(dest, host_ip, alias, key, sb, port=8766):
    """nonsecure (демон) — генерира токен, качва daemon.py, вдига systemd, отваря порт.

    ⚠ Демонът слуша на 0.0.0.0:<port> → дава shell на ВСЕКИ с токена в мрежата.
    За продукция → ssh тунел/Tailscale + не-root User= в unit-а (DESIGN §6).
    """
    token = secrets.token_hex(16)
    # pre-flight: портът зает ли е вече на сървъра? (хваща тихия crash-loop при сблъсък — напр. стар rh)
    chk = subprocess.run(sb + ["ss -ltn 2>/dev/null | grep -q ':%d ' && echo BUSY || echo FREE" % port],
                         capture_output=True)
    if b"BUSY" in (chk.stdout or b""):
        die("порт %d вече е зает на %s (друг демон?). Спри го или ползвай --port ДРУГ." % (port, host_ip))
    daemon_src = os.path.join(SELF_DIR, "daemon.py")
    unit_src = os.path.join(SELF_DIR, "systemd", "shunt-daemon.service")
    if not os.path.exists(daemon_src):
        die("липсва daemon.py: %s" % daemon_src)
    if not os.path.exists(unit_src):
        die("липсва unit шаблон: %s" % unit_src)
    # scp ползва същия ключ като ssh; -O форсира scp протокола (стабилен за прости пътища)
    scp = ["scp", "-O", "-o", "StrictHostKeyChecking=accept-new"]
    if key:
        scp[1:1] = ["-i", key]

    # 1) /opt/shunt + daemon.py на сървъра
    r = subprocess.run(sb + ["mkdir -p /opt/shunt /etc/shunt"])
    if r.returncode != 0:
        die("не успях да създам /opt/shunt и /etc/shunt на %s" % host_ip)
    r = subprocess.run(scp + [daemon_src, dest + ":/opt/shunt/daemon.py"])
    if r.returncode != 0:
        die("scp на daemon.py се провали")
    print("✓ daemon.py → %s:/opt/shunt/daemon.py" % host_ip)

    # 2) /etc/shunt/daemon.env (chmod 600) — SHUNT_HOST=0.0.0.0 (LAN достъп)
    env_body = "SHUNT_TOKEN=%s\nSHUNT_PORT=%d\nSHUNT_HOST=0.0.0.0\n" % (token, port)
    remote_env = ("umask 177 && cat > /etc/shunt/daemon.env <<'SHUNT_EOF'\n"
                  + env_body + "SHUNT_EOF\nchmod 600 /etc/shunt/daemon.env")
    r = subprocess.run(sb + [remote_env])
    if r.returncode != 0:
        die("не успях да запиша /etc/shunt/daemon.env")
    print("✓ /etc/shunt/daemon.env (chmod 600, SHUNT_HOST=0.0.0.0, порт %d)" % port)

    # 3) systemd unit → daemon-reload → enable --now
    r = subprocess.run(scp + [unit_src, dest + ":/etc/systemd/system/shunt-daemon.service"])
    if r.returncode != 0:
        die("scp на unit файла се провали")
    r = subprocess.run(sb + ["systemctl daemon-reload && systemctl enable --now shunt-daemon"])
    if r.returncode != 0:
        die("systemctl enable --now shunt-daemon се провали")
    print("✓ systemd: shunt-daemon enabled + started")

    # 4) локално: hosts ред (daemon транспорт, target = host:port) + токен (chmod 600)
    _write_hosts_line(alias, "%s daemon %s:%d" % (alias, host_ip, port))
    os.makedirs(CONF, exist_ok=True)
    tp = os.path.join(CONF, "token")
    with open(tp, "w") as f:
        f.write(token + "\n")
    os.chmod(tp, 0o600)
    print("✓ токен → %s (chmod 600)" % tp)

    # 5) hook инструкция
    _print_hook_hint()

    # ⚠ предупреждение за модела на заплахата (DESIGN §6)
    print("\n⚠ ВНИМАНИЕ (nonsecure): демонът слуша на 0.0.0.0:%d → дава shell на" % port)
    print("  ВСЕКИ с токена в мрежата. Само за ДОВЕРЕНА LAN.")
    print("  За продукция → SSH тунел/Tailscale + не-root User= в unit-а; иначе ползвай --mode secure.")

    # 6) тест на връзката
    print("\nТест:")
    subprocess.run(sb + ["echo '  ✓ свързан с' $(hostname); systemctl is-active shunt-daemon"])
    return 0


def main():
    if len(sys.argv) < 2:
        die("употреба: shunt {hosts|read|edit|cp|bg|get|install} ...")
    sub, argv = sys.argv[1], sys.argv[2:]
    fns = {"hosts": cmd_hosts, "read": cmd_read, "edit": cmd_edit,
           "cp": cmd_cp, "bg": cmd_bg, "get": cmd_get, "install": cmd_install}
    fn = fns.get(sub)
    if not fn:
        die("непозната подкоманда: %s" % sub)
    sys.exit(fn(argv) or 0)


if __name__ == "__main__":
    main()
