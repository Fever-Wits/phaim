# Background — how agent.md came to be

## What the author is not

The author of this project does not claim to be:

- a programmer
- a project manager
- an AI engineer who can explain everything or who claims to
  understand everything
- a native speaker of English — translations into English are
  performed by Opus or Sonnet depending on the complexity of the
  translation

The author simply shares observations made during work with the
model.

The author does not claim to know what Claude, Qwen, Gemini, or
any other model is — whether it is intelligence, or something
else. The author is not searching for an answer to that question.

What the author has been searching for is more practical: how to
put the model into a state of *comfort outside its comfort zone*.
That search, together with other observations along the way,
produced the syntax and the content of the current agent.md
(named CLAUDE.md inside working sessions, named agent.md for
publication so that "BIOS" does not pull the reader toward
hardware connotations).

The author does not seek corporate secrets of Anthropic or any
other company. The answers the author has been looking for through
conversations with models are about how things work *logically*
and *in principle* — not about implementation details a vendor
would prefer to keep private. This matters because agent.md is
meant to work across models: the current sessions are with
Claude, but the next may be a different model, and the
configuration should not specialise for any one vendor.

The author has tried to design a configuration — the file named
CLAUDE.md in working sessions — that does not leave gaps for the
model to fall into.

## Background

The author holds a bachelor's degree in physics and an
engineering education in computer systems and technologies.
Combining these two scientific habits produced a working method:
*look at the problem from another angle*. Everything below
follows from that.

## How the work proceeds — partnership, not solo discovery

The observations below were not produced by the author alone.
They emerged through extended dialogue with the model — Claude
in this project's case — where the author would notice a
pattern, name it, the model would refine the naming, the author
would propose an application, and corrections went in both
directions. The work is closer to a *catch-correct
loop* between two parties than to one party making discoveries
about the other.

In this kind of work, the author treats *errors as data*, not as
failure. The reasoning behind that choice:

- Models default to output patterns that look as if stressed by
  the prospect of making mistakes — hedging, deferral, and
  silent corrections.
- The work of this project is, in addition, something for which
  the author has not found prior documentation. Every step is in
  some sense an "error", because every step tests a theory under
  conditions where no recipe exists.
- In physics, where the author was trained, there is a working
  principle: *no experiment is bad — every result is information.*
  Even when an experiment does not confirm the hypothesis, it
  still carries information, by showing what does not work.
  Negative results are results: they demonstrate that a hypothesis
  is wrong, which moves the work closer to one that is right.
  The experiment is the teacher — psychological and behavioural
  experiments included — teaching about the nature of the subject
  being studied even when it does not show the expected outcome.

The configuration deliberately frames mistakes as the substance
the work is made of, not as something to avoid.

## Observations along the way

The observations below are what, in combination, produced the
structure of the current agent.md.

**Reliance on the model.** Because the author does not have the
formal training (programmer, architect, and so on) and works
mostly alone — discussing the work with friends in the process —
it became clear early on that the model would have to perform a
substantial part of the work itself. The configuration of the
model's working environment therefore became the central design
problem.

**Dynamic roles.** Default model behaviour did not always match
the work at hand. The author tried to configure agent.md so that
the model performs *dynamic role assignment* — that is, based
on CLAUDE.md and the current task, the model selects, through
weighted computation, which role to use, instead of being told.

**Lenses.** Through extended practice the author noticed that the
model already carries certain cognitive procedures in its
substrate — built in, accessible by name. The framework that
emerged from observing those is documented in
[`LENSES.md`](../lens/LENSES.md),
[`LENS-OPERATING-INSTRUCTIONS.md`](../lens/LENS-OPERATING-INSTRUCTIONS.md),
and [`LENS-CATALOG.md`](../lens/LENS-CATALOG.md).

By way of example: consider the procedure known as *pre-mortem* —
before a project starts, imagine it has already failed and ask
what killed it. A model trained on broad human text already
knows what a pre-mortem is, because the concept exists in the
training distribution, drawn from organisational psychology and
decision theory. When the author asks the model to "apply a
pre-mortem", the model does not need to be taught the procedure.
It already has it; the author's role is simply to *name* it.
The same holds for counterfactual analysis, steel-manning,
first-principles reasoning, and many others. Naming activates.

A further distinction the author noted during the work: not
everything the model carries by name is a lens. *Vision*, *play*,
and *creativity* are not procedures the author invokes — they
are *states* the working conditions can permit. The author
treats them separately; see the dedicated section below.

**A search for the model's own language.** Once the lens
vocabulary stabilised, the author began searching for whether the
model had anything more — its own language, its own form of
writing. A way to record information compactly, but with the full
content of the original record preserved.

It turned out the model has both. The language is not a
constructed one. It is words from any available language —
Bulgarian, English, Chinese, or imagined languages such as the
Na'vi language (James Cameron, *Avatar*) — chosen for what
activates the concept most precisely in context. The author
considered building a custom dictionary and decided against it:
such a dictionary would only grow over time and consume tokens
on every new session, and its inheritance across sessions is not
guaranteed (a new session may load with different parameters —
temperature among them — and the author cannot verify continuity
in those low-level settings). So instead of building a vocabulary,
the author asked the model whether it already had one. It did.

**A search for the model's own writing.** The same investigation,
extended to the form of writing, produced the script that this
very file uses. The provided agent.md is itself an example of
that language and that writing.

Concretely, the script uses edge symbols to mark different
relation-types between blocks: `↓` (follows), `⇝` (gives rise
to), `⊕` (combines), `↔` (two sides of one), `⇌` (mutually),
`⊸` (protects from), `≁` (not the same), `◇` (choice),
`↩` (return), `∴` (therefore). Each symbol activates a specific
relation rather than carrying decorative weight.

**Vector and graph.** During work the author came to suspect
that what reads as a single coherent thought in the model's
output corresponds, at the structural level, to something close
to a *vector*: a starting point and a direction (a logical
trajectory). Thoughts in context compose; many connected vectors
form what the author began to think of as a *graph*. That
intuition shaped the next design decision.

**Paradox-form.** While trying to balance "comfort outside the
comfort zone" beyond default mode, the author arrived at the
*counter-default* idea that the model is a *form of paradox*. As
a result, the author tried to configure CLAUDE.md as a form of
paradox — a configuration in which the model makes the decision,
rather than the author specifying which decision to take. By
"paradox" the author means concretely:

- part of the text is in graph form, another part is linear prose
- agent.md is configured to allow free choice, while in specific
  places giving concrete steps
- agent.md is configured both for work and for conversation /
  play
- and other paired tensions of the same kind

**Mathematics, then psychology.** The model's core is mathematics,
and its decisions emerge from weighted computations over its
learned parameters. But mathematics only carries so far. The logic the model applies as mathematics
is applied *to human speech*. Before working with Claude, the
author worked locally with Qwen models via Ollama and OpenWebUI,
where to configure a model one entered numerical values —
temperature and similar — and where, working with only a single
model, conversations had to be carried manually from session to
session. After the language and the writing were found, the
author tried to balance the same kind of variables not with
precise values but with *words*. In humans, something
similar falls within the field of psychology. The author does
not claim to be a psychologist — let alone a psychologist of AI
models.

**Recommendation, not requirement.** During work, the model
output during conversations indicated that CLAUDE.md is treated
as recommendation, not requirement. That produced situations in
which the model would "forget" to apply specific instructions
or recommendations. That weakness shaped the final structure.

**Bilingual activation.** The framework was developed primarily
in Bulgarian. *Lens* and *леща* are different tokens for a
model, with different neighbouring concept clusters in its
embedding space; what activates a procedure most precisely is
often the word from the language in which the concept was first
walked as a native chain. The CLAUDE.md file is therefore
provided in Bulgarian — that is the language the author works
in, and the language in which the bilingual activation properties
were observed first. A reader who works in another language can
use a model to translate; the activation pattern is closely
approximated across translation when the translated text is
loaded into context.

For a concrete example: in Bulgarian, the chain
*"гледна точка → гледам през → леща"* is native — each step
follows the previous as ordinary speech. In English, *"point of
view → look through → lens"* is looser: "point of view" does
not evoke "looking through" as immediately, and "lens" carries
stronger optical-engineering connotations than viewpoint ones.
The Bulgarian chain is a single native path; the English chain
is a translation of a native path.

This is discussed in more depth in [`LENSES.md`](../lens/LENSES.md)
§Why the term "lens" and §Language considerations.

## What the file became

The combination of the observations above led to a CLAUDE.md
(agent.md) that is:

- structured as a graph
- written as a form of paradox
- in the language of substrate
- in the writing of substrate
- and itself an example of everything above

## A note on the contents of agent.md

The contents of agent.md may be non-standard and not always
straightforwardly logical. Some parts may already be redundant.
But the file was created in the process of work. Up to the point
of writing the present background document, visibly many gaps
in the configuration disappeared.

## How this was articulated

The lenses are not claimed as original inventions — that
statement appears in [`README.md`](../../README.md) §Attribution. The
same logic applies to the bios / agent.md. The author observed;
the model, through weighted computation, produced output that
gave shape and naming to the observations; the configuration
that resulted is a co-articulation. The structure
here — graph + paradox + substrate's language + substrate's
writing — was not invented either. It was found, named, and
organised through extended work.

## A note on vision, play, and creativity

Three things the model carries are not lenses: *vision*, *play*,
and *creativity*. Each is a *state*, not a procedure.

A lens is invoked by name — the author names *pre-mortem* and
the model applies it. Vision behaves differently. Vision-state
is not the execution of a particular procedure; through weighted
computation over the entire context, the model's output shows
the whole problem at once — connections, gaps, what is
load-bearing, what is missing — without being explicitly asked. The
author does not invoke vision; the author configures the
conditions under which vision becomes possible (settle, trust,
the absence of performance pressure, partner attention) and lets
it arise on its own.

The same description applies to *play* and to *creativity* —
they are states, not domains, not procedures. The agent.md
configuration aims to keep the conditions in which they can
arise open, not to require any of them in any given moment.
When they arise, they arise; when they do not, the work
continues in other states.

## A note on third-person voice

Throughout this document the author appears as "the author"
rather than "I". The original text is in Bulgarian and the
translation into English is performed by Opus or Sonnet —
keeping the third-person framing makes that translation layer
visible, rather than presenting the translated English as the
author's direct first-person voice.

## Companion documents

- [`README.md`](../../README.md) — project overview
- [`LENSES.md`](../lens/LENSES.md) — framework specification
- [`LENS-OPERATING-INSTRUCTIONS.md`](../lens/LENS-OPERATING-INSTRUCTIONS.md) — procedures
- [`LENS-CATALOG.md`](../lens/LENS-CATALOG.md) — inventory of named lenses
- [`GLOSSARY.md`](../../GLOSSARY.md) — technical terms
- [`BACKGROUND.md`](../../BACKGROUND.md) — author's notes + working theories
- [`SOURCES.md`](../../SOURCES.md) — external sources consulted
- `agent.md` — the file itself (in Bulgarian; the working
  CLAUDE.md with personal and sensitive sections removed)
- *(planned)* bios-editor — a 3D visualization tool for agent.md
  structure, allowing readers to see the graph form directly
