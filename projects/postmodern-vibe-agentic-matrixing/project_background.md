# Project Background: What Problem Is This Project Solving?

## The analysis challenge

This project asks students to confront a common problem in AI-assisted humanities research: how can a researcher use computational methods to compare interpretive qualities without pretending that interpretation has become objective measurement?

The case study focuses on the loosely named "vibe" of postmodern fiction. In ordinary literary discussion, a reader might say that a novel feels paranoid, fragmented, claustrophobic, playful, exhausting, recursive, or ontologically unstable. These impressions matter, but they are difficult to teach, compare, or reproduce because they usually remain implicit.

The project therefore turns "vibe" into a visible research apparatus. Students do not ask an LLM for one final interpretation. Instead, they split the analysis across several role-based agents, each with a restricted interpretive lens, and then collect the outputs into a matrix. The matrix does not prove what a book "really is." It creates a structured object that can be inspected, challenged, revised, and compared.

## Why postmodern fiction?

Postmodern fiction is a useful test case because many postmodern works deliberately disturb the boundaries that simple literary categories depend on. They may blur fact and fiction, destabilize time, overload the reader with documents and footnotes, parody inherited styles, or create a feeling that systems are too large to map. This makes them ideal for a lesson on theory-to-taxonomy translation and agent-based interpretation.

The sample corpus uses short descriptions of well-known postmodern works rather than full texts. That choice is pedagogically convenient but methodologically dangerous. It allows the workflow to run in a short classroom setting, but it also exposes a major limitation: the model may rely on canonical reputation, summaries, or prior associations rather than evidence from the text itself. That limitation is not a bug to hide. It is one of the main lessons.

## The central research question

The project is organized around this question:

> Can we design a transparent, reproducible, and criticizable LLM workflow for comparing the structural and affective qualities of postmodern texts, while still preserving the humanities obligation to question the categories, scores, and outputs?

## What students are really learning

Students are not simply learning to classify books. They are learning how to build and critique an interpretive machine.

The machine consists of:

- a theory-informed problem statement;
- a small corpus or set of descriptions;
- agent roles with bounded interpretive responsibilities;
- reusable prompts;
- a score matrix;
- qualitative justifications;
- reliability warnings;
- a simple reporting script;
- a discussion of where the method fails.

The educational goal is methodological transparency. Every part of the analysis should be visible enough for students to ask: Who defined this category? What evidence supports this score? What did the agent ignore? What would change if we used passages instead of summaries? What hidden assumptions entered through the prompt?

## Why the method uses multiple agents

A single LLM prompt such as "analyze the postmodern vibe of this novel" tends to produce a smooth, confident synthesis. That is often rhetorically impressive but methodologically opaque. The multi-agent setup slows the process down.

Each agent is intentionally partial:

1. **Ontological Tracker** — attends to worlds, time, reality rules, and fiction/reality boundaries.
2. **Affective Vibe-Scout** — attends to paranoia, exhaustion, irony, detachment, and structural affect.
3. **Media Formalist** — attends to layout, footnotes, typography, recursive framing, and reading friction.

The point is not that these are the only valid agents. The point is that interpretive perspective should be declared before the analysis begins.

## What counts as success?

A successful student project should not merely reproduce the sample scores. A successful project should:

- revise at least one agent role;
- explain why each score is debatable;
- identify at least one case of possible summary bias or reputation bias;
- use the report to generate a better question, not a final answer;
- propose how the workflow would improve with richer textual evidence.
