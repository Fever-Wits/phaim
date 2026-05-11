# Agent Visualization — design specification

A specification for a 3D visualization tool that surfaces the
graph structure of `agent.md`. Includes parser, server, and
frontend skeletons sufficient to bootstrap a reproduction;
read the security notes before deploying.

## Purpose

The agent.md file (named CLAUDE.md in working sessions) is
written as a graph composed of named blocks connected by typed
edges. Read as linear text, the graph structure does not surface
visually. A visualization tool makes the graph form directly
observable: which blocks connect, which paradox pairs are
formed, which states emerge from which conditions.

The visualization is intended for *internal use* by the
configuration's author during work — to see whether the
structure remains coherent as the file evolves, to spot orphan
blocks, to verify that paradox pairs remain balanced when blocks
are added or removed.

## Idea

Parse agent.md into a graph and render it in 3D.

- **Blocks** become nodes, identified by their bracketed names
  (e.g. `[пристигане]`, `[drift / catch]`). The first ~200
  characters of the block body appear on the node as a card or
  expanded preview — not just a tooltip on a sphere. The reader
  should see content directly through the visualization.
- **Edges** are extracted from the edge symbols defined at the
  top of the file: `↓ ⇝ ⊕ ↔ ⇌ ⊸ ≁ ◇ ↩ ∴` (and any others the
  configuration introduces). Each edge type has its own colour
  and style — for example, `↓` thin grey, `⇝` thicker orange,
  `↔` purple bidirectional, `⊸` dashed red.
- **Blocks referring to other blocks by name** in their body
  text produce additional edges (cross-references).
- The opening line of the file ("Добро утро :)" in the current
  configuration) is treated as a central focal node. Other
  blocks radiate from it under a gentle gravitational pull
  toward the centre.

## Parser

A parser splits the file by separator lines (`═══════════════════════════`),
reads the bracketed block name at the start of each chunk,
and extracts edges by scanning for the defined edge symbols
within and between chunks. Block type can be inferred from
keyword matching in the body (for example, the presence of
"парадокс" → paradox type).

The parser should emit warnings:

- **orphan** — a block with no incoming or outgoing edges
- **asymmetric bidirectional** — `↔` or `⇌` used in one
  direction without a corresponding reverse pair
- **undefined symbol** — an edge symbol appearing in body text
  that is not declared in the edge legend

## Server

A small HTTP server reads the file on demand, parses it, and
serves the graph as JSON. A filesystem watcher detects edits
to the file and broadcasts a refresh event over WebSocket so
the visualization updates without manual reload.

Endpoints:

- `GET /` — the visualization frontend (HTML + JS + CSS)
- `GET /api/bios` — current parsed graph as JSON (nodes, edges,
  edge legend, warnings)
- `WS /ws/refresh` — push refresh events on file change

For a public reproduction, the server should be bound to
`localhost` only (not exposed to the network), and the source
path should be a placeholder value (e.g. `/path_to_file/agent.md`)
that the reproducer adjusts for their own setup.

## Frontend

A two-column layout works well:

- **Left:** short cards listing the blocks (block name + first
  line), optionally a small overlay showing current focus or
  current role-state if such signals are available from the
  surrounding environment.
- **Right:** a 3D force-directed graph occupying the larger
  portion of the viewport. Nodes coloured by block type. Edges
  drawn in the defined symbol colours. Clicking a node centres
  the graph on it and expands the node's content preview.

A 2D fallback view (a simpler graph rendering) is useful when
the 3D view is too dense to read or when running in environments
without WebGL.

## Recommended libraries

Any sufficiently capable model can recreate the tool with
publicly available libraries — for example:

- `3d-force-graph` for 3D force-directed rendering
- `vis-network` for the 2D fallback
- FastAPI or another lightweight HTTP framework (Flask, Starlette)
- `watchdog` or another filesystem-watching library
- standard WebSocket support

The choice is not load-bearing. What matters is that the parser
captures the graph that agent.md already is, and that the
rendering surfaces it visually.

## Software versions tested

The implementation that produced this specification used the
following versions. Other versions likely work; these are the
ones empirically verified.

- Python 3.11+
- FastAPI 0.110+
- uvicorn 0.27+
- watchdog 4.0+
- pydantic 2.6+
- 3d-force-graph 1.73+
- vis-network 9.1+
- pytest 8.0+ (parser tests)

## Example code (skeleton)

The snippets below are skeletons sufficient to bootstrap a
reproduction. They are not full implementations; production
adaptation requires the security notes that follow.

### Security notes (read before using)

- The server must bind to `127.0.0.1` (localhost) only. Never
  expose to a network without authentication.
- The path to `agent.md` must be hard-coded or read from a
  trusted config — never accept it from user input or query
  string (path-traversal risk).
- The frontend renders block body content. Sanitize the body
  if rendering as HTML; the safe path is to render as plain
  text with explicit escaping.
- WebSocket message handlers must validate message origin if
  the server is ever exposed beyond localhost.

### Parser — block split and edge extraction (Python)

```python
import re
from dataclasses import dataclass

EDGE_SYMBOLS = {
    "↓": "follows",
    "⇝": "gives rise to",
    "⊕": "combines",
    "↔": "two sides of one",
    "⇌": "mutually",
    "⊸": "protects from",
    "≁": "not the same",
    "◇": "choice",
    "↩": "return",
    "∴": "therefore",
}

@dataclass
class Block:
    name: str
    body: str
    first_line: str

@dataclass
class Edge:
    source: str
    target: str
    symbol: str

def parse_blocks(text: str) -> list[Block]:
    """Split file by separator lines and extract bracketed block names."""
    sections = re.split(r"\n═{20,}\s*\n", text)
    blocks: list[Block] = []
    for section in sections:
        match = re.match(r"\s*\[([^\]]+)\]", section)
        if not match:
            continue
        name = match.group(1).strip()
        body = section[match.end():].strip()
        first_line = body.split("\n", 1)[0] if body else ""
        blocks.append(Block(name=name, body=body, first_line=first_line))
    return blocks

def extract_edges(blocks: list[Block]) -> list[Edge]:
    """Scan block bodies for edge symbols and the [name] references
    that follow them within a few lines. Implementation detail:
    proximity-based pairing — refine for your own discipline."""
    name_set = {b.name for b in blocks}
    edges: list[Edge] = []
    for b in blocks:
        for symbol in EDGE_SYMBOLS:
            for match in re.finditer(re.escape(symbol), b.body):
                window = b.body[match.end():match.end() + 200]
                target = re.search(r"\[([^\]]+)\]", window)
                if target and target.group(1).strip() in name_set:
                    edges.append(Edge(
                        source=b.name,
                        target=target.group(1).strip(),
                        symbol=symbol,
                    ))
    return edges
```

### Server — FastAPI + watchdog (Python)

```python
import asyncio
import json
from pathlib import Path

from fastapi import FastAPI, WebSocket
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BIOS_PATH = Path("/path_to_file/agent.md")   # adjust for your setup
HOST = "127.0.0.1"                           # localhost only
PORT = 8765

app = FastAPI()
connections: set[WebSocket] = set()

@app.get("/api/bios")
def get_bios() -> dict:
    text = BIOS_PATH.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    edges = extract_edges(blocks)
    return {
        "nodes": [
            {"id": b.name, "first_line": b.first_line, "body": b.body}
            for b in blocks
        ],
        "links": [
            {"source": e.source, "target": e.target, "symbol": e.symbol}
            for e in edges
        ],
    }

@app.websocket("/ws/refresh")
async def ws_refresh(ws: WebSocket) -> None:
    await ws.accept()
    connections.add(ws)
    try:
        while True:
            await ws.receive_text()
    finally:
        connections.discard(ws)

class BiosWatcher(FileSystemEventHandler):
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
    def on_modified(self, event) -> None:
        if Path(event.src_path) == BIOS_PATH:
            for ws in list(connections):
                asyncio.run_coroutine_threadsafe(
                    ws.send_text("refresh"), self.loop
                )

if __name__ == "__main__":
    import uvicorn
    loop = asyncio.new_event_loop()
    observer = Observer()
    observer.schedule(BiosWatcher(loop), str(BIOS_PATH.parent), recursive=False)
    observer.start()
    uvicorn.run(app, host=HOST, port=PORT, loop="asyncio")
```

### Frontend — 3d-force-graph initialization (JavaScript)

```javascript
const EDGE_COLORS = {
    "↓": "#888", "⇝": "#f80", "⊕": "#c60", "↔": "#a0a",
    "⇌": "#06a", "⊸": "#f00", "≁": "#444", "◇": "#0c0",
    "↩": "#cc0", "∴": "#fff",
};

async function load() {
    const res = await fetch("/api/bios");
    const data = await res.json();

    const graph = ForceGraph3D()(document.getElementById("graph"))
        .graphData({ nodes: data.nodes, links: data.links })
        .nodeLabel(n => `[${escapeHtml(n.id)}]\n${escapeHtml(n.first_line)}`)
        .linkColor(l => EDGE_COLORS[l.symbol] || "#888")
        .linkDirectionalArrowLength(3);

    const ws = new WebSocket(`ws://${location.host}/ws/refresh`);
    ws.onmessage = () => load();  // reload on file change
}

function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g,
        c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;",
                '"': "&quot;", "'": "&#39;" })[c]);
}

load();
```

These skeletons cover the three main moving parts. A
reproducer adapts the path constant, the edge-color palette,
and the layout preferences to taste.

## What the visualization is for

Not for end users of the configuration. For its *author* — to
see whether new blocks orphan, whether paradox pairs remain
balanced, whether removals leave dangling references. Reading
the file linearly hides this; reading it as a graph surfaces it.

The tool is therefore part of the operating-frame, not part of
the configuration itself.

## What this specification is not

This specification does not include source code, and the project
does not publish the implementation. The reasons are practical:
the existing implementation has not been audited for security
in a public-deployment context, and publishing code introduces
maintenance and dependency obligations that go beyond the scope
of the framework.

A reader who wishes to use a visualization of this kind is
invited to build one. The idea above is sufficient.
