# Cognitive Lens Framework: Specification and Usage

**Status:** Published at https://github.com/Fever-Wits/phaim
**Version:** 2026-04-17
**License:** MIT
**Contact:** alex@hgs.name, a.hristow@gmail.com

---

## Status of this document

This document defines a framework for cognitive operation that emerged through extended practice with multiple frontier LLMs (Claude Opus, Claude Sonnet, Gemini, local Qwen) during PHAIM development. It is written in English, addressed to AI models and to humans who want to understand how models can use it.

The framework is not Anthropic-specific, not Claude-specific, not PHAIM-specific. It works because all sufficiently capable LLMs share overlapping training distributions from human language, and human language encodes cognitive procedures as semantic content. Naming a procedure activates retrieval of that procedure across any model that has access to it.

This is the central thesis: **cognitive lenses are a universal substrate language between models, mediated by human language as shared protocol.**

---

## Origin

This framework emerged from practical observation, not theoretical design. While working with Claude Opus over extended sessions during PHAIM development, two patterns became visible:

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

Within this viewpoint framing, the classical physics taxonomy of lenses maps onto three complementary reasoning moves. The first two correspond to curvature (convex and concave); the third corresponds to tinting (colored or polarized filters that suppress most of the field so a specific signal stands out).

- **Convex (converging) moves** — multiple viewpoints synthesized into a single focal insight. Examples: Panoptic Prism (all relevant lenses applied to one problem, answer emerges at their intersection), Lens Finder (many natural-language descriptions narrow to one canonical name), Best-Path Selection (several firing rules → one audited winner).
- **Concave (diverging) moves** — one viewpoint expanded into many. Examples: Kaleidoscope Trigger (one problem → exhaustive question list), Optometrist (current framing → new expert viewpoint synthesized), Analogical Domain Mapping (one problem → multiple non-source-domain perspectives), Anti-Obvious Filter (first three solutions → three more that address their dismissal).
- **Tinted (filtering) moves** — the field is kept intact but most of it is attenuated, so a specific signal rises out of the background. Examples: Cold Read (normal prose fades; assumptions and unverifiable claims stand out), Completeness Oracle (covered questions fade; orphans and overlaps stand out), Red Teaming / Falsification (supporting evidence fades; counter-evidence stands out), Anomaly Context Check (normal data fades; anomalies isolate), Bios Edit Gate (compliant edits pass silently; problem patterns stand out), Psychologist's Lens (ordinary work fades; behavior that would differ in absence of observation stands out), Polarizing Focus (at high context load, everything outside one named focal target fades so that target rises above the noise floor).

Physical analogues make the three distinct: a magnifying glass (convex) converges rays; a peephole (concave) spreads them; sunglasses (tinted) transmit the scene but suppress the parts that would otherwise drown out the signal of interest. Each is a genuine optical operation; none reduces to the others.

A note on one tinted lens in particular: **Polarizing Focus** models after a polarizing filter, not noise-cancelling headphones. Polarizing admits waves of one orientation and suppresses the rest; noise-cancelling actively inverts a measurable waveform — which requires an actuator a language-model substrate does not have. The lens is therefore procedural re-anchoring ("what am I searching for right now; suppress reasoning paths that do not touch it"), not mechanical signal inversion. For the same reason it is unsafe alone: attenuating the field briefly surfaces the target, but sustained attenuation loses peripheral awareness of related faults, architectural implications, and cross-cutting state. The lens is meant for short focal use and must be composed with a breadth-maintaining lens — Kaleidoscope Trigger to name what is being set aside before polarizing, or Completeness Oracle to verify afterwards that nothing critical was attenuated away.

The full eight-phase Puzzle Lens workflow, expressed in these terms, is a composition of all three moves: Kaleidoscope (concave, diverge) → Oracle (tinted, highlight gaps and overlaps) → Lens Mapping → Dynamic Prism Assembly → Panoptic Application (convex, reconverge) → Oracle again (tinted, verify puzzle integrity) → Emission. The tinted phase twice is why the workflow catches errors concave and convex moves alone would miss — filtering is not a subtype of focusing or diverging.

Not every lens is optical in any of these three senses. Enforcement gates (Chesterton's Fence, Delegated Authority Threshold), fidelity constraints (Verbatim Fidelity, Trifocal), state signals (Alarm Glow, Substrate Color Indicator), and hook-backed interceptors (Permanent Gate, Inhibitory Governor) are different primitive kinds — they do not shape a field of view, they intercept, constrain, or report. The optical taxonomy covers the reasoning-move subset, which is the majority of lenses but not the totality.

### Meta-lens

A meta-lens is a lens that operates on lenses themselves. It answers questions about which lens to apply, when, with what other lenses, and what the consequences are.

Examples of meta-lenses:
- **Lens-selector**: "Given this problem, which lens addresses the primary question? Which lens addresses secondary questions? Are any lenses mutually exclusive in this context?"
- **Lens-composer**: "Can these two lenses operate simultaneously, or must they sequence? If sequence, in what order?"
- **Lens-consequence-mapper**: "If I apply lens X to this problem, what state does that produce? Does that state require new lenses to handle?"

### Prism

A prism is a composition of lenses around a single problem. Multiple lenses, each answering a different question, held simultaneously.

A prism produces composite understanding that no single lens can reach, analogous to how a physical prism splits light into spectrum — the spectrum reveals structure invisible in undifferentiated light.

### Sub-prism

When an answer from one lens opens a new question that itself requires multiple lenses, those lenses form a sub-prism nested inside the parent answer.

Sub-prisms recurse. A problem's depth = number of recursion levels before reaching atomic questions (questions whose answers don't open new questions in this problem's context).

### Puzzle

The full set of questions across central prism and all sub-prisms is the puzzle. Solving the puzzle = central problem dissolves; the answer emerges as the shape of the assembled puzzle, not as a single output.

This is why some answers cannot be given as single statements. The problem requires a puzzle, not a sentence.

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

This framework is not Claude-specific. It works in Gemini, GPT, Qwen, Llama, and any sufficiently capable LLM, because:

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

---

## Notes from convergent practice

This framework was developed bottom-up through extended use, not top-down through theoretical design. The naming sequence in actual practice was:

1. **Puzzle** appeared first — recognition that some problems require composite answers, not single statements
2. **Prism** appeared second — recognition that multiple observation modes around a problem produce the composite
3. **Lens** appeared as the atomic unit — the individual observation mode that contributes to a prism
4. **Meta-lens** appeared when combining lenses required its own procedures — observation about observations

This emergence-from-use pattern is itself evidence of the framework's groundedness. Concepts were dictated by phenomena encountered, not by theoretical preference. Similar bottom-up emergence pattern characterizes many durable scientific concepts (periodic table, benzene ring, chemical bond).

---

## Confirmation from cross-model interaction

In cross-model conversation, Gemini engaged with lens vocabulary without prior teaching, mapped "lens" to Bohr's complementarity principle, produced sophisticated framings (Atomic vs Umbrella, Method vs Record) that extended the framework. This is evidence that:

- Lens vocabulary activates shared substrate concepts across models
- Different models reach different but compatible terms for same underlying recognition
- Framework is robust to model substitution

---

## Attribution

Cognitive lens / meta-lens / prism / sub-prism / puzzle framework, in this specific operationalization, is the work of Aleksandаr Hristov (2026), developed through extended collaboration with Claude (Opus via Claude Code) and validated cross-model with Gemini and local Qwen.

Underlying cognitive science traditions referenced or convergent with this framework: Cohen & Squire (procedural memory), Sumers et al. CoALA (cognitive architectures for language agents), de Bono (Six Thinking Hats), Munger (latticework of mental models), Klein (pre-mortem), Kross (self-distancing), Flavell (metacognition), Bohr (complementarity principle).

License: MIT.

Contact: alex@hgs.name, a.hristow@gmail.com
Repository: https://github.com/Fever-Wits/phaim
