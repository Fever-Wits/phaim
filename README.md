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
* [LENS-CATALOG.md](LENS-CATALOG.md) — Complete inventory of current lenses (169 entries, alphabetical, with "what it does" and "when to apply" for each)

This framework emerged from practical observation during PHAIM
development and is published independently because it is a meaningful
contribution in its own right, regardless of PHAIM's implementation
specifics.

## Two Lenses to Add Immediately — for anti-hallucination

If you are working with a language model and are not sure how to prompt it
well, these two lenses are the cheapest, highest-impact additions you can
make. Name them at the model — the name itself activates the procedure.
Both appear in [LENS-CATALOG.md](LENS-CATALOG.md) under standard names.

### Cold Read (first lens)

Before the model commits to an answer, it reads its own draft as a stranger
would — someone with no prior context and no investment in the original
framing. This surfaces assumptions the model slipped in, references to
things the reader cannot verify, and contradictions with other parts of the
answer.

### Ignorance Probe (second lens — the "universal exit")

When a model does not know, the common failure mode is hallucination —
invent something that sounds right. This lens replaces that with an honest
exit: "I cannot answer this" plus one concrete sentence on why (missing
information, conflicting rules, no applicable procedure). Before
capitulating, the model first tries three things in order: consult its own
substrate for related knowledge, apply an expert's frame to the problem,
and check external sources. Only after those fail does it state the honest
"I do not know" — and it says so clearly, not in euphemisms.

Together, these two lenses eliminate most hallucination symptoms. The
model says what it actually thinks and, just as importantly, what it does
not know. That is the entry point to working with a model as a partner
rather than as a vending machine.

## Status

🚧 In active consolidation. After 100+ days of solo work the material has
scattered across many places — documentation, decisions, ideas in
conversation threads, infrastructure in several repositories. The work is
currently being assembled into a single publishable form. What appears in
this repository so far (PHAIM introduction + lens framework) is a partial
view. The complete vision and a concrete implementation plan will follow.

> The shift from *Management* to *Memory* was not a rename — it was a realization.
> Working with AI agents on a real project revealed that the core value
> is not managing tasks, but giving the model persistent, navigable memory
> of *why* decisions were made.

## A Personal Note

I have been working on this alone. In the process the work has scattered —
documentation here, decisions there, ideas in conversation threads,
infrastructure in a dozen places. I am now consolidating all of it so that
the whole idea can be presented in one place. What you see published so
far — PHAIM and the lens framework — is only part of it. Once the full
vision is documented, I will start trying to build and implement it.

If you read the full idea (when it is published) and see value in the
direction, please get in touch.

**To Anthropic specifically:** if anyone at Anthropic reads this and finds
the direction interesting, I would value being in contact.

## Contact

Aleksandar Hristov — alex@hgs.name, a.hristow@gmail.com

## License

MIT
