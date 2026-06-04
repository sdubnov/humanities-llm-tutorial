# Advanced Lesson 3 — Loop Patterns, Multi-Turn Reasoning, and Agent Orchestration

## Goal

Learn how reasoning traces, multi-turn interaction, agents, and loops fit together in an advanced humanities research workflow.

The introductory course asks:

```text
How can we make reasoning explicit?
```

This advanced lesson asks:

```text
How can we run, critique, revise, evaluate, and stop a reasoning workflow?
```

---

## Core Distinction

CoT, ToT, multi-turn interaction, agents, and loops are related, but they are not the same thing.

| Concept | What it is | Example |
|---|---|---|
| CoT | Linear reasoning path | Evidence → interpretation → uncertainty → claim |
| ToT | Branching reasoning path | Political reading vs psychological reading vs formal reading |
| Multi-turn interaction | Conversation over several turns | Ask, critique, revise, summarize |
| Loop | Repeated workflow with rules | Analyze → critique → revise until acceptable |
| Agent | Role or function inside a workflow | Analyst, Skeptic, Editor |
| Orchestration | Control logic | Who acts next? What input do they receive? When do we stop? |

The most important point:

```text
A loop is not just “ask again.”
A loop has roles, state, inputs, outputs, evaluation, and termination criteria.
```

---

## What a Loop Contains

A loop has six parts:

```text
1. Task
2. State
3. Roles / agents
4. Actions
5. Evaluation
6. Termination condition
```

Example:

```text
Task:
Analyze metaphor in a passage.

State:
Current annotation, critique notes, revision history, score.

Roles:
Analyst, Skeptic, Editor, Evaluator, Archivist.

Actions:
Analyze, critique, revise, score, save.

Evaluation:
Rubric score for evidence, uncertainty, and structure.

Termination:
Stop after 2 rounds or when score ≥ 4 out of 5.
```

---

## Methodological Principle

Loops are not there to produce more text.

They are there to make revision accountable.

Agents are not characters.

They are functions in a workflow.

```text
Analyst = produces candidate interpretation
Skeptic = identifies methodological weaknesses
Editor = revises according to critique
Evaluator = applies rubric
Archivist = preserves state and provenance
```

---

## Worked Example

This lesson uses the same basic example from the earlier advanced lessons.

Source text:

```text
The city was a broken mirror, reflecting every dream I had lost.
```

Goal:

```text
Improve a metaphor annotation until it is structurally complete and interpretively careful.
```

Loop:

```text
Analyst
→ Skeptic
→ Editor
→ Evaluator
→ repeat if needed
→ Archivist
```

Use the files in:

```text
worked_example/
```

---

## Manual Orchestration

The first implementation is manual.

Students copy outputs from one role to the next.

```text
1. Prompt Analyst.
2. Copy Analyst output into Skeptic prompt.
3. Copy Skeptic critique into Editor prompt.
4. Copy Editor revision into Evaluator prompt.
5. If score passes, ask Archivist to summarize.
6. If not, repeat the loop.
```

This is the best first version because students can see exactly what is happening.

---

## Scripted Orchestration

After the manual version, students inspect pseudocode for a scripted controller.

See:

```text
scripts/loop_controller_pseudocode.py
```

The controller shows the logic:

```text
while score is below threshold and max rounds not reached:
    run analyst
    run skeptic
    run editor
    run evaluator

run archivist
```

Students do not need to implement a full agent framework. The goal is to understand the control logic.

---

## Termination Criteria

Loops need stopping rules.

Possible termination criteria:

```text
Stop after N rounds.
Stop when average score ≥ threshold.
Stop when no required revisions remain.
Stop when the same critique repeats.
Stop when human reviewer approves.
Stop when ambiguity is documented rather than resolved.
```

For humanities workflows, this is especially important:

```text
A loop does not always end by finding certainty.
Sometimes it ends by documenting unresolved ambiguity.
```

---

## Named Loop Patterns

### Critique–Revision Loop

```text
Analyst → Skeptic → Editor
```

Best for improving interpretive quality.

### Reflexion Loop

```text
Generate → Critique → Lesson learned → Retry
```

Best for saving what went wrong so the next round improves.

### ReAct Loop

```text
Reason → Act → Observe → Reason
```

Best when the model needs more evidence.

### Tree-of-Thought Loop

```text
Generate branches → evaluate branches → prune or synthesize
```

Best when several interpretations are plausible.

### Evaluator–Optimizer Loop

```text
Generate → score → revise → repeat
```

Best when there is a rubric.

---

## Lab 3 — Build and Run an Interpretive Loop

### Part A — Choose a source text

Use the worked example or choose a short passage from the Lesson 2 corpus.

### Part B — Choose a loop type

Choose one:

```text
critique-revision
ReAct
Reflexion
Tree of Thought
Evaluator-Optimizer
Debate loop
```

### Part C — Define roles

At minimum:

```text
Analyst
Skeptic
Editor
Evaluator
Archivist
```

### Part D — Define loop state

Use:

```text
templates/loop_state_template.md
```

### Part E — Run one full loop manually

Save each stage:

```text
outputs/analyst_output.md
outputs/skeptic_critique.md
outputs/editor_revision.md
outputs/evaluator_score.md
outputs/archivist_summary.md
```

### Part F — Apply termination criteria

Decide whether to stop or repeat.

Explain why.

### Part G — Archive the loop

Save:

```text
outputs/final_loop_reflection.md
```

---

## Deliverables

Submit:

```text
outputs/loop_plan.md
outputs/analyst_output.md
outputs/skeptic_critique.md
outputs/editor_revision.md
outputs/evaluator_score.md
outputs/archivist_summary.md
outputs/final_loop_reflection.md
```

---

## Final Reflection Questions

1. What made this a loop rather than just a conversation?
2. What was the loop state?
3. Which role improved the analysis most?
4. What did the Evaluator measure?
5. What was the stopping condition?
6. Did the loop resolve ambiguity or document it?
7. What part of this workflow could be automated?
8. What part should remain human-reviewed?
