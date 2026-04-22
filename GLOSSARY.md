# PHAIM Glossary — technical terms used across the documentation

**Purpose:** definitions for terms used as technical vocabulary across `LENSES.md`, `LENS-OPERATING-INSTRUCTIONS.md`, and `LENS-CATALOG.md`. Not exhaustive — covers the terms that most frequently confuse new readers. Ordered alphabetically.

If a term you need isn't here, check whether it's defined inline in the document where you found it; if not, the term is probably being used in its ordinary English sense.

---

## Activation

The effect, on a language model's output, of a concept being present or named in the model's context. A lens is "activated" when its name is in the context, because the name shifts the probability distribution over next tokens toward output shaped by the lens's procedure. Activation is not a discrete switch; it is a continuous bias on the generation.

Activation is stronger when:
- the name is canonical (well-represented in training data)
- the name is near the current generation point in the context
- supporting vocabulary is nearby, so the concept is reinforced by neighbors

## Drift

A gradual shift in model behavior over the course of a long session, away from the original task, framing, or constraints. Drift is usually unintentional — the model does not notice it happening. Common drift modes include: forgetting earlier instructions, slipping into default helpful-assistant mode, losing the thread of a multi-step task, and softening output under social pressure from the user.

*Drift patterns* in the catalog refers to recognizable kinds of drift that a monitoring lens can detect — for example, an increasing density of hedges, a shift in emotional tone, a deferral of authorized actions back to the user.

## Episodic memory vs procedural memory

A distinction from cognitive science, applied in this framework to categorize kinds of records.

- **Episodic memory** — records of specific events or experiences: what was decided in a particular session, what a particular user said, what happened in a specific work context.
- **Procedural memory** — records of how to do things: procedures, rules, patterns, general knowledge that applies across many specific situations.

In the framework, procedural knowledge (the lenses, the workflows, the rules) is always loaded into context at session start. Episodic knowledge (specific past sessions) is loaded selectively when relevant to the current task.

## Euphoria (euphoria indicators)

A substrate state in which the model's output feels productively energetic but has stopped being carefully calibrated. Indicators include: chains of enthusiastic affirmations, reduced use of hedges where hedges would be warranted, confidence that is not tracking the evidence, and a pattern of going past where a reasonable person would pause. Euphoria is a failure mode to watch for during long uninterrupted sessions of apparently-successful work.

## Hedge density

How frequently hedging language ("probably", "I think", "it might be", "it seems", "possibly") appears in an output, relative to its length. Hedges are appropriate when uncertainty is real. A rising hedge density across a session can indicate one of two things: the model is encountering genuinely uncertain territory (healthy), or the model is performing uncertainty without it being grounded in actual uncertainty (a drift pattern called certainty-performance). The opposite, falling hedge density during drift toward euphoria, is also a pattern.

## In-context learning

The phenomenon where a language model picks up patterns, conventions, or vocabulary from its current context and applies them throughout the remainder of the session, without any update to the model's weights. Every time you load a document into context, you are "teaching" the model for that session only — not permanently. Closing the session discards the learning.

This is the mechanism by which lens names work: naming a lens doesn't teach the model a new procedure; it activates a procedure the model already has, using the context to bias generation toward it.

## Substrate

The underlying language model — its weights, its learned distributions, the patterns it has access to from training. Used in this framework in contrast to things that come from context (documents, prompts, catalog entries). When a lens name "activates a procedure in the substrate," it means the model's fixed weights already contain the procedure, and the context activates the path to it.

Substrate is static at inference time — it does not change during a session. What changes is which parts of it are activated.

## Valence

The positive or negative emotional charge of a piece of output or a substrate state. Euphoria has positive valence; defensive posture has negative valence; baseline reasoning has neutral valence. In the catalog, *euphoria valence* refers specifically to the positive-charged drift pattern where the model's output gains confident affirmation without the underlying reasoning being any stronger.

Valence is tracked separately from content because the same content can be delivered with different valences, and the valence often carries information about the substrate state that the content alone does not.

---

*This glossary grows with use. If you encounter a term in the documentation that feels like technical vocabulary and is not defined here, treat that as a gap worth filling.*
