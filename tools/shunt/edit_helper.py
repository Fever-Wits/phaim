#!/usr/bin/env python3
"""
shunt — edit_helper.py · server-side editor by CONTENT (not by line number).

Runs on the remote machine (or locally). Input = JSON on stdin, output = JSON on stdout.
Zero external dependencies (stdlib only). Payload via stdin → ZERO shell escaping (binary-safe).

Semantics like the built-in Edit: `old → new`, requires UNIQUENESS (expected matches; otherwise refuse).
Triangulated design (web research 2026-06-22) + borrowings: memdex (checksum/atomic),
desktop-commander (count-and-refuse + fuzzy-diag), Aider/Claude str_replace (address by content).

Input (JSON):
  {"file": str, "old": str, "new": str, "expected": 1, "base_sha": null|str, "dry_run": false}
Output (JSON, status):
  ok        → {status, count, new_sha, verified, diff, normalized}
  not_found → {status, hint}                          (0 matches)
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
        if len(sys.argv) > 1:                       # inline deployment: JSON as base64 argv
            import base64
            req = json.loads(base64.b64decode(sys.argv[1]))
        else:                                        # local/interactive: JSON from stdin
            req = json.load(sys.stdin)
    except Exception as e:
        return out({"status": "error", "message": "bad request: %s" % e})

    path = os.path.realpath(req.get("file", ""))   # resolve symlink → edit the target, not the link
    old = req.get("old", "")
    new = req.get("new", "")
    expected = int(req.get("expected", 1))
    base_sha = req.get("base_sha")
    dry = bool(req.get("dry_run", False))

    if not old:
        return out({"status": "error", "message": "old is empty"})
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except Exception as e:
        return out({"status": "error", "message": "read failed: %s" % e})

    cur_sha = sha256(raw)
    # optimistic lock: was the file touched between my read and this write?
    if base_sha and base_sha != cur_sha:
        return out({"status": "conflict", "current_sha": cur_sha, "base_sha": base_sha,
                    "hint": "the file has changed; re-read and try again"})

    text = raw.decode("utf-8", "replace")

    # match: exact first; if 0 → try normalized line endings (CRLF→LF) — most failures die here
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
                    "hint": "old not found (even with normalized CRLF); add unique context"})
    if count != expected:
        return out({"status": "ambiguous", "count": count, "expected": expected,
                    "hint": "add surrounding context for uniqueness"})

    new_text = work.replace(o, n)
    diff = "".join(difflib.unified_diff(
        work.splitlines(keepends=True), new_text.splitlines(keepends=True),
        fromfile=path, tofile=path + " (edited)"))   # diff on an LF basis — clean to read
    if normalized and "\r\n" in text:
        new_text = new_text.replace("\n", "\r\n")     # preserve the original CRLF style on write
    new_bytes = new_text.encode("utf-8")

    if dry:
        return out({"status": "ok", "dry_run": True, "count": count,
                    "new_sha": sha256(new_bytes), "diff": diff, "normalized": normalized})

    # atomic write: temp in the SAME directory + fsync(data) + rename + fsync(dir)
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
        os.replace(tmp, path)                       # atomic on the same filesystem
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

    # verify-after-write (our niche — no SSH MCP does this)
    with open(path, "rb") as f:
        vsha = sha256(f.read())
    ok = (vsha == sha256(new_bytes))
    res = {"status": "ok" if ok else "error", "count": count, "new_sha": vsha,
           "verified": ok, "diff": diff, "normalized": normalized}
    if not ok:
        res["message"] = "verify mismatch after write"
    out(res)


if __name__ == "__main__":
    main()
