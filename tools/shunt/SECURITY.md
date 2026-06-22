# Security

`shunt` lets an AI agent run arbitrary shell commands on a remote machine. Treat any host
you add as fully controllable by whoever drives the agent. **Choose the transport by your
network's trust level.**

## secure (ssh) — recommended

- Encryption and authentication are provided by `ssh`. No extra open port, no shared token.
- Uses `ControlMaster` with a **per-destination** control socket.
- Use this for anything beyond a fully trusted LAN.

## nonsecure (daemon) — trusted LAN only

The daemon opens a TCP port (default `8766`) guarded by a shared token. Know the trade-offs:

- ⚠ **The token travels in clear text** over the network — anyone who can sniff the LAN can
  capture it and obtain a shell. There is no TLS.
- ⚠ **The token is visible in the agent's transcript** (the rewritten command carries it via
  an environment assignment). Do not treat it as a network-grade secret.
- The installer binds the daemon to `0.0.0.0` so the LAN can reach it — restrict with a
  firewall to known clients.
- Run the daemon as a **non-root** user. The systemd unit ships with a commented `User=`/
  `Group=` for exactly this; a breach then grants only that user's rights, not the whole box.

For anything resembling production, prefer **secure (ssh)**, or tunnel the daemon over SSH /
bind it to a Tailscale address and use a stronger token.

## Secrets

- Tokens live in `~/.config/shunt/token` and `/etc/shunt/daemon.env`, both `chmod 600`.
- Never commit secrets. `.gitignore` excludes `token`, `*.env`, and real configs; only
  `*.example` files are tracked.

## File edits

`shunt edit` writes atomically (temp file in the same directory → `fsync` → `rename`) and
**verifies by checksum after write**, so a partial or silently-failed write is detected
rather than corrupting the target.

## Reporting

Please report security issues via the project's GitHub issues, or privately to the
maintainer, rather than in a public pull request.
