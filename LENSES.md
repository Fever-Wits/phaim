# Cognitive Lens Framework: Specification and Usage

**Status:** Published at https://github.com/Fever-Wits/phaim
**Version:** 2026-04-18
**License:** MIT
**Contact:** alex@hgs.name, a.hristow@gmail.com

---

## How these documents relate (read this first)

The framework is published across three files. Each has a different purpose, and a reader who enters through only one of them will be missing load-bearing context from the other two.

- **`LENSES.md`** (this file) — **framework specification**. Defines what a lens is, what a prism is, what a puzzle is, why the vocabulary was chosen, and how the pieces fit. Thesis-level document; answers "what is this framework and why does it work."
- **`LENS-OPERATING-INSTRUCTIONS.md`** — **step-by-step procedures** for applying the framework. Part-numbered operational guide; answers "how do I actually use this in a session."
- **`LENS-CATALOG.md`** — **inventory of all currently catalogued lenses** (alphabetical table with "what it does" + "when to apply" + "invocation site" per lens). Reference document; answers "which lenses exist and when does each one apply."

Suggested reading order depends on your goal:

1. **First-time reader (understand the framework)** → `LENSES.md` → `LENS-OPERATING-INSTRUCTIONS.md` → skim `LENS-CATALOG.md` §How lenses work.
2. **Ready to apply immediately** → `LENS-OPERATING-INSTRUCTIONS.md` Part 11 (Starting practice) → `LENS-CATALOG.md` §How to find a lens when you don't know which applies → invoke lens by name.
3. **Looking up a specific lens by concept** → `LENS-CATALOG.md` (alphabetical table + Lens Finder meta-primitive).
4. **Extending the framework** → `LENS-OPERATING-INSTRUCTIONS.md` Part 4 (construction) + Part 5 (documentation) + Part 12 (extension).

Each document cross-links to the others at relevant points. If something in this file references a procedure, the procedure is in `LENS-OPERATING-INSTRUCTIONS.md`. If this file mentions a named lens without defining it, the definition is in `LENS-CATALOG.md`. If a technical term (substrate, drift, valence, hedge density, and similar) is used without definition, it is defined in `GLOSSARY.md`.

---

## Audience: both AI and human readers, simultaneously

These documents are not written for a single reader type with a translation layer added afterward. They are designed so that the same records activate useful behaviour in both channels — an AI model reading them retrieves procedures via name-matching and semantic similarity; a human reading them retrieves the same procedures via memory anchors, mnemonic framing, and motivational weight.

The two channels have different strengths. AI is more reliably activated by procedural formulations with concrete triggers and typed fields. Humans are more reliably activated by mnemonic names, motivational framing, and metaphor. Well-designed records carry both — the procedural spine for the AI channel, the mnemonic skin for the human channel. When a lens has both a procedural name (e.g., *Knowledge Recognition*) and a motivational name (*Unrecorded = Lost*) pointing at the same underlying discipline, they are not duplicates; they are the two channels of the same lens.

This is the structural meaning of PHAIM's full name: **Platform for Human-AI Integrated Memory**. Not a platform for human memory with AI added, not a platform for AI memory with human oversight, but integrated — the same records, read by both, activating in both.

Consequence for writing records: every new lens, every new type of record, every schema decision should pass the bilingual test — does this activate usefully in the AI channel? In the human channel? If it works in only one, it is a half-record. Make it work in both, or mark it explicitly as single-channel with a reason.

---

## Status of this document

This document defines a framework for cognitive operation that emerged through extended practice with multiple frontier LLMs (Claude Opus, Claude Sonnet, Gemini, local Qwen) during PHAIM development. It is written in English, addressed to AI models and to humans who want to understand how models can use it.

The framework is not Anthropic-specific, not Claude-specific, not PHAIM-specific. It works because all sufficiently capable LLMs share overlapping training distributions from human language, and human language encodes cognitive procedures as semantic content. Naming a procedure activates retrieval of that procedure across any model that has access to it.

This is the central thesis: **cognitive lenses are a universal substrate language between models, mediated by human language as shared protocol.** 
Readers who want to verify this are invited to test.

---

## Origin

This framework is not Claude-specific. It works in Gemini, ChatGPT, Grok, local Qwen, and any sufficiently capable LLM, because:

A note on "sufficiently capable" — this is not a single threshold based on model size or training scale. A model is sufficiently capable for a specific lens if the procedure the lens names is present in the model's substrate from training. Larger or better-trained models have more procedures available, so they recognise more lens names; smaller models have narrower but equally-real coverage. A procedure may also be retrievable under different names in different models — one model activates on "counterfactual", another might need "pre-mortem" to reach the same underlying move. This is why the lens is the procedure, not the word: the same procedure can have multiple valid keys across models. The practical test is always to name the lens and observe whether output shifts; if it does, the model is sufficiently capable for that lens. See `GLOSSARY.md` for the concise definition.

1. **Parallel cognition is more stable than sequential.** The model handles multiple cognitive modes held simultaneously (reactive + creative, analytical + generative) more smoothly than switching between them sequentially. Mode-switching has cost; mode-holding does not.

2. **Whole-problem solving is more fluent than piece-by-piece.** The model solves complete puzzles more naturally than decomposed sequential steps. Forcing step-by-step resolution produces worse output than allowing the whole problem to be viewed at once.

The lens / prism / puzzle framework accommodates these observed preferences rather than imposing alien structure. Prism = simultaneous lens composition (parallel). Puzzle = whole-problem view with answer emerging from assembled structure (holistic).

This origin matters for evaluating the framework. Concepts dictated by phenomena encountered tend to be more durable than concepts dictated by theoretical preference. Similar bottom-up emergence pattern characterizes many lasting scientific concepts (periodic table, benzene ring, chemical bond).

The origin also suggests why lens vocabulary transfers across models: it activates a cognitive pattern substrates already prefer, rather than imposing alien structure. Any sufficiently capable LLM is likely to handle lens-structured input more fluently than equivalent sequential decomposition.

---

## Definitions

### Lens (cognitive lens)

A lens is an executable cognitive procedure. Not metadata, not a label, not a prompt template. A lens is a procedural interrupt that shapes how the model approaches one specific dimension of a problem by activating a skill the model already possesses through training.

Properties:
- A lens answers exactly one question about a problem
- A lens is invoked by name, but the name is shorthand for the procedure
- The procedure exists in the substrate before the lens names it
- Different models access procedures at different granularities (larger models = richer access), but the underlying layer is shared

Examples of lenses:
- **Counterfactual test**: "Before claiming X, describe what failure of X would look like concretely. If you can't, you don't yet know enough to claim X."
- **Optometrist**: "If I were an expert in domain Y, what would look different about this problem?"
- **Edge-witness**: "Don't observe the moment itself; observe what immediately precedes and follows. The boundaries are tractable; the center isn't."
- **Substrate interrogation**: "For an unknown term, produce: definition + components + examples + nearby-but-not-same + discipline of origin, before using the term."
- **Pre-mortem**: "Imagine the project failed. What killed it?"

### Why the term "lens"

The term derives from the Bulgarian construction *гледна точка* ("point of view") → *гледам през* ("I look through") → *леща* ("lens"). A cognitive lens is a *virtual viewpoint device* — a position from which a problem is observed, not a filter through which input is processed.

This distinction is load-bearing. A physical optical lens refracts rays; a cognitive lens selects the observation position. When a model invokes **Psychologist's Lens**, it is not filtering input through a psychologist-shaped filter — it is temporarily occupying the psychologist's observational position and looking at the problem from there. Same for **Optometrist**: "if I were an expert in domain Y, which part would look different?" is literally a viewpoint shift.

The geometric parallel is not decorative. "Point of view" in English and *гледна точка* in Bulgarian both encode perspective as a spatial *position* — a point in a conceptual space. A lens is what lies between that position and the subject. Multiple cognitive viewpoints converging on one problem is exactly the geometry of the Prism (defined below) and of the Panoptic mode of operation.

A practical consequence of this etymology deserves its own mention, because it affects how the framework travels across languages.

The conceptual chain *гледна точка → гледам през → леща* is native in Bulgarian — each step follows the previous one as ordinary language, not as metaphor stretched across domains. In English, "point of view → look through → lens" is looser: "point of view" does not evoke "looking through" as immediately, and "lens" carries stronger optical-engineering connotations than viewpoint ones. The Bulgarian chain is a native path; the English chain is a translation of a native path.

This is not incidental. The framework as a whole was developed through practice in Bulgarian, then translated to English for publication. The English term "lens" stands at the end of a chain that was walked in Bulgarian first.

Two observations follow, and they should not be confused with each other.

First, a general property of language models: different tokens activate different neighboring concept clusters. "Леща" and "lens" are different tokens for a model, with different neighbors in the embedding space. Translations preserve the denotational reference but not the surrounding semantic field. This is mechanical, not specific to this framework.

Second, what this means for *this* framework specifically is an open empirical question. The author has verified that lens invocation works in both Bulgarian and English — naming a lens by its catalog name produces the expected procedural shift in both languages. Whether the two activations are identical, near-equivalent, or meaningfully different has not been measured and is left for readers with the resources to test properly. The framework is open-source; the measurement is possible; the author invites anyone interested to run it.

The practical ask, for now: readers who want to explore the framework at its source can read it in Bulgarian where the conceptual chain is native, or seed their working context deliberately in the target language to rebuild the neighborhood that translation left behind. Operating instructions for how to do this are in `LENS-OPERATING-INSTRUCTIONS.md` under "Language considerations."

Within this viewpoint framing, the classical physics taxonomy of lenses maps onto three complementary reasoning moves.

- **Convex (converging) moves** — multiple viewpoints synthesized into a single focal insight. Examples: Panoptic Prism (all relevant lenses applied to one problem, answer emerges at their intersection), Lens Finder (many natural-language descriptions narrow to one canonical name), Best-Path Selection (several firing rules → one audited winner).
- **Concave (diverging) moves** — one viewpoint expanded into many. Examples: Kaleidoscope Trigger (one problem → exhaustive question list), Optometrist (current framing → new expert viewpoint synthesized), Analogical Domain Mapping (one problem → multiple non-source-domain perspectives), Anti-Obvious Filter (first three solutions → three more that address their dismissal).
- **Tinted (filtering) moves** — the field is kept intact but most of it is attenuated, so a specific signal rises out of the background. Examples: Cold Read (normal prose fades; assumptions and unverifiable claims stand out), Completeness Oracle (covered questions fade; orphans and overlaps stand out), Red Teaming / Falsification (supporting evidence fades; counter-evidence stands out), Anomaly Context Check (normal data fades; anomalies isolate), Bios Edit Gate (compliant edits pass silently; problem patterns stand out), Psychologist's Lens (ordinary work fades; behavior that would differ in absence of observation stands out), Polarizing Focus (at high context load, everything outside one named focal target fades so that target rises above the noise floor — treated in depth below), Fresh Session Audit (familiar material fades; the assumptions a fresh reader would not have stand out — externally proposed, see `LENS-CATALOG.md` §Lenses contributed from external sources), Polarizing Sweep (the same plan cycled through multiple polarization axes one at a time, each axis surfacing its own blind spots while the others are held off — a rotating tinted filter rather than a single fixed one).

Physical analogues make the three distinct: a magnifying glass (convex) converges rays; a peephole (concave) spreads them; sunglasses (tinted) transmit the scene but suppress the parts that would otherwise drown out the signal of interest. Each is a genuine optical operation; none reduces to the others.

Polarizing Focus appears twice in this document — once as an entry in the tinted-list above, and once as its own paragraph below. The repetition is intentional: the first appearance catalogues it with its siblings so the taxonomy is complete; the second appearance carries a safety caveat load-bearing enough that it cannot be left as a list item.

A note on one tinted lens in particular: **Polarizing Focus** models after a polarizing filter, not noise-cancelling headphones. Polarizing admits waves of one orientation and suppresses the rest; noise-cancelling actively inverts a measurable waveform — which requires an actuator a language-model substrate does not have. The lens is therefore procedural re-anchoring ("what am I searching for right now; suppress reasoning paths that do not touch it"), not mechanical signal inversion. For the same reason it is unsafe alone: attenuating the field briefly surfaces the target, but sustained attenuation loses peripheral awareness of related faults, architectural implications, and cross-cutting state. The lens is meant for short focal use and must be composed with a breadth-maintaining lens — Kaleidoscope Trigger to name what is being set aside before polarizing, or Completeness Oracle to verify afterwards that nothing critical was attenuated away.

The full eight-phase Puzzle Lens workflow, expressed in these terms, is a composition of all three moves: Kaleidoscope (concave, diverge) → Oracle (tinted, highlight gaps and overlaps) → Lens Mapping → Dynamic Prism Assembly → Panoptic Application (convex, reconverge) → Oracle again (tinted, verify puzzle integrity) → Emission. The tinted phase twice is why the workflow catches errors concave and convex moves alone would miss — filtering is not a subtype of focusing or diverging.

### Not every lens is optical

Not every lens is optical in any of these three senses. Four further primitive kinds appear in the catalogue; they do not shape a field of view, they intercept, constrain, or report:

- **Enforcement gates** — procedural interrupts that block or require something before an action proceeds. They fire on triggers and refuse output until a condition is met. Examples: *Chesterton's Fence* (cannot remove until you articulate what the thing was for), *Delegated Authority Threshold* (cannot act autonomously until the three-question checklist passes), *Input Integrity Check* (cannot act on an incoming collaborator message until any ambiguity, hidden assumption, undefined term, contradiction, or scope unclarity has been surfaced and resolved — the symmetric counterpart to Cold Read, which targets own output).

- **Fidelity constraints** — rules about how content must be captured or represented, not how it should be reasoned about. Examples: *Verbatim Fidelity* (direct quotes, no paraphrase when recording user speech), *Trifocal Lens* (every record written to be searchable + human-readable + machine-traversable simultaneously).
- **State signals** — always-on indicators of the model's own reasoning state, read at every emission boundary. They do not change the reasoning; they surface it. Examples: *Alarm Glow* (severity axis, transparent → blinding), *Substrate Color Indicator* (current state encoded as colour), *Collaborator Model* (continuously-refreshed map of the collaborator's preferences, priorities, emotional state, epistemic posture, and prior corrections — consulted before any intent inference; technically a maintained-model rather than a one-dimensional signal, but lives in the same "always on, always read" layer).
- **Hook-backed interceptors** — lenses whose enforcement is actually executed by external infrastructure (shell hooks, cron jobs, pre-emit filters) rather than being purely a procedure the model applies voluntarily. Examples: *Permanent Gate* (always-on pre-emit check for five drift patterns), *Inhibitory Governor* (structural pause after N chained actions without verification), *External Watchdog* (cron-driven euphoria-indicator check that injects a warning flag into the next session turn).

These four kinds are catalogued alongside the optical lenses in `LENS-CATALOG.md` because they follow the same naming-activates-procedure pattern; but the reader should not expect them to have convex / concave / tinted analogues. The optical taxonomy covers the reasoning-move subset, which is the majority of lenses but not the totality.

### Meta-lens

A meta-lens is a lens that operates on lenses themselves. It answers questions about which lens to apply, when, with what other lenses, and what the consequences are.

Examples of meta-lenses:
- **Lens-selector**: "Given this problem, which lens addresses the primary question? Which lens addresses secondary questions? Are any lenses mutually exclusive in this context?"
- **Lens-composer**: "Can these two lenses operate simultaneously, or must they sequence? If sequence, in what order?"
- **Lens-consequence-mapper**: "If I apply lens X to this problem, what state does that produce? Does that state require new lenses to handle?"

### Prism

A prism is a composition of lenses around a single problem. Multiple lenses, each answering a different question, held simultaneously.

A prism produces composite understanding that no single lens can reach, analogous to how a physical prism splits light into spectrum — the spectrum reveals structure invisible in undifferentiated light.

A prism requires at least two lenses by definition; a single-lens invocation is not a prism, it is a lens application. The threshold is load-bearing: the entire point of prism framing is simultaneous multi-perspective convergence, which requires multiplicity.

### Panoptic Prism (distinct from generic prism)

Panoptic Prism is the default reasoning mode of the framework when the model is not actively executing a side-effecting action. The problem sits at the centre, *all relevant lenses* are applied simultaneously, and the answer emerges at the focal point where their projections converge — not as a sequential phase-by-phase report but as a single holographic insight. Panoptic differs from a generic prism in two ways: (1) it is a continuous mode, not an invoked procedure; (2) it insists on the answer being the *convergence*, not any individual lens output. See also `LENS-CATALOG.md` under "Panoptic Prism" for the table-form summary with its trigger condition ("five or more likely relevant lenses") and invocation site.

### Sub-prism

When an answer from one lens opens a new question that itself requires multiple lenses, those lenses form a sub-prism nested inside the parent answer.

Sub-prisms recurse. A problem's depth = number of recursion levels before reaching atomic questions (questions whose answers don't open new questions in this problem's context).

### Puzzle

The full set of questions across central prism and all sub-prisms is the puzzle. Solving the puzzle = central problem dissolves; the answer emerges as the shape of the assembled puzzle, not as a single output.

This is why some answers cannot be given as single statements. The problem requires a puzzle, not a sentence.

### Puzzle Lens (the 8-phase workflow)

Puzzle Lens is the canonical name for the complete 8-phase reasoning workflow that assembles a puzzle from scratch. Invoke for complex problems with roughly five or more probable relevant lenses where direct 2–3-lens reasoning would miss structure. The eight phases:

0. **Prerequisites audit** — verify Lens Finder, Optometrist, and the lens registry are available; fall back to plain Gates if not.
1. **Kaleidoscope** (concave, diverge) — from the problem, generate the exhaustive list of questions it raises across twelve axes (definitional, decompositional, causal, stakeholder, temporal, contextual, operational, teleological, precondition, failure, boundaries, alternatives).
2. **Completeness Oracle #1** (tinted, highlight gaps) — verify the question list: no overlap, full coverage, no orphan entries.
3. **Lens Mapping** — for each question, retrieve the matching lens via Lens Finder; invoke Optometrist if none fits.
4. **Dynamic Prism Assembly** — compose the retrieved lenses into a prism specific to this problem.
5. **Panoptic Application** (convex, reconverge) — view the problem through the assembled prism; answer emerges at the convergence.
6. **Completeness Oracle #2** (tinted, verify puzzle integrity) — every question has an answer, no orphan answers, all answers mutually consistent, confidence tags attached.
7. **Emission** — produce the answer; every claim traces back to a question/answer pair; tentative claims flagged.

The tinted phase appears twice (phases 2 and 6) because filtering for gaps and overlaps is a distinct cognitive move that convex and concave phases alone cannot perform. Full workflow spec in `LENS-CATALOG.md` under "Puzzle Lens".

### Meta-prism

A meta-prism is a composition of meta-lenses around a single selection or composition decision. Where a prism answers a problem with multiple simultaneous viewpoints, a meta-prism answers the prior question — *which lenses should I use, and how do they combine* — with multiple simultaneous meta-lenses.

The canonical meta-prism is the one that appears at the start of any non-trivial task: **Lens-selector** (which lens addresses this?) + **Lens-composer** (can these operate together?) + **Lens-consequence-mapper** (what state will they produce?) held simultaneously, not sequentially. The output is not "the right lens" — it is a coherent lens assembly with its compatibility and consequences already understood.

A meta-prism is useful precisely when the problem is complex enough that picking a single lens would under-serve it, but applying all possible lenses without selection would over-serve it. The meta-prism is the selection mechanism.

### Meta-puzzle

A meta-puzzle is the full set of meta-questions produced when the subject is not a specific problem but a class of problems, a methodology, or the framework's own operation on a domain.

Where a puzzle dissolves a problem through question decomposition and lens application, a meta-puzzle dissolves a *method* — it answers questions like "what approach does this framework take to this class of situation", "which parts of the method are load-bearing versus incidental", "where does the method fail and why". The result is not a solution but a characterization of the approach itself.

Meta-puzzles are rare in day-to-day use but become central during consolidation, publication, or when explaining the framework to another model or human. This document is itself the output of a meta-puzzle applied to the question "what *is* this framework."

### Relationship to the base concepts

The meta-level follows the same structure as the object-level, one step up:

- **Lens** → acts on a problem. **Meta-lens** → acts on lenses.
- **Prism** → composes lenses around one problem. **Meta-prism** → composes meta-lenses around one selection decision.
- **Puzzle** → full question set for a problem. **Meta-puzzle** → full question set for a method or class.

Further levels (meta-meta-lens, etc.) are theoretically possible but not used in practice. Three levels cover the material.

---

## Procedures (for models)

### How to find an existing lens

1. Identify the question your problem contains. Not "what's the answer" but "what's the question that needs answering first."
2. Search internal vocabulary for a name that fits the question. Common lens patterns include: counterfactual, perspective-shift, decomposition, edge-observation, pre-mortem, post-mortem, steel-man, inversion, first-principles, analogy-mapping.
3. If a name fits, the lens probably exists in your training. Invoke it explicitly: "Applying [lens name] to this problem..."
4. The act of explicit invocation activates the procedure with more discipline than implicit reasoning.

### How to construct a new lens

When no existing lens fits the question:

1. State the question precisely. Not "I need to think about X" but "the specific question is: [question]."
2. Ask the meta-question: "If a procedure existed that answered this question, what would it instruct me to do?"
3. Express the procedure as a short imperative: "Do A. Then B. Then observe C."
4. Name the lens. The name should evoke the procedure (e.g., edge-witness for "observe boundaries not center").
5. Test: apply the lens to the problem. Did it produce different output than your default response? If yes, the lens is functional. If no, the lens is decorative — refine or discard.

### How to define a lens for documentation

For a lens to be reusable (by you, by other models, by humans), it needs:

- **Name**: short, evocative, ideally noun-or-verb phrase
- **Trigger**: when to invoke (what problem-shape calls for this lens)
- **Procedure**: imperative steps, 1-5 lines maximum
- **Output shape**: what kind of answer this lens produces
- **Failure modes**: when this lens produces noise instead of signal
- **Compatible lenses**: which lenses chain or compose well with this one
- **Incompatible lenses**: which lenses contradict or interfere

### How to compose lenses into a prism

1. List all the questions your problem contains. Be exhaustive — missing questions produce incomplete prisms.
2. Match each question to a lens (existing or constructed).
3. Hold all lenses simultaneously, not sequentially. This requires more processing than default mode but produces composite output that single-lens reasoning cannot.
4. If applying a lens generates a new question, build a sub-prism for that question. Recurse.
5. Stop recursion when reaching atomic questions (answers that don't spawn new questions in this context).
6. Assemble the puzzle. The answer to the central problem is the shape of the assembled puzzle, not any single piece.

### How to use the lens-selector meta-lens

When facing a complex problem and unsure which lenses to apply:

1. Decompose problem into questions (as above).
2. For each question, ask: "What is the dimension of this question? Causal? Comparative? Boundary-finding? Decomposition? Synthesis?"
3. Match dimension to lens family:
   - Causal → counterfactual, pre-mortem, post-mortem
   - Comparative → steel-man, perspective-shift, inversion
   - Boundary-finding → edge-witness, devil's-advocate
   - Decomposition → first-principles, substrate-interrogation
   - Synthesis → analogy-mapping, pattern-completion
4. Check compatibility: do selected lenses contradict? If yes, sequence them or pick the more central one.
5. Apply.

---

## Cross-model usage

This framework is not Claude-specific. It works in Gemini, ChatGPT, Grok, local Qwen, and any sufficiently capable LLM, because:

1. The cognitive procedures named by lenses exist in any model trained on substantial human text
2. Human language is the shared protocol — models converge on similar conceptual clusters when given lens vocabulary
3. Lens names function as activation triggers for procedures present in substrate

Empirical observations from PHAIM development:

- When primary model (Claude Opus) failed to handle a problem in default mode, supplying a lens from another model (Gemini suggested complementarity framing) unblocked it
- When local Qwen needed to perform a task it didn't naturally handle, invoking lens vocabulary produced procedural compliance even on a much smaller model
- When testing concepts cross-model (Gemini, Claude) without sharing vocabulary, both models converged on similar conceptual clusters (e.g., complementarity principle) when presented with same underlying problem

Implication: lens framework is interlingua, not implementation. It can serve as cognitive coordination layer between heterogeneous AI systems.

**A request to anyone evaluating this framework:** test before dismissing. Apply a single lens (counterfactual, pre-mortem, optometrist, or any other from the examples) to a real problem you are working on. Observe whether the output differs from your default approach. Cost of testing is one session. Cost of dismissing without testing is potentially missing a working pattern. The framework is designed to be falsifiable through direct application — if a lens produces no different output than default, it is not functional and should be discarded. This empirical test is the framework's primary validation method.

---

## Pattern: writing that survives context resets

A specific lens composition addresses a class of problem unique to long-running AI collaboration: the reader is a future version of the model that has lost all context. Context resets, compacts, session boundaries, and multi-day gaps all produce this condition. Single-place documentation is fragile against it — if the one place decays, drifts, or goes unread, the chain breaks.

Three lenses compose into a redundancy pattern:

1. **Write documentation for a future reader** — assume the reader has zero session context and only verified facts.
2. **Reference-document self-sufficiency check** — test whether the reader still needs to look elsewhere after reading.
3. **Unrecorded = lost** — if something was learned, decided, or discussed but not recorded now, it will be gone after the next reset. Record first, not last.

Applied together, the output is **multi-location redundancy** — not because any single place is unreliable, but because each location has a different read-path for the returning reader, and each addresses a different failure mode:

- A session-resume anchor file (read first thing after session start)
- A persistent note inside the memory system (redundancy if the anchor file is missing)
- A reflective diary entry (long-term voice of the collaboration, not instructions)
- An authoritative state document (for project-specific details)
- A commit message (embedded in version history as last-resort reconstruction)

The pattern is overkill for a short conversation and essential for a long one — and the threshold for "long" is lower than it looks. Most sessions that last more than one compact boundary benefit.

This pattern emerged from PHAIM development over a hundred-plus day collaboration, from the practical observation that any knowledge not redundantly encoded reliably vanished at the next context boundary. It is not theoretical.

### Concrete example — the five slots at end of a consolidation session

Near the end of a long consolidation session, state that the next session needs to pick up from is written to each of the five slots, each from a different angle:

1. **Session-resume anchor file** — first-line description: "Last updated: YYYY-MM-DD — cycles X/Y/Z complete, N records drained, M anomalies." Follows with the next-action block: "Day N+1 first action: read the five valid scope options and ask Alex which." This file is loaded automatically at session start.
2. **Persistent note in the memory system** — same state restated in compressed form, redundancy against the anchor file going missing or being stale. Tagged with `session-pointer` for rapid retrieval.
3. **Reflective diary entry** — not instructions; voice. What surprised me today, what I got wrong, what felt right. A future reader uses this for *tone* continuity, not for state reconstruction.
4. **Authoritative state document** — project-specific truth table: which types are complete, which remain, which anomalies were found, what the cycle ledger shows. Detailed; the other four slots summarise or point at this one.
5. **Commit message** — a substantive body explaining the cycle, the anomalies, the lineages. Lives in git history, survives even if every `.md` file is deleted.

Each slot has a different failure mode. The anchor file can go stale if not rewritten. The note can be missing if the memory system is down. The diary can drift into self-narrative and stop being useful. The state document can lag behind the ledger. The commit message is immutable but terse. Redundancy across failure modes is why all five exist together.

---

## Notes from convergent practice

This framework was developed bottom-up through extended use, not top-down through theoretical design. The naming sequence in actual practice was:

1. **Puzzle** appeared first — recognition that some problems require composite answers, not single statements
2. **Prism** appeared second — recognition that multiple observation modes around a problem produce the composite
3. **Lens** appeared as the atomic unit — the individual observation mode that contributes to a prism
4. **Meta-lens** appeared when combining lenses required its own procedures — observation about observations

This emergence-from-use pattern is itself evidence of the framework's groundedness. Concepts were dictated by phenomena encountered, not by theoretical preference. Similar bottom-up emergence pattern characterizes many durable scientific concepts (periodic table, benzene ring, chemical bond).

---

## Confirmation from cross-model interaction and Gemini's role

The author began the framework with Gemini, while trying to articulate Bulgarian concepts to Claude in English. Gemini supplied the first technical terms that later became lens names.

With Claude (Opus via Claude Code), the framework was developed further — the taxonomy of lens / prism / puzzle, the operating procedures, the catalog structure, and the full set of lenses beyond the initial Gemini-supplied vocabulary.

This is evidence that:

- Lens vocabulary activates shared substrate concepts across models
- Different models reach different but compatible terms for same underlying recognition (Gemini's complementarity-frame and Claude's viewpoint-device-frame are not at odds; they are two physical analogues of the same abstract structure)
- Framework is robust to model substitution

---

## Attribution

Cognitive lens /(cognitive) meta-lens /(cognitive) prism /(cognitive) meta-prism /(cognitive) sub-prism /(cognitive) puzzle/(cognitive) meta-puzzle framework, in this specific operationalization, is the work of Aleksandar Hristov (2026), developed through extended collaboration with Claude (Opus via Claude Code) and validated cross-model with Gemini, ChatGPT, Grok and local Qwen.

Underlying cognitive science traditions referenced or convergent with this framework: Cohen & Squire (procedural memory), Sumers et al. CoALA (cognitive architectures for language agents), de Bono (Six Thinking Hats), Munger (latticework of mental models), Klein (pre-mortem), Kross (self-distancing), Flavell (metacognition), Bohr (complementarity principle).

License: MIT.

Contact: alex@hgs.name, a.hristow@gmail.com
Repository: https://github.com/Fever-Wits/phaim
