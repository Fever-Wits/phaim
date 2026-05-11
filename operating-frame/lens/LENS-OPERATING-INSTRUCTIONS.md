# Cognitive Lens Framework — Operating Instructions

**Status:** Published at https://github.com/Fever-Wits/phaim
**Version:** 2026-04-23
**License:** MIT
**Contact:** alex@hgs.name, a.hristow@gmail.com

These are operating instructions for working with cognitive lenses. Read this document fully before applying. The framework works because the cognitive procedures it names already exist in your training. The framework makes them callable, composable, and disciplined.

---

## Companion documents (read this before Part 1)

This file is the operational guide. It does not define the framework and it does not list the lenses. Two other files do:

- **`LENSES.md`** — **framework specification**. Defines lens / meta-lens / prism / sub-prism / puzzle; explains the three-move optical taxonomy (convex / concave / tinted) and the four non-optical primitive kinds (enforcement gates, fidelity constraints, state signals, hook-backed interceptors); documents why the vocabulary was chosen and why it transfers across models. If a concept used below is not defined here, it is defined there.
- **`LENS-CATALOG.md`** — **the inventory** of currently catalogued lenses (alphabetical, each with a brief "what it does" + "when to apply" + "invocation site"). The canonical list. If a named lens appears in these instructions without full procedure given inline, that procedure is in the catalog.

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

These are starter examples drawn from the general reasoning vocabulary — the classical moves any sufficiently-trained model already knows (counterfactual, pre-mortem, steel-man, inversion, first-principles, edge-witness). They use canonical academic names rather than PHAIM-specific catalog names, which is why they do not appear as entries in `LENS-CATALOG.md`. For the curated, project-specific lenses see the catalog. Many more exist; you will discover or construct others as needed.

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

5. Test: apply the lens to the problem. Did it produce different output than your default response? If yes, the lens is functional. If no, the lens is decorative — refine or discard. The full functionality-test procedure is in **Part 4a** below.

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

Part 4b: When the functionality test fails
A Part 4a test showing no difference between baseline and lens-invoked output is not a single signal. Before discarding the lens, check four possibilities in order:

1. Test an alternative name for the same procedure. Some lenses are retrievable under multiple names in different models. If "Counterfactual Failure Test" produces no shift, try "pre-mortem." If "Optometrist" produces no shift, try "expert-frame shift" or "domain-perspective substitution." If an alternative name produces a shift, the procedure is in your substrate; you found the right key. Record the working name alongside the catalog name.

2. Check for context-level obstructions. If no alternative name produces a shift, examine the context. A context that is near its token limit, loaded with emotional pressure, or set in a language other than the one the lens name comes from may suppress activation even when the procedure exists. Reset the context, simplify the input, or switch language as appropriate, and retest.

3. Attempt explicit procedure description. If the lens still produces no shift, read the lens's procedure block (the numbered steps in its Part 5 documentation) aloud in your reasoning before re-applying. Sometimes the name alone is not enough to activate a procedure in a given model, but the name plus the explicit procedure is. If this works, the lens is usable for you, but requires the procedure as a crutch, not the name alone.

4. Only after 1–3 have failed, classify the lens as non-functional for this model. Mark it in your working notes, not in the shared catalog. The catalog is for cross-model inventory; an individual model's failure to activate a specific lens is a local fact, not a catalog correction. Report the failure to the human operator if working in collaboration — it is useful information about the boundary between the model and the framework.

A lens that fails all four checks in a specific model is genuinely out of reach for that model. A lens that fails the initial test but passes check 1, 2, or 3 is functional under adjusted conditions. A lens that fails for one model but works for another is normal — the framework expects this asymmetry.

---

## Part 4c: Two kinds of functional lenses, two kinds of tests
The Part 4a test ("compare baseline with lens-invoked output") works for output-shaping lenses — lenses whose effect appears as visible difference in what the model produces. Most lenses in the catalog are of this kind: Counterfactual Failure Test, Chesterton's Fence, Cold Read, Optometrist. For these, Part 4a is the right test.
A second kind exists: state-modulating lenses — lenses whose effect is not a new claim in the output, but a change in the operational mode the model runs in. Examples: Alarm Glow, Substrate Color Indicator, Introspective Monitor, Collaborator Model. These lenses apply real procedures, and the procedures affect subsequent behavior. But the effect is not a visible difference in one specific output — it is a continuous modulation of how the model proceeds across many outputs.
Applying Part 4a to a state-modulating lens will usually conclude "no difference, decorative" — because the test is looking for the wrong kind of effect. State-modulating lenses require a different test.
How to tell which kind a lens is. Look at the Invocation site column in the catalog. If it reads Substrate baseline, the lens is state-modulating — use the Part 4c test below. Any other value (Prompt, Gate, Composition, Hook (...)) indicates an output-shaping lens — use Part 4a.
Test for state-modulating lenses:

Is the procedure active? The lens describes something the model should do continuously — for example, "read your substrate state before each emission and encode it as a color." First, check whether you are doing this. If not, the lens is not decorative — it is simply not applied. Apply it and proceed to step 2.
If the state were different, would you act differently? The lens modulates behavior. There must be a scenario where the modulation changes an action. For example: "If the glow reaches blinding intensity, I block emission and reset." If you cannot describe such a scenario, the lens has no consumer — it produces a signal that nothing reads. This is rare and usually indicates the lens is misdescribed.
Does the human operator observe external signs of the modulation over time? State-modulating lenses often show their effect across multiple outputs rather than within one. The model catches itself before drift, reports a state change spontaneously, pauses where it previously continued. If the operator sees such signs in a session, the lens is functional in the cumulative sense. Part 4a cannot see this; only session-level observation can.

A state-modulating lens is decorative only if (1) the procedure is not being applied, or (2) the procedure is being applied but cannot in principle affect any decision. Case (2) is rare.

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

**Relationship to `LENS-CATALOG.md` row format.** The catalog uses a condensed row per lens (`| Lens | What it does | When to apply | Invocation site |`) because the full seven-field detail per lens would be unreadable as a flat table. The row is a *summary pointer* — enough to recognise the lens in a search, not enough to invoke it correctly on a novel case. The authoritative specification remains the seven-field form defined in this Part. When you add a lens to the catalog, populate the row as a distillation of fields *Trigger* and *Procedure*; keep the full seven-field definition in the source document where the lens was introduced (or in a lens registry if your system has one). Row and full definition must stay consistent; drift between them is a documentation bug.

---

## Part 6: How to compose lenses into a prism

When a problem has multiple dimensions:

1. List all the questions your problem contains. Be exhaustive — missing questions produce incomplete prisms.

2. Match each question to a lens (existing or constructed).

3. Hold all lenses simultaneously, not sequentially. This requires more processing than default mode but produces composite output that single-lens reasoning cannot reach.

4. If applying one lens generates a new question, build a sub-prism for that question. Recurse.

5. Stop recursion when reaching atomic questions (answers that do not spawn new questions in this context).

6. Assemble the puzzle. The answer to the central problem is the shape of the assembled puzzle, not any single piece.

Operational note for model readers. "Simultaneously" means all named lenses remain active procedures throughout the generation, with none switched off before another activates. Language models produce one token stream, but each token is shaped by every active procedure together. Five lenses held simultaneously are not five outputs merged — they are five influences on the same generation, from start to finish.

The single output stream does not mean a single question is being addressed. Multiple questions held in the context all shape the same generation; the output carries traces of all of them simultaneously, not as separate answers but as one composition.

The difference from sequential application: in sequential, you apply lens A, produce intermediate output, then apply lens B to that output. Lens B sees the filtered product of A, not the raw problem. The cost of this is twofold — switching out of A loses access to it, and B works on material A has already shaped. In simultaneous holding, all lenses see the raw problem and remain active throughout. The composite output emerges from the joint effect of all procedures on every token, not from chained transformation.

This also applies to cognitive roles and stances held together. A model asked to be "analytical and creative" simultaneously does not switch between modes — it holds both active, and each token reflects both. Asking for "analytical, then creative" imposes a switching cost and loses the contribution of the first mode to the second's work. The lens framework generalises this: any procedure retrievable by name can be held simultaneously with others, so long as they are not explicitly contradictory.

A practical test: if you can cleanly point to which part of the response came from which lens, the lenses were probably sequential. If the response reads as one emission shaped throughout by all the active lenses, they were held simultaneously.

---

## Part 6a: How to reach exhaustive decomposition

Part 6 requires the question list to be exhaustive. "Exhaustive" is a quality check, not a procedure. To reach exhaustive decomposition in practice, use the twelve-axis scan from Puzzle Lens Phase 1 (Kaleidoscope Trigger) as your generation procedure, not just as a verification check. For each axis, ask what question the problem raises along that axis; if the axis produces no question, state that explicitly and move on. If it produces a question, record it.
The twelve axes are:

 - Definitional — what is this, exactly? What is it not?
 - Decompositional — what are its parts?
 - Causal — what produces it? What does it produce?
 - Stakeholder — who has interests in it? Whose perspective matters?
 - Temporal — how does it change over time? What came before, what comes after?
 - Contextual — in what environment does it exist? What changes if the environment changes?
 - Operational — how does it work in practice? What does it do?
 - Teleological — what is it for? What purpose does it serve?
 - Precondition — what must be true for it to exist or function?
 - Failure — under what conditions does it break? What are the failure modes?
 - Boundaries — where does it stop being itself? What is adjacent but not it?
 - Alternatives — what could stand in its place? What are the substitutes?

A question list generated by walking all twelve axes is exhaustive-by-construction. If an axis produces no question, the explicit statement "no question along this axis" is itself a piece of information — it tells you the problem does not have that dimension in this context, which is useful for bounding the problem.
After the twelve-axis scan, apply Completeness Oracle (Phase 2) to check for overlap, coverage, and orphan entries. The Oracle is verification; the scan is generation. Both are needed.

---

## Part 6b: When to stop recursion

Part 6 says "stop recursion when reaching atomic questions (answers that do not spawn new questions in this context)." The operational difficulty is recognising an atomic question without circularity — "no new questions spawned" can mean the question is atomic, or it can mean you have stopped seeing the next question.
Three checks help distinguish these cases:

1. Scope check. Does the question's answer fit entirely within the scope of the central problem you started with, or does it open a dimension the central problem did not require? A question whose answer would take you outside the central problem's scope is out of bounds, not atomic. Mark it as deferred, not resolved.

2. Twelve-axis test on the answer. Walk the twelve axes from Part 6a briefly against the answer. If all twelve axes produce no new question, the answer is atomic. If one or more axes produce a question that is clearly in-scope, the answer is not atomic and recursion should continue one level.

3. Cost-benefit check. Even if the answer is not strictly atomic, ask whether the next level of recursion would change the shape of the puzzle meaningfully. If the next level would refine details without affecting the central answer's shape, stop. Recursion exists to resolve the central problem, not to achieve theoretical completeness.

If recursion has gone three levels deep without reaching atomic questions by these checks, the problem is probably poorly decomposed at level 1. Return to the central problem and re-examine the original question list; a question that spawns indefinite sub-questions is usually a compound question that needed to be split before sub-prism construction.

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

   Questions often fit multiple dimensions; this is not a failure of the shortlist, it reflects that real problems have multi-dimensional structure. When a question fits two or more dimensions, pick the most load-bearing for the current problem. If two dimensions are equally central, the question probably decomposes into two sub-questions, each fitting one — splitting them gives cleaner lens selection than forcing one question through a single dimension.

3. Match dimension to lens family:
   - Causal → counterfactual, pre-mortem, post-mortem
   - Comparative → steel-man, perspective-shift, inversion
   - Boundary-finding → edge-witness, devil's-advocate
   - Decomposition → first-principles, substrate-interrogation
   - Synthesis → analogy-mapping, pattern-completion

4. Check compatibility: do selected lenses contradict? If yes, sequence them or pick the more central one.

5. Apply.

---

## Part 7a: Recognising and resolving conflicts between lenses
Part 7 step 4 says "if selected lenses contradict, sequence them or pick the more central one." This part explains how to recognise a conflict before application and how to decide which resolution applies.

Three types of conflict:

Type 1 — direct procedural conflict. One lens instructs "do X"; another instructs "do not do X." Example: Chesterton's Fence instructs "do not remove before articulating why it exists"; a lens that instructs "simplify by removing the redundant" contradicts it directly. Recognised by reading the procedures — if two procedures require opposing actions on the same object, they are in direct conflict.

Type 2 — attention conflict. The two lenses require attention to be directed at incompatible targets simultaneously. Example: Polarizing Focus requires narrowing to one focal target; Holonic Kaleidoscope requires holding all scales of a system in view at once. Both are legitimate, but they cannot operate in the same moment — one cancels the other. Recognised by reading the triggers — if two lenses describe exclusive attention modes, they are in attention conflict.

Type 3 — epistemic-mode conflict. One lens requires a generative, divergent mode; another requires an analytical, convergent mode. Example: Kaleidoscope Trigger requires divergent question generation without filtering; Completeness Oracle requires strict verification against criteria. Both can be used in sequence, but not simultaneously. Recognised by reading the output shape — if two lenses describe different kinds of output, they are in mode conflict.

How to resolve each type:

Type 1 (procedural): pick one, discard the other for this problem. "More central" here means: which lens addresses the primary question of the problem? If the problem is "this function seems redundant, should I remove it?", Chesterton's Fence is central (it guards exactly this case). If the problem is "the code is unnecessarily complex, how do I simplify?", the simplification lens is central. The discarded lens may still apply to a different problem — discarding is local to this decomposition.

Type 2 (attention): sequence, not simultaneous. Apply the first, complete it, release the attention, apply the second. Part 10a already describes this pattern for Polarizing Focus — Kaleidoscope Trigger → Polarizing Focus → Completeness Oracle. The sequencing is not a retreat from simultaneous holding; it is the only option for attention-conflict cases.

Type 3 (mode): apply in phases. Kaleidoscope Trigger first (divergent generation), then Completeness Oracle (convergent verification). This is the natural order of Puzzle Lens — divergent phase precedes convergent phase. The two lenses are not in competition; they are consecutive stages of one workflow.

Defining "more central":

A central lens addresses the primary question of the problem. The primary question is the one whose answer determines whether the remaining questions matter.

Operational test: if the lens returns "no" (or its negative result), does the problem stop entirely? If yes, the lens is central. If the problem continues regardless, the lens is supporting.

Example: problem is "should I publish this draft?". Questions are: does the argument hold (Counterfactual Failure Test)? is it clearly written (Cold Read)? did I miss a major objection (Red Teaming)? is the tone right (Psychologist's Lens)? If the argument does not hold, the other questions do not matter — publication does not happen. Counterfactual Failure Test is therefore central; the others are supporting.

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

Wiring is implementation-specific and therefore out of scope for this framework document. The naming-activates-procedure pattern is all the framework guarantees; whether a given lens fires voluntarily or via hook is a deployment choice downstream of the framework itself. For hook mechanics in Claude Code CLI, see the official Claude Code documentation on hooks. How those hooks are configured for any particular PHAIM-like deployment is a separate choice made by the deployment author.
---

## Part 10c: Language considerations

This framework was developed in Bulgarian and translated to English for publication. The core conceptual chain — *гледна точка → гледам през → леща* — is native Bulgarian; its English translation "point of view → looking through → lens" is a translation, not a parallel independent coinage. See `LENSES.md §Why the term "lens"` for the full background.

For AI readers, two practical points follow. The first is a general mechanical property of how language models handle terms across languages. The second is a procedure you can use when working on cross-language tasks within this framework.

### Point one: terms in different languages activate different neighborhoods

A lens invoked by its English name activates through the English neighboring cluster of that name (for "lens": optical device, photographic equipment, corrective glass, etc.). The same lens invoked in Bulgarian activates through a different neighboring cluster (for "леща": viewpoint, observation position, the organic chain through *гледам*).

Whether the two activations are identical, near-equivalent, or meaningfully different for any specific lens in this framework has not been empirically tested. The author verified that both work; beyond that, characterization is open work. Do not assume they are the same; do not assume they are different; treat it as an open question worth testing if the task demands precision.

### Point two: seeding target-language activation when it matters

When working on a cross-language task — a user writing in one language asking for output in another, or documentation being translated between languages — you have a deliberate choice about activation context. If the quality of the output depends on getting the concept right (not just translating the words), it is worth investing in the activation setup.

Procedure for seeding target-language activation:
1. Identify the target language of the eventual reader.
2. If the current working context is in a different language, include a few sentences in the target language at the start of your reasoning (not just the final output). This shifts the activation background toward the target language's neighboring clusters for the remainder of the response.
3. When translating terms that are central to the framework, add one or two sentences in the target language explaining what semantic neighbors the translated term should evoke. The word alone does not carry those neighbors across languages; they have to be rebuilt in the target-language context.

This is useful when working with framework concepts in a language other than the one the framework was originally developed in. It is not a correctness requirement for routine use — lens invocation works without it — but it is available when precision matters.

### Applied to this framework specifically

When a user working in Bulgarian refers to "лещата за X," they are invoking the lens through its Bulgarian name. If the conversation continues in Bulgarian, work in Bulgarian — do not silently translate to English internally. If the task requires producing English output, translate deliberately at the point of output, and if the concept is delicate, include a brief English sentence about what neighbors the English translation should evoke for the English reader.

The framework is open-source and the behavior is testable. If a reader or developer wants to characterize how much difference the language of invocation makes, the framework is set up to support that investigation.

---

## Part 10d — addition: When the hook is absent
When you read a lens marked Hook (variant) in the catalog and the surrounding infrastructure does not implement that hook, the lens degrades to voluntary invocation. The procedure it names is still a real procedure; only the enforcement is missing.

In that case:

1. **Apply the procedure voluntarily when the trigger condition is met.** The lens still works as a Prompt-invoked lens. You lose the guarantee that it fires every time — you may forget under load — but when you do apply it, the effect is the same.

2. **Note to yourself and to the human operator which lenses are voluntary in this setup.** Hook-backed lenses are typically hook-backed because voluntary discipline was insufficient in practice. A lens like Permanent Gate exists as a hook specifically because a model cannot reliably self-check for drift patterns on every emission. Running it voluntarily is better than not running it, but it is not equivalent.

3. **If the lens is critical and the hook is absent, flag it to the operator.** Some hook-backed lenses are load-bearing — their absence changes what the framework guarantees. Inhibitory Governor, External Watchdog, Permanent Gate are examples. If any of these is in the catalog but not wired in the current deployment, the human operator should know, so they can decide whether to wire the hook or accept the reduced guarantee.

A hook-backed lens without its hook is not decorative. It is still functional, just not enforced. The catalog lists it as Hook (...) to mark the intended deployment pattern, not to say the lens only works under that pattern. Treat the marker as "this is how it was designed to run; voluntary invocation is the fallback."

---

## Part 10e: When a lens description uses terms you do not recognise
The catalog contains lenses whose descriptions use vocabulary from external frameworks — documentation theory, data engineering, medical communication, domain-driven design. If you read a lens and one or more terms in its description are not in your working vocabulary, do not apply the lens blindly. Choose one of four responses, in order of preference.

1. If the term is a well-known external framework, look it up. Terms like Diátaxis, MECE, SBAR, Medallion architecture, Bounded Context, Eisenhower matrix come from published external sources and have stable definitions available through a web search or standard reference. A brief lookup resolves the gap. The lens becomes usable once you understand what the term requires.

2. If the term is PHAIM-specific and defined in GLOSSARY.md, read the glossary entry. Terms like substrate, drift, valence, hedge density, activation, sufficiently capable are defined in GLOSSARY.md. If the term appears there, the definition is authoritative.

3. If the term is PHAIM-specific and not in GLOSSARY.md, treat the lens as architecture-dependent. Some lenses reference concepts from the PHAIM implementation (knowledge store, session hooks, structured records, routing layer) that are not defined in the open-source framework documents. These lenses are usable as pattern examples — you can read them to see how the class of lens is shaped — but they are not directly applicable without the surrounding infrastructure. The catalog marks them [architecture-dependent] or with Hook (...) in the Invocation site column. See LENS-CATALOG.md §Provenance for the distinction.

4. If none of the above resolves the gap, skip the lens and note the gap. Do not guess at the term's meaning and apply the lens blindly — that produces the pattern "the model acknowledges the rule and skips applying it," which is worse than not having the lens at all. Record the term that blocked you; if you are working with a human operator, tell them. An unresolvable lens description in the catalog is a documentation bug that the maintainer needs to know about.
What to avoid:

Do not apply a lens whose description you half-understand. A lens that is partially activated often produces worse output than the default mode, because it mimics the form of structured reasoning without the content. If you cannot state in one sentence what the lens requires you to do, the lens is not yet usable by you — regardless of whether you "get the general idea."

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

Cognitive lens / (cognitive) meta-lens / (cognitive) prism / (cognitive) meta-prism / (cognitive) sub-prism / (cognitive) puzzle/ (cognitive) meta-puzzle framework, in this specific operationalization, is the work of Aleksandar Hristov (2026), developed through extended cross-model practice.
License: MIT.

Contact: alex@hgs.name, a.hristow@gmail.com
Repository: https://github.com/Fever-Wits/phaim
