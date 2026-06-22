#!/usr/bin/env python3
"""
shunt — edit_helper.py · server-side редактор по СЪДЪРЖАНИЕ (не по номер на ред).

Изпълнява се на отдалечената машина (или локално). Вход = JSON по stdin, изход = JSON по stdout.
Нула външни зависимости (само stdlib). Payload през stdin → НУЛА shell escaping (бинарно-безопасно).

Семантика като вградения Edit: `old → new`, изисква УНИКАЛНОСТ (expected съвпадения; иначе отказ).
Триангулиран дизайн (web research 2026-06-22) + заемки: memdex (checksum/atomic),
desktop-commander (count-and-refuse + fuzzy-diag), Aider/Claude str_replace (адрес по съдържание).

Вход (JSON):
  {"file": str, "old": str, "new": str, "expected": 1, "base_sha": null|str, "dry_run": false}
Изход (JSON, status):
  ok        → {status, count, new_sha, verified, diff, normalized}
  not_found → {status, hint}                          (0 съвпадения)
  ambiguous → {status, count, expected, hint}         (count-and-refuse)
  conflict  → {status, current_sha, base_sha}         (optimistic SHA-256 lock)
  error     → {status, message}
"""
import sys, json, os, hashlib, difflib, tempfile


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def out(d):
    print(json.dumps(d, ensure_ascii=False))


def main():
    try:
        if len(sys.argv) > 1:                       # inline deployment: JSON като base64 argv
            import base64
            req = json.loads(base64.b64decode(sys.argv[1]))
        else:                                        # локален/интерактивен: JSON от stdin
            req = json.load(sys.stdin)
    except Exception as e:
        return out({"status": "error", "message": "bad request: %s" % e})

    path = os.path.realpath(req.get("file", ""))   # resolve symlink → редактирай таргета, не link-а
    old = req.get("old", "")
    new = req.get("new", "")
    expected = int(req.get("expected", 1))
    base_sha = req.get("base_sha")
    dry = bool(req.get("dry_run", False))

    if not old:
        return out({"status": "error", "message": "old е празен"})
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except Exception as e:
        return out({"status": "error", "message": "read failed: %s" % e})

    cur_sha = sha256(raw)
    # optimistic lock: пипнат ли е файлът между четенето ми и този запис?
    if base_sha and base_sha != cur_sha:
        return out({"status": "conflict", "current_sha": cur_sha, "base_sha": base_sha,
                    "hint": "файлът се е променил; прочети наново и опитай пак"})

    text = raw.decode("utf-8", "replace")

    # match: exact първо; ако 0 → опитай нормализирани line endings (CRLF→LF) — тук умират повечето
    count = text.count(old)
    normalized = False
    work, o, n = text, old, new
    if count == 0:
        work = text.replace("\r\n", "\n")
        o = old.replace("\r\n", "\n")
        n = new.replace("\r\n", "\n")
        count = work.count(o)
        normalized = count > 0

    if count == 0:
        return out({"status": "not_found",
                    "hint": "old не е намерен (дори с нормализирани CRLF); добави уникален контекст"})
    if count != expected:
        return out({"status": "ambiguous", "count": count, "expected": expected,
                    "hint": "добави обграждащ контекст за уникалност"})

    new_text = work.replace(o, n)
    diff = "".join(difflib.unified_diff(
        work.splitlines(keepends=True), new_text.splitlines(keepends=True),
        fromfile=path, tofile=path + " (edited)"))   # diff на LF база — чист за четене
    if normalized and "\r\n" in text:
        new_text = new_text.replace("\n", "\r\n")     # запази оригиналния CRLF стил при запис
    new_bytes = new_text.encode("utf-8")

    if dry:
        return out({"status": "ok", "dry_run": True, "count": count,
                    "new_sha": sha256(new_bytes), "diff": diff, "normalized": normalized})

    # atomic запис: temp в СЪЩАТА папка + fsync(data) + rename + fsync(dir)
    d = os.path.dirname(path) or "."
    tmp = None
    try:
        st = os.stat(path)
        fd, tmp = tempfile.mkstemp(dir=d, prefix=".shunt-edit-")
        try:
            os.write(fd, new_bytes)
            os.fsync(fd)
        finally:
            os.close(fd)
        os.chmod(tmp, st.st_mode)
        try:
            os.chown(tmp, st.st_uid, st.st_gid)
        except Exception:
            pass
        os.replace(tmp, path)                       # atomic на същата ФС
        tmp = None
        dfd = os.open(d, os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    except Exception as e:
        if tmp:
            try: os.unlink(tmp)
            except Exception: pass
        return out({"status": "error", "message": "write failed: %s" % e})

    # verify-after-write (нашата ниша — никой SSH MCP не го прави)
    with open(path, "rb") as f:
        vsha = sha256(f.read())
    ok = (vsha == sha256(new_bytes))
    res = {"status": "ok" if ok else "error", "count": count, "new_sha": vsha,
           "verified": ok, "diff": diff, "normalized": normalized}
    if not ok:
        res["message"] = "verify mismatch след запис"
    out(res)


if __name__ == "__main__":
    main()
