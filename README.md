# PHAIM

**Platform for Human-AI Integrated Memory**

PHAIM bridges the gap between human memory and AI context.
It allows AI models — working alongside humans — to build, navigate
and reason over a persistent knowledge graph of a working environment:
projects, infrastructure, people and ways of working.

## What is PHAIM?

PHAIM is the external memory of an AI model — structured as a causal
knowledge graph so the model can navigate not just *what* was decided,
but *why*.

It solves three problems every long-running AI collaboration faces:

* **Context loss** — long sessions get compressed, decisions get forgotten
* **Session amnesia** — every new session starts from zero
* **Topic drift** — switching context loses the thread

## Core concepts

* Ideas, tasks, bugs, and decisions tracked as a **causal knowledge graph**
* Lifecycle management: idea → task → implementation
* **Graph traversal** as primary navigation (keyword search for verification only)
* Two knowledge types: **Project** (project-specific) and **Library** (AI-owned universal reasoning patterns)
* Human and AI agents collaborate through structured workflows

## Cognitive Lens Framework

PHAIM uses a framework of **cognitive lenses** — executable cognitive
procedures that activate specific reasoning skills already present in
sufficiently capable LLMs. Lenses compose into **prisms** (multiple
lenses around one problem) and can recurse into **sub-prisms** when
answers open new questions. The full set of questions across a problem
forms a **puzzle**, and solving the puzzle lets the central answer
emerge as the shape of the assembled structure.

The framework is not PHAIM-specific or Claude-specific. It works
cross-model (Claude, Gemini, ChatGPT, Qwen) because human language
encodes cognitive procedures as semantic content, and naming a
procedure activates it across any model with access to that shared
training distribution.

Framework documentation:

* [LENSES.md](LENSES.md) — Framework specification (definitions, cross-model usage, attribution)
* [LENS-OPERATING-INSTRUCTIONS.md](LENS-OPERATING-INSTRUCTIONS.md) — Operating instructions for AI models

This framework emerged from practical observation during PHAIM
development and is published independently because it is a meaningful
contribution in its own right, regardless of PHAIM's implementation
specifics.

## Status

🚧 In active development. Not yet available for public use.

> The shift from *Management* to *Memory* was not a rename — it was a realization.
> Working with AI agents on a real project revealed that the core value
> is not managing tasks, but giving the model persistent, navigable memory
> of *why* decisions were made.

## Contact

Aleksandar Hristov — alex@hgs.name, a.hristow@gmail.com

## License

MIT
