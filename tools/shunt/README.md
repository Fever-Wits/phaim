# shunt

**Transparent remote hands for AI coding agents.**

Write a plain `bash` command; it runs on a remote server and the output comes back
*identical to local* — as if the agent were on that machine. Switch machines with
`@<host>` / `@local`. No manual `ssh user@host '...'` wrapping, no quoting gymnastics,
no carrying keys and IPs in your head.

```
@84                       # switch: commands now run on the host aliased "84"
hostname                  # → ai-brain-n   (ran remotely, looks local)
cd /var/log               # remembered across commands
journalctl -u nginx -f    # streams live; interrupt kills it on the server
@local                    # back to local
```

## Why

An AI coding agent's natural output is a bare shell command. Driving a remote box over
plain `ssh` forces the agent to wrap and escape **every** command and to remember the
key + user + IP each time. For pipelines, nested quotes, `$(...)`, `awk`, heredocs, this
is fragile and the agent *will* eventually send a command to the wrong place or mangle a
quote. `shunt` removes the ceremony: configure a host once, then write commands exactly
as you would locally.

The result is identical to `ssh` — same output, same exit codes — but the cost per
command drops to zero and there is no state to carry.

## How it works

`shunt` is a **PreToolUse hook** (matcher: `Bash`) that sees each command *before* it runs
and either recognises a toggle (`@host` / `@local` / `@status`) or transparently rewrites
the command to run on the selected machine. Two transports, chosen per host:

- **secure** = `ssh` + `ControlMaster` — encrypted, authenticated, **no open port, no
  shared token**. Reuses one multiplexed connection (handshake amortised to ~ms).
- **nonsecure** = a small daemon (TCP + token) — faster on a *trusted* LAN.

Transparency comes from the hook, not from the transport — both feel identical to the
agent; only the security underneath differs. `shunt` builds on the **official** hook
mechanism, so it does not depend on any undocumented internals.

`cd` persistence, live streaming, exit-code propagation, and kill-on-disconnect all work
in both transports.

## Install

```
shunt install user@host [--alias NAME] [--key PATH] [--mode secure|nonsecure] [--port N]
```

- `secure` (default): registers the host for ssh transport. Nothing runs on the server.
- `nonsecure`: generates a token, uploads the daemon, installs a systemd unit, starts it.
  Pre-flight checks the port is free first.

The installer prints the one line to add to your Claude Code `settings.json`
(`hooks.PreToolUse`) — it does **not** edit your settings automatically.

## Usage

Toggles: `@<alias>` · `@local` · `@status`

Special operations (`shunt` CLI — these run locally and drive the transport themselves):

```
shunt hosts                          list configured hosts
shunt read  @host FILE [start:end]   show a file with line numbers (for orientation)
shunt edit  @host FILE OLD NEW       edit a remote file by CONTENT (see below)
shunt cp    SRC DST                  copy via rsync (one side @host:/path)
shunt bg    @host CMD                long-running job (systemd-run) → prints JOB=<unit>
shunt bg    @host --list|--status JOB|--stop JOB
shunt get   @host URL [DEST]         background download on the server (wget -b)
```

## Editing remote files

`shunt edit` addresses the change **by content** (`old → new`, like a search/replace),
not by line number. Line numbers drift the moment any earlier edit shifts the file;
content anchors don't. The edit is applied on the server by a small helper that:

- normalises line endings before matching (CRLF/whitespace — where most edits fail),
- **counts matches and refuses** if the count isn't what you expect (no silent
  wrong-place edit); fuzzy matching is diagnostic only, never auto-applied,
- writes **atomically** (temp file in the same dir → `fsync` → `rename` → `fsync` dir),
- **verifies by checksum after write**, then returns a unified diff.

For heavy work on a file, the bridge fallback (rsync pull → edit locally with full tools
→ rsync push, with a checksum conflict-guard) is available.

## Long-running jobs

`shunt bg` wraps the command in a `systemd-run` transient unit, so it survives disconnect,
keeps a precise exit code, and is killed cleanly as a whole process tree. Read progress
without touching the process via `journalctl`; the final status via `systemctl show`.

## Security

- **secure (ssh)** is recommended for anything beyond a trusted LAN: encrypted,
  authenticated, no open port, no shared secret.
- **nonsecure (daemon)** opens a token-guarded TCP port and is for **trusted LANs only**
  — the token travels in clear text and (because the rewritten command is visible to the
  agent's transcript) should not be treated as a network-grade secret. The daemon should
  run as a non-root user in production. See `SECURITY.md`.

## How shunt relates to similar tools

`shunt` is not the first to run an agent's shell on a remote box. Projects like
`torarnv/claude-remote-shell` and `langwatch/claude-remote` do the same core thing well.
What `shunt` does differently: it is **hook-based** (built on the documented PreToolUse
hook, rather than replacing the shell), supports **multiple named hosts** with toggling,
and is **sync-tool-agnostic** (no required Mutagen/mount).

It is also deliberately the opposite of the many **SSH-MCP servers**, where the agent
*explicitly* calls an `ssh_execute` tool and knows it is remote. `shunt`'s goal is the
reverse: make a bare `bash` command transparently local-feeling, wherever it runs.

## Requirements

- `python3` (stdlib only) on both the agent's machine and the remote server.
- `ssh` on the agent's machine. `rsync` for `shunt cp`. `systemd` on the server for `bg`.

## License

MIT — see `LICENSE`.
