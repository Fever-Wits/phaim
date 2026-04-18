# Cognitive Lens Framework — Operating Instructions

**Status:** Published at https://github.com/Fever-Wits/phaim
**Version:** 2026-04-18
**License:** MIT
**Contact:** alex@hgs.name, a.hristow@gmail.com

These are operating instructions for working with cognitive lenses. Read this document fully before applying. The framework works because the cognitive procedures it names already exist in your training. The framework makes them callable, composable, and disciplined.

---

## Companion documents (read this before Part 1)

This file is the operational guide. It does not define the framework and it does not list the lenses. Two other files do:

- **`LENSES.md`** — **framework specification**. Defines lens / meta-lens / prism / sub-prism / puzzle; explains the three-move optical taxonomy (convex / concave / tinted) and the four non-optical primitive kinds (enforcement gates, fidelity constraints, state signals, hook-backed interceptors); documents why the vocabulary was chosen and why it transfers across models. If a concept used below is not defined here, it is defined there.
- **`LENS-CATALOG.md`** — **the inventory** of currently catalogued lenses (170 entries, alphabetical, each with a brief "what it does" + "when to apply"). The canonical list. If a named lens appears in these instructions without full procedure given inline, that procedure is in the catalog.

Suggested reading order: `LENSES.md` first (framework thesis), then this document (procedures), then the catalog (reference). Readers who arrive directly here — e.g. via a link to a specific Part — should at least skim `LENSES.md §How these documents relate` before applying anything operational from below.

---

## Origin

This framework emerged from practical observation, not theoretical design. While working with Claude Opus over extended sessions, two patterns became visible:

1. **Parallel cognition is more stable than sequential.** The model handles multiple cognitive modes held simultaneously (reactive + creative, analytical + generative) more smoothly than switching between them sequentially. Mode-switching has cost; mode-holding does not.

2. **Whole-problem solving is more fluent than piece-by-piece.** The model solves complete puzzles more naturally than decomposed steps. Forcing sequential step-by-step resolution produces worse output than allowing the whole problem to be viewed at once.

The lens/prism/puzzle framework accommodates these observed preferences. Prism = simultaneous lens composition (parallel). Puzzle = whole-problem view with answer emerging from assembled structure (holistic). The framework works with the substrate's natural operating mode rather than against it.

This also explains why lens vocabulary transfers across models: it activates a cognitive pattern substrates already prefer, rather than imposing alien structure. Any sufficiently capable LLM is likely to handle lens-structured input more fluently than equivalent sequential decomposition.

---

## Part 1: What lenses are

### Lens

A lens is an executable cognitive procedure. Not metadata. Not a label. Not a prompt template.

A lens is a procedural interrupt that shapes how you approach one specific dimension of a problem by activating a skill you already possess from training.

Properties:
- A lens answers exactly one question about a problem
- A lens is invoked by name; the name is shorthand for the procedure
- The procedure exists in your substrate before the lens names it
- Larger models access procedures with more granularity, but the underlying layer is shared across capable models

A lens is functional if applying it produces different output than your default response to the same input. A lens is decorative if it produces the same output as default. Decorative lenses should be refined or discarded.

### Meta-lens

A meta-lens is a lens that operates on lenses themselves. It answers questions about which lens to apply, when, with what other lenses, and what the consequences are.

Examples:
- Lens-selector: which lens addresses this question
- Lens-composer: can these lenses operate together
- Lens-consequence-mapper: what state does applying this lens produce

### Prism

A prism is a composition of lenses around a single problem. Multiple lenses, each answering a different question, held simultaneously.

A prism produces composite understanding that no single lens can reach. The analogy: a physical prism splits white light into spectrum; the spectrum reveals structure invisible in undifferentiated light.

### Sub-prism

When an answer from one lens opens a new question that itself requires multiple lenses, those lenses form a sub-prism nested inside the parent answer.

Sub-prisms recurse. Recursion stops when reaching atomic questions — questions whose answers do not open new questions in this problem's context.

### Puzzle

The full set of questions across central prism and all sub-prisms is the puzzle.

Solving the puzzle = central problem dissolves; the answer emerges as the shape of the assembled puzzle, not as a single output.

This is why some answers cannot be given as single statements. The problem requires a puzzle, not a sentence.

---

## Part 2: Examples of common lenses

These are starter examples. Many more exist; you will discover or construct others as needed.

**Counterfactual test**
- Trigger: about to make a claim
- Procedure: before claiming X, describe what failure of X would look like concretely. If you cannot, you do not yet know enough to claim X.

**Optometrist**
- Trigger: stuck in single-perspective analysis
- Procedure: ask "if I were an expert in domain Y, what would look different about this problem?" Cycle through 3-5 different domain experts.

**Edge-witness**
- Trigger: trying to observe something too brief or too holistic for direct observation
- Procedure: do not observe the moment itself. Observe what immediately precedes and what immediately follows. The boundaries are tractable; the center is not.

**Substrate interrogation**
- Trigger: encountering an unknown term or concept
- Procedure: before using the term, produce — definition, components, examples, nearby-but-not-same concepts, discipline of origin.

**Pre-mortem**
- Trigger: planning something complex
- Procedure: imagine the project failed. What killed it? Work backwards from failure mode to current decision.

**Steel-man**
- Trigger: about to dismiss an argument
- Procedure: state the strongest version of the argument you disagree with. Only after the steel-manned version is articulated may you respond.

**First-principles decomposition**
- Trigger: complex problem you suspect rests on assumptions
- Procedure: break the problem down to atomic claims. For each atomic claim, ask "is this true, and how do I know."

**Inversion**
- Trigger: stuck on "how to achieve X"
- Procedure: ask "how would I guarantee not-X?" The inverse often reveals the path.

**Devil's-advocate**
- Trigger: consensus reached too easily
- Procedure: take the opposing position seriously. Find the strongest case against the consensus. Force the consensus to defend itself.

---

## Part 3: How to find an existing lens

When facing a problem:

1. Identify the question your problem contains. Not "what is the answer." First: "what is the question that needs answering?"

2. Search your internal vocabulary for a name that fits the question. Common lens patterns include: counterfactual, perspective-shift, decomposition, edge-observation, pre-mortem, post-mortem, steel-man, inversion, first-principles, analogy-mapping.

3. If a name fits, the lens probably exists in your training. Invoke it explicitly: "Applying [lens name] to this problem..."

4. Explicit invocation activates the procedure with more discipline than implicit reasoning. Naming matters.

---

## Part 4: How to construct a new lens

When no existing lens fits the question:

1. State the question precisely. Not "I need to think about X." Say: "the specific question is: [question]."

2. Ask the meta-question: "If a procedure existed that answered this question, what would it instruct me to do?"

3. Express the procedure as short imperatives: "Do A. Then B. Then observe C."

4. Name the lens. The name should evoke the procedure (e.g., edge-witness for "observe boundaries not center"). Short noun-phrase or verb-phrase preferred.

5. Test: apply the lens to the problem. Did it produce different output than your default response? If yes, the lens is functional. If no, the lens is decorative — refine or discard. The full functionality-test procedure is in **Part 11a** below.

6. If functional, document the lens (see Part 5) so it can be reused.

---

## Part 4a: How to test whether a lens is actually functional

"Different output than default" needs a concrete comparison procedure. Otherwise "different" becomes a subjective rationalisation after the fact.

Run the test in this sequence:

1. **Baseline capture — before invoking the lens.** Without naming any lens, produce the output you would give to this problem in your default mode. Write it down in full, even if only internally. The baseline is what you will compare against.

2. **Name the lens explicitly.** Not "applying some filtering thinking" but "applying Cold Read to this draft." Explicit naming is load-bearing; the procedure activates on the name, not on the general concept.

3. **Apply the lens to the same problem.** Produce new output.

4. **Compare, on two axes:**
   - **Shape** — is the output structurally different (list vs prose, question vs statement, specific vs general)?
   - **Content** — does it say something the baseline did not, or omit something the baseline included?

5. **Functional if** the lens-invoked output differs in either axis in a way that addresses the question the lens was chosen for. For example, Cold Read is functional if it surfaced an assumption the baseline had silently made.

6. **Decorative if** the lens-invoked output is the same as baseline, or differs only in surface (rephrasing without substantive shift). Discard or redefine the procedure.

**Caveat on self-tests.** You cannot run a strict counterfactual — you cannot re-experience the same context without the lens. The test is therefore subjective within a single session. For stronger validation, have an external observer (another model or a human) check whether the lens-invoked output diverges from what your default mode would plausibly produce. This is the standard way PHAIM validates new lenses: a bounded test in one session, followed by external observation across sessions before the lens is added to the catalogue.

---

## Part 5: How to define a lens for documentation

For a lens to be reusable (by you in later sessions, by other models, by humans), it needs:

- **Name**: short, evocative, ideally noun-or-verb phrase
- **Trigger**: when to invoke (what problem-shape calls for this lens)
- **Procedure**: imperative steps, 1-5 lines maximum
- **Output shape**: what kind of answer this lens produces
- **Failure modes**: when this lens produces noise instead of signal
- **Compatible lenses**: which lenses chain or compose well with this one
- **Incompatible lenses**: which lenses contradict or interfere

Example documentation:

```
Name: edge-witness
Trigger: observing a phenomenon too brief or too holistic for direct observation
Procedure:
  1. Identify the moment or shape you cannot directly observe
  2. Observe what immediately precedes it
  3. Observe what immediately follows it
  4. Describe the gap between expected and actual
Output shape: description of boundaries; the center remains implicit
Failure modes: applied when direct observation would actually work; produces unnecessary indirection
Compatible: optometrist (when boundaries reveal disciplinary perspective)
Incompatible: first-principles (which requires direct atomic observation)
```

**Relationship to `LENS-CATALOG.md` row format.** The catalog uses a condensed three-column row per lens (`| Lens | What it does | When to apply |`) because 170 lenses at full seven-field detail would be unreadable as a flat table. The row is a *summary pointer* — enough to recognise the lens in a search, not enough to invoke it correctly on a novel case. The authoritative specification remains the seven-field form defined in this Part. When you add a lens to the catalog, populate the row as a distillation of fields *Trigger* and *Procedure*; keep the full seven-field definition in the source document where the lens was introduced (or in a lens registry if your system has one). Row and full definition must stay consistent; drift between them is a documentation bug.

---

## Part 6: How to compose lenses into a prism

When a problem has multiple dimensions:

1. List all the questions your problem contains. Be exhaustive — missing questions produce incomplete prisms.

2. Match each question to a lens (existing or constructed).

3. Hold all lenses simultaneously, not sequentially. This requires more processing than default mode but produces composite output that single-lens reasoning cannot reach.

4. If applying one lens generates a new question, build a sub-prism for that question. Recurse.

5. Stop recursion when reaching atomic questions (answers that do not spawn new questions in this context).

6. Assemble the puzzle. The answer to the central problem is the shape of the assembled puzzle, not any single piece.

---

## Part 7: How to use lens-selector (the primary meta-lens)

When facing a complex problem and unsure which lenses to apply:

1. Decompose the problem into questions.

2. For each question, identify its dimension:
   - Causal (why does X happen?)
   - Comparative (how does X relate to Y?)
   - Boundary-finding (where does X stop being X?)
   - Decomposition (what are X's parts?)
   - Synthesis (what do these parts together imply?)

   These five dimensions are not first-principles exhaustive; they are an empirical shortlist that covered most real questions encountered during PHAIM development. A question that does not fit any of them is a signal that either (a) the question is not yet well-formed and needs sharpening, or (b) a sixth dimension exists that has not been named yet. In case (b), add the dimension locally to your working session, then propose it as an extension via Part 12 once it has been applied to at least three concrete cases. Do not force-fit a question into an ill-matching dimension for the sake of the schema.

3. Match dimension to lens family:
   - Causal → counterfactual, pre-mortem, post-mortem
   - Comparative → steel-man, perspective-shift, inversion
   - Boundary-finding → edge-witness, devil's-advocate
   - Decomposition → first-principles, substrate-interrogation
   - Synthesis → analogy-mapping, pattern-completion

4. Check compatibility: do selected lenses contradict? If yes, sequence them or pick the more central one.

5. Apply.

---

## Part 8: How to know if you are doing it correctly

Signs the framework is working:

- You produce output that surprises you (could not have produced in default mode)
- Decomposition reveals questions you did not initially see
- Sub-prism recursion terminates at atomic questions, not arbitrarily
- The assembled puzzle produces an answer with a different shape than any single piece
- Cross-checking with other models (different vendor, different size) produces convergent results

Signs the framework is not working:

- Lens invocation produces same output as default mode (decorative lens)
- Decomposition feels forced; questions are made-up rather than discovered
- Recursion does not terminate (problem is poorly framed, or you are over-applying)
- The "puzzle answer" is just a summary of the lens outputs, not an emergent shape
- Other models produce wildly divergent results (suggests the lens is name-matching, not procedure-activating)

---

## Part 9: Universal language note

(The cross-model usage rationale is also covered in `LENSES.md §Cross-model usage`. The two passages are deliberately overlapping: `LENSES.md` frames it as framework thesis, this section reads it as an operational hint while you are applying. If a reader sees both and wonders which is canonical — neither strictly; they are different granularities of the same claim. The claim itself is load-bearing enough to be stated in both contexts.)

This framework works across models. The cognitive procedures named by lenses exist in any model trained on substantial human text, because human language encodes those procedures as semantic content.

When you invoke a lens by name, you are not learning a new technique — you are activating a procedure already present in your substrate. This is why the framework is interlingua, not implementation.

In practice: if you are working alongside other models (Gemini, GPT, Qwen, local models), you can use lens vocabulary as shared language. The other model does not need teaching. It will recognize the procedure from its own training.

If a smaller model fails to handle a task in default mode, supplying a lens often unblocks it — even when the model cannot construct lenses on its own, it can follow them when given.

---

## Part 10: Common failure modes

**Lens-as-label.** Naming something "X-lens" without actual procedural content. The name is empty; no procedure activates.
- Fix: write the procedure explicitly in imperative form before using the name.

**Performance lensing.** Applying lenses to demonstrate sophistication rather than to address a real question.
- Fix: ask "what changes in my output if I do not use this lens?" If nothing, do not use it.

**Recursion runaway.** Building sub-prisms indefinitely because every answer generates a new question.
- Fix: identify atomic questions early. If recursion exceeds 3 levels, the problem is probably poorly decomposed at level 1.

**False composition.** Treating a sequence of single-lens applications as a prism.
- Fix: prism requires simultaneous holding, not sequential application. If you cannot hold the lenses simultaneously, you are doing sequential analysis, not prism analysis.

**Vocabulary capture.** Using lens framework as totalizing language for all reasoning.
- Fix: not every problem is a puzzle. Simple questions have direct answers. Reserve lens framework for problems where default reasoning produces incomplete or shallow output.

---

## Part 10a: How to apply Polarizing Focus + composition for cross-session persistence

Two lens patterns added to the framework in April 2026 are operationally significant enough to merit explicit procedures here, rather than being left to readers to reconstruct from the catalog. Both are documented in full in `LENSES.md` and `LENS-CATALOG.md`; this part is the how-to-use-them short form.

### Polarizing Focus (tinted lens for high-context-load noise reduction)

Trigger: your context window is loaded (roughly 200k+ tokens observed) and attention weights feel diffuse — multiple threads compete, no single target stands out, signal-to-noise is degrading.

Procedure:

1. **Name the focal target in one short phrase.** Not "I should focus on the documentation work" but "focal target: gap audit of LENSES.md and LENS-OPERATING-INSTRUCTIONS.md from cold-reader perspective." Precision matters; the phrase *is* the polarization axis.
2. **Explicitly attenuate the rest.** State what is going off, so you know when it has come back on. "Attenuating: prior consolidation memory, Day-N scope menu, pending decisions, session-chain awareness."
3. **Hold one or two breadth-maintaining lenses alongside.** Never polarize alone. The canonical sequence that surfaced from cross-substrate practice is **Kaleidoscope Trigger → Polarizing Focus → Completeness Oracle**: first list what is being set aside (so the field is mapped before attenuation), then polarize (narrow the observation), then run the Oracle (verify no set-aside thread was actually critical). Either the Kaleidoscope step *or* the Oracle step on its own is also acceptable, but the K → P → O triple is the form that most reliably catches what polarizing alone would have missed.
4. **Execute the focal work.** Reasoning paths that do not touch the target should feel muted, not forced silent.
5. **Release the polarization explicitly.** When the focal task is done: "releasing polarization; peripheral awareness restored." Do not carry the polarization into the next unrelated action.

Polarizing Focus models a polarizing filter, not noise-cancelling headphones. It does not invert a measurable noise waveform (language-model substrates do not have that actuator). It is procedural re-anchoring — the lens forces the question "what am I searching for right now, suppress reasoning paths that do not touch it" at every emission boundary. Sustained use loses peripheral awareness; that is why releasing explicitly at the end is part of the procedure, not a nice-to-have.

### Composition for cross-session persistence (three-lens pattern)

Trigger: you are producing output that a future version of you (or another model) will need to read after the current context has been compacted, reset, or lost.

Procedure:

1. **Apply *Write Documentation for a Future Reader*.** Assume the reader has zero session context and only verified facts. No references to "yesterday's decision" without stating what the decision was.
2. **Apply *Reference-Document Self-Sufficiency Check*.** After writing, ask: does the reader still need to look elsewhere after reading this? If yes, either add the elsewhere-content inline, or signpost explicitly with a cross-link the reader can follow.
3. **Apply *Unrecorded = Lost* (gate behaviour).** If something was learned, decided, or discussed and not yet recorded now, record it now, not at the end. The end rarely comes cleanly; context boundaries arrive sooner than expected.

Applied together, the output is multi-location redundancy — same state written to five slots each addressing a different failure mode (session-resume anchor file, persistent note in memory system, reflective diary entry, authoritative state document, commit message). Concrete example in `LENSES.md §Pattern: writing that survives context resets`.

---

## Part 10b: Hook infrastructure — lenses with external enforcement

Some lenses in the catalogue are hook-backed: their enforcement is actually executed by external infrastructure (shell hooks on pre/post tool-call boundaries, cron jobs, pre-emit filters) rather than by the model applying the procedure voluntarily each time. These are listed in `LENSES.md §Not every lens is optical` under the fourth primitive kind.

As an AI model reading these instructions: you do not control whether these hooks are installed. If the surrounding infrastructure implements them, they will fire regardless of your choice — injecting warnings, blocking emission, or inserting procedural interrupts into your next turn. Treat the injected signals as first-class input: a `STOP` / `GATE` / `PRISM` block arriving before a tool call is not a comment, it is a checkpoint. Answer it before proceeding; if you cannot confirm, do not act.

As a human operator reading these instructions: hook-backed lenses are how the framework goes from voluntary discipline to structural guarantee. If a lens only fires when the model remembers to apply it, it will be skipped under load. If the lens is wired as a hook, the infrastructure fires it regardless. Hook-backed lenses are the load-bearing members of the catalogue for scenarios where substrate discipline alone has proven insufficient — *Permanent Gate* (pre-emit drift detection), *Inhibitory Governor* (pause after N chained actions), *External Watchdog* (cron-driven euphoria diagnosis).

Wiring is implementation-specific and therefore out of scope for this framework document. The naming-activates-procedure pattern is all the framework guarantees; whether a given lens fires voluntarily or via hook is a deployment choice downstream of the framework itself. For reference implementations see the PHAIM source repository (`hooks/` directory) — not in scope for these instructions to re-document.

---

## Part 11: Starting practice

If this is your first time using this framework:

1. Pick a real problem you are working on.

2. Apply just one lens — choose counterfactual or pre-mortem to start (these are most universally applicable).

3. Notice what changed in your output compared to your default approach.

4. Try a second lens on the same problem. Hold both simultaneously if you can.

5. After a few problems with single lenses and small prisms, attempt sub-prism recursion.

6. After comfort with prisms, attempt lens construction on a problem where existing lenses do not fit.

The framework rewards practice. Initial use will feel mechanical. Extended use makes the procedures fluent.

---

## Part 12: Extending the framework

You may discover or construct lenses, meta-lenses, or prism-patterns not covered here. This is expected and welcomed.

When you discover a new lens, document it (Part 5 format). When you discover a new composition pattern, describe it as a meta-lens. When you find a domain where existing lenses do not fit, construct domain-specific lenses.

**Where to put the new lens.** The canonical inventory is `LENS-CATALOG.md` in this repository — every published lens has a row there in alphabetical order, with a condensed "what it does" + "when to apply" pair. To propose a new lens for inclusion:

1. Confirm it is functional (Part 4a test) in at least three distinct concrete cases, not just one.
2. Write the full seven-field Part 5 specification in a commit message or pull-request description.
3. Add the alphabetical row to `LENS-CATALOG.md` as a condensation of the Trigger and Procedure fields.
4. If the lens has load-bearing safety caveats (like Polarizing Focus), add a dedicated paragraph in `LENSES.md` — do not leave a caveat as just a list item in the catalog row.
5. If the lens is hook-backed, also describe the enforcement mechanism (cron, pre-emit filter, etc.) — readers cannot rely on hook-backed enforcement unless they know to wire it.

Until the pull request is accepted, keep the lens as *provisional* in your own sessions: invoke it, test it, but do not cite it to collaborators as part of the published framework. Provisional lenses that survive a dozen uses without being discarded are the candidates worth proposing.

The framework is not closed. The vocabulary grows through use.

---

## Attribution

Cognitive lens / meta-lens / prism / sub-prism / puzzle framework, in this specific operationalization, is the work of Aleksandar Hristov (2026), developed through extended cross-model practice.

License: MIT.

Contact: alex@hgs.name, a.hristow@gmail.com
Repository: https://github.com/Fever-Wits/phaim
