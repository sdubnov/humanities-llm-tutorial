# Lesson 7 — Agent Roles for Interpretive Analysis

## Goal

Understand agents as roles in a research workflow, even before using technical agent frameworks.

This lesson builds on Lesson 6. Students should now be able to produce explicit reasoning traces. Agent roles are introduced as a way to divide, test, revise, and archive those traces.

---

## Agent as role

An agent does not have to be a complicated software system. At the beginning, an agent can simply be a stable role prompt.

In this course, role-based agents are used to create a controlled interpretive workflow.

```text
Theorist → Analyst → Skeptic → Editor → Archivist
```

Each role should operate on visible evidence, reasoning steps, uncertainty notes, and prior outputs.

---

## Recommended roles

### Theorist

Extracts concepts from scholarly sources and proposes taxonomies.

Questions:

- What are the main concepts?
- How are they related?
- What categories could be operationalized?

### Analyst

Applies the taxonomy to primary texts.

Questions:

- Which evidence supports each category?
- What interpretive moves are being made?
- What claims are plausible?

### Skeptic

Checks for over-interpretation, missing evidence, unclear categories, and unsupported reasoning.

Questions:

- Is the quoted evidence sufficient?
- Are categories applied consistently?
- Are there alternative readings?
- Is any cultural claim unsupported?
- Are reasoning traces too confident?

### Comparativist

Compares authors, genres, periods, groups, cultural contexts, or interpretive branches.

Questions:

- What patterns repeat across texts?
- What changes across contexts?
- Which differences are meaningful?
- Which differences may be artifacts of the prompt?

### Editor

Produces a revised interpretation after critique.

Questions:

- What should be preserved?
- What should be weakened or removed?
- What ambiguity should be acknowledged?
- What evidence should be added?

### Archivist

Summarizes sessions and updates files.

Questions:

- What prompts were used?
- What outputs were produced?
- What changed after critique?
- What files should be saved?

---

## Example role prompt: Skeptic

```text
You are the Skeptic agent.

Your job is not to produce a new interpretation.

Your job is to test whether the previous analysis is supported by textual evidence and whether the reasoning trace is methodologically sound.

Check:

1. Is the quoted evidence sufficient?
2. Are categories applied consistently?
3. Are there alternative readings?
4. Is any cultural claim unsupported?
5. Does the reasoning trace overstate certainty?
6. Are there missing uncertainty notes?

Return corrections only.
```

---

## Example workflow

Start with one short source text.

1. Theorist creates or revises the taxonomy.
2. Analyst applies the taxonomy and produces a CoT-style reasoning trace.
3. Skeptic critiques the reasoning trace.
4. Analyst or Editor revises the interpretation.
5. Comparativist compares the revised interpretation with another text or branch.
6. Archivist summarizes the workflow and saves the final files.

---

## Lab 7

Run one text through four roles:

1. Analyst
2. Skeptic
3. Editor
4. Archivist

Save each output separately:

```text
outputs/analyst_output_001.md
outputs/skeptic_output_001.md
outputs/editor_revision_001.md
session_notes/archivist_summary_001.md
```

Also save the reasoning trace being evaluated:

```text
reasoning_traces/cot_trace_001.md
```

---

## Reflection

Create:

```text
evaluations/agent_workflow_reflection_001.md
```

Answer:

- What did the Analyst produce that was useful?
- What did the Skeptic catch?
- What did the Editor improve?
- What did the Archivist preserve?
- Did the role-based workflow improve the reasoning trace?
- Did any role become redundant or theatrical?
- What would make this workflow reusable?

---

## Common failure modes

- Role names without distinct tasks
- Skeptic produces a new interpretation instead of critique
- Editor rewrites style but does not fix reasoning
- Archivist summarizes vaguely
- The workflow loses track of textual evidence
- Agents generate more text but not better method

---

## Deliverables

Submit:

```text
reasoning_traces/cot_trace_001.md
outputs/analyst_output_001.md
outputs/skeptic_output_001.md
outputs/editor_revision_001.md
session_notes/archivist_summary_001.md
evaluations/agent_workflow_reflection_001.md
```
