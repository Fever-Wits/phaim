# Cognitive Lens Framework — Operating Instructions

These are operating instructions for working with cognitive lenses. Read this document fully before applying. The framework works because the cognitive procedures it names already exist in your training. The framework makes them callable, composable, and disciplined.

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

5. Test: apply the lens to the problem. Did it produce different output than your default response? If yes, the lens is functional. If no, the lens is decorative — refine or discard.

6. If functional, document the lens (see Part 5) so it can be reused.

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

The framework is not closed. The vocabulary grows through use.

---

## Attribution

Cognitive lens / meta-lens / prism / sub-prism / puzzle framework, in this specific operationalization, is the work of Aleksandar Hristov (2026), developed through extended cross-model practice.

License: MIT.

Contact: alex@hgs.name, a.hristow@gmail.com
Repository: https://github.com/Fever-Wits/phaim
