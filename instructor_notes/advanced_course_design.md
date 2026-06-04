# Instructor Notes — Advanced Humanities LLM Research Platforms

## Purpose of This Document

This document is the instructor guide for the advanced course sequence.

The introductory course teaches students to move from casual LLM use toward explicit, reproducible humanities methods:

```text
chatting
→ prompting
→ files
→ rules
→ taxonomies
→ multi-turn interaction
→ explicit reasoning traces
→ role-based agents
→ research workflows
```

The advanced course teaches students how to turn those methods into operational research systems:

```text
skills and tools
→ RAG and context engineering
→ loop orchestration
→ research harnesses
→ annotation assets and model adaptation
→ humanities research platform
```

The central instructor message is:

```text
The advanced course is not about adding more AI features.
It is about turning LLM-assisted interpretation into an operational research system.
```

---

## Advanced Course Philosophy

The advanced course should not be taught as a software engineering course, even though it introduces software-engineering concepts.

It should be taught as a course in **method operationalization**.

Students should learn how to make interpretive work:

- explicit
- grounded
- testable
- revisable
- auditable
- reproducible
- ethically reviewable

The key pedagogical shift is:

```text
Introductory course:
How do we use LLMs carefully for humanities interpretation?

Advanced course:
How do we build a research environment that constrains, supports, evaluates, and archives LLM-assisted interpretation?
```

---

## Core Advanced Progression

The course progression is:

```text
Lesson 1:
Skills, tools, MCP, and Python helpers

Lesson 2:
RAG and context engineering

Lesson 3:
Loop patterns, multi-turn reasoning, and agent orchestration

Lesson 4:
Research harnesses and evaluation harnesses

Lesson 5:
Annotation assets and model adaptation

Lesson 6:
Capstone humanities research platform
```

This sequence should be explained as a cumulative architecture:

```text
Skill:
packages the method

RAG:
grounds the method in documents

Loop:
improves outputs through critique and revision

Research harness:
operationalizes rules, resources, checks, policies, and archives

Annotation assets:
preserve examples for reuse, evaluation, and possible model adaptation

Platform:
assembles all components into a reproducible research environment
```

---

## Core Slogan

Use this slogan throughout the advanced course:

```text
Skills package methods.
Tools execute actions.
MCP connects tools.
RAG controls context.
Loops make revision accountable.
Harnesses operationalize research policy.
Annotations preserve reusable examples.
Fine-tuning internalizes behavior only when justified.
Platforms assemble the system.
```

---

## Relationship to the Introductory Course

The introductory course should be treated as a prerequisite.

It introduces:

- prompting as method
- externalized memory
- taxonomies and ontologies
- multi-turn interaction
- reasoning traces
- role-based agents
- reproducible workflows

The advanced course assumes students can already create:

- prompts
- session notes
- taxonomies
- reasoning traces
- basic role-based critiques

The advanced course then asks students to package, test, and operationalize those methods.

---

## Lesson 1 — Skills, Tools, MCP, and Python Helpers

### Purpose

Teach architectural literacy.

Students should distinguish:

```text
Skill = method package
Tool = executable action
MCP = connection protocol
Agent = coordinator over time
Python helper = repeatable validation or processing step
```

### Instructor Emphasis

Do not begin with MCP installation.

Begin with conceptual distinctions.

The first goal is for students to understand how a future humanities assistant might connect to:

- Zotero
- Obsidian
- local files
- PDFs
- GitHub
- transcription tools
- translation tools
- vector search

### Worked Example

Use the metaphor-analysis skill example.

It shows:

```text
SKILL.md = method
examples.md = teacher examples
rubric.md = evaluation criteria
output_schema.json = expected structure
check_output.py = executable checker
future MCP = way to expose checker as callable tool
```

### Student Success Indicators

Students can explain:

- what part of the example is the skill
- what part is the tool
- what MCP would add
- what an agent would coordinate
- what remains human judgment

### Common Failure Modes

- Students think MCP itself is the main topic.
- Students confuse a skill with a prompt.
- Students think Python replaces interpretation.
- Students treat tools as proof of methodological validity.

### Instructor Guidance

Keep repeating:

```text
The skill explains the humanities method.
The script performs a repeatable subtask.
The tool executes an action.
MCP exposes tools through a connector.
The agent coordinates them over time.
```

---

## Lesson 2 — RAG and Context Engineering

### Purpose

Teach students how retrieval actually works.

RAG should not be presented as a vague magic improvement.

Students must understand:

```text
where documents live
how passages are selected
what gets retrieved
what gets inserted into the prompt
what the LLM actually sees
how grounded answers are evaluated
```

### Instructor Emphasis

The most important sentence:

```text
RAG is not the answer.
RAG is the process of deciding what evidence the model is allowed to use.
```

### Pedagogical Levels

Teach three levels:

```text
Level 1:
Manual RAG

Level 2:
Keyword RAG with a local Python script

Level 3:
Conceptual vector RAG
```

MCP-connected RAG should be explained as an optional architecture:

```text
RAG = grounding method
MCP = connector to retrieval tools
```

### Student Success Indicators

Students can:

- identify the corpus folder
- manually select relevant passages
- run keyword retrieval
- build a context packet
- ask the LLM to answer using only retrieved context
- evaluate whether the answer used evidence correctly

### Common Failure Modes

- Students think RAG means “the model searches the internet.”
- Students do not know what documents were available.
- Students paste too much context without selection.
- Students fail to check whether the answer used retrieved evidence.
- Students confuse retrieved context with truth.

### Instructor Guidance

Make students inspect the corpus manually before running retrieval scripts.

They should see that retrieval is a research decision, not a purely technical step.

---

## Lesson 3 — Loop Patterns, Multi-Turn Reasoning, and Agent Orchestration

### Purpose

Teach students how reasoning traces become repeatable workflows.

The key distinction:

```text
CoT / ToT = reasoning patterns
multi-turn interaction = conversation over time
loop = repeated workflow with state and stopping criteria
agent = role or function inside the workflow
orchestration = control logic for who acts next and when to stop
```

### Instructor Emphasis

The most important sentence:

```text
A loop is not just “ask again.”
A loop has roles, state, inputs, outputs, evaluation, and termination criteria.
```

### Recommended Worked Example

Use:

```text
Analyst → Skeptic → Editor → Evaluator → Archivist
```

on the metaphor-analysis passage:

```text
The city was a broken mirror, reflecting every dream I had lost.
```

### What Students Should Learn

Students should understand that:

- the Analyst produces a candidate interpretation
- the Skeptic identifies weaknesses
- the Editor revises
- the Evaluator applies criteria
- the Archivist preserves state and provenance

### Termination Criteria

Teach that loops must stop.

Possible stopping rules:

- stop after N rounds
- stop when score reaches a threshold
- stop when no required revisions remain
- stop when the same critique repeats
- stop when human reviewer approves
- stop when ambiguity is documented rather than resolved

For humanities workflows:

```text
A loop does not always end by finding certainty.
Sometimes it ends by documenting unresolved ambiguity.
```

### Student Success Indicators

Students can:

- define loop state
- assign roles
- run one manual loop
- apply a stopping condition
- archive the workflow
- explain what improved and what remained unresolved

### Common Failure Modes

- Agents become theatrical roleplay.
- The loop produces more text but not better method.
- No stopping condition is defined.
- The Archivist summarizes vaguely.
- The Evaluator scores without a rubric.

### Instructor Guidance

Keep emphasizing:

```text
Agents are not characters.
Agents are functions in a workflow.
```

---

## Lesson 4 — Research Harnesses and Evaluation Harnesses

### Purpose

This is the conceptual peak of the advanced course.

Students learn that a harness is not only an evaluation table.

A humanities research harness is:

```text
a structured set of guides, resources, tools, checks, policies, and archives that makes an LLM-assisted research method operational, accountable, and reproducible
```

### Instructor Emphasis

The most important sentences:

```text
A loop improves one answer.
A harness operationalizes the environment in which improvement is allowed to happen.
```

and:

```text
An evaluation harness tests a method.
A research harness operationalizes a method.
```

### Engineering Analogy

It is useful to borrow the engineering idea of a harness as the system around the model, but translate it carefully.

For humanities:

```text
Model = interpretive engine
Harness = research environment around the model
```

The harness defines:

- allowed sources
- forbidden claims
- tools
- output schema
- checks
- rubric
- human review points
- archive rules

### Feedforward and Feedback

Use this distinction:

```text
Guides before action.
Sensors after action.
```

Feedforward guides include:

- research question
- corpus boundaries
- theory packet
- taxonomy
- skill instructions
- citation policy
- uncertainty policy
- output schema

Feedback sensors include:

- schema checker
- citation check
- evidence check
- ambiguity check
- overinterpretation check
- human rubric scoring
- LLM-assisted critique

### Student Success Indicators

Students can explain:

- what the harness allows
- what the harness forbids
- what sources are available
- what tools check
- what humans review
- how outputs are archived
- how the harness differs from a loop

### Common Failure Modes

- Students treat harness as just a scores table.
- Students define policies but do not operationalize them.
- Students automate checks that require human interpretation.
- Students confuse structural validity with interpretive validity.
- Students assume guardrails make outputs correct.

### Instructor Guidance

Use this phrase often:

```text
Tool validity is not interpretive validity.
```

A schema checker can detect missing fields. It cannot decide whether a metaphor interpretation is culturally or historically adequate.

---

## Lesson 5 — Annotation Assets and Model Adaptation

### Purpose

Teach students that annotations are reusable research assets.

Fine-tuning should be introduced, but not as the default endpoint.

The key question is:

```text
Should this method remain external as a skill, RAG workflow, loop, and research harness,
or is there enough reason and enough data to adapt a model?
```

### Instructor Emphasis

The most important sentence:

```text
Do not fine-tune a method that has not been tested.
```

Students should learn:

```text
Skills externalize method.
RAG externalizes knowledge.
Harnesses externalize policy and evaluation.
Fine-tuning internalizes behavior.
Distillation transfers behavior to a smaller model.
LoRA/adapters internalize behavior through lightweight trainable modules.
```

### Practical Position on Fine-Tuning

Fine-tuning is possible, but it is usually not required or practical as the main course task.

For most students, the practical task is to prepare a **model-adaptation dossier**, not to train a model.

The dossier includes:

- annotation schema
- annotations.jsonl
- few-shot prompt
- evaluation split
- fine-tuning-format JSONL
- model adaptation decision memo

### Student Success Indicators

Students can explain:

- how the same annotations support prompting, skills, RAG, evaluation, and fine-tuning
- why five examples are not enough for serious fine-tuning
- what behavior fine-tuning would internalize
- what should remain external
- what requires human review
- whether fine-tuning is justified

### Common Failure Modes

- Students think fine-tuning is automatically better.
- Students assume five examples are enough.
- Students want to train before evaluating.
- Students ignore copyright, provenance, and review status.
- Students confuse stable formatting with interpretive accuracy.

### Instructor Guidance

A strong student conclusion may be:

```text
Fine-tuning is not justified yet.
The method should remain external until we have more examples, better evaluation, and clearer failure analysis.
```

This is not a failure. It is a sophisticated methodological judgment.

---

## Lesson 6 — Capstone: Humanities Research Platform

### Purpose

Assemble the full advanced course into a reproducible humanities research platform.

The final platform should include:

- research question
- corpus manifest
- theory library
- skill
- RAG context packet
- loop trace
- research harness
- annotation assets
- model adaptation memo
- final interpretive report

### Instructor Emphasis

The final goal is not a polished app.

The final goal is a reproducible research environment.

The key sentence:

```text
The goal is to move from LLM assistant to humanities research platform.
```

### Capstone Architecture

Students should be able to show:

```text
Research question
→ corpus and theory library
→ skill
→ RAG/context engineering
→ loop/orchestration
→ research harness
→ annotation assets
→ model adaptation decision
→ final interpretive report
```

### Student Success Indicators

Students can explain:

- what method the platform packages
- what evidence the model can access
- what retrieval contributes
- what loop improves
- what the harness constrains
- what annotations preserve
- whether model adaptation is justified
- what remains human judgment

### Common Failure Modes

- Beautiful final answer but no method.
- Method files exist but are not used.
- RAG packet lacks source boundaries.
- Loop has no stopping condition.
- Harness has no real checks.
- Annotation dataset has no review status.
- Fine-tuning memo assumes training is automatically better.
- Final report hides ambiguity.

### Instructor Guidance

Grade the capstone by method quality, not only interpretive elegance.

A successful project is:

- explicit
- grounded
- reproducible
- self-critical
- ethically aware
- honest about limitations

---

## Suggested Pacing

### Six-week version

```text
Week 1:
Skills, tools, MCP, Python helper

Week 2:
RAG and context engineering

Week 3:
Loops and orchestration

Week 4:
Research harnesses

Week 5:
Annotation assets and model adaptation

Week 6:
Platform capstone presentations
```

### Twelve-week version

```text
Week 1:
Review introductory course concepts

Week 2:
Skills and tool architecture

Week 3:
MCP discovery and Python helper lab

Week 4:
Manual RAG

Week 5:
Keyword RAG and vector RAG concepts

Week 6:
Loop patterns and orchestration

Week 7:
Research harnesses

Week 8:
Evaluation, guardrails, and human review

Week 9:
Annotation assets

Week 10:
Fine-tuning, distillation, LoRA/adapters as decision pathways

Week 11:
Capstone workshop

Week 12:
Capstone presentations and reflection
```

---

## Assessment Strategy

The advanced course should be assessed through cumulative artifacts.

Recommended grading categories:

| Category | Weight |
|---|---:|
| Skill package and tool distinction | 15% |
| RAG/context packet | 15% |
| Loop trace and orchestration | 15% |
| Research harness | 20% |
| Annotation assets and adaptation memo | 15% |
| Final platform report and reflection | 20% |

The research harness receives high weight because it is the conceptual center of the advanced course.

---

## Student Learning Checkpoints

### After Lesson 1

Students can distinguish skill, tool, MCP, agent, and Python helper.

### After Lesson 2

Students can explain where documents live, how retrieval works, and what the LLM sees.

### After Lesson 3

Students can run a loop with roles, state, and a stopping condition.

### After Lesson 4

Students can define a research harness with guides, resources, tools, sensors, policies, and human review.

### After Lesson 5

Students can prepare annotation assets and justify whether fine-tuning is or is not appropriate.

### After Lesson 6

Students can present a complete humanities research platform.

---

## Student Success Indicators

Students are succeeding when they say things like:

```text
This answer is interesting, but it is not grounded in the retrieved context.

The schema check passed, but the interpretation still overreaches.

The loop should stop because the remaining ambiguity is documented.

Fine-tuning is not justified yet because our taxonomy is unstable.

The harness forbids claims outside the provided sources.

The annotation is useful for few-shot prompting, but not yet for training.
```

These statements show methodological maturity.

---

## Instructor Cautions

### Avoid feature accumulation

The course should not become:

```text
Now we learn tools.
Now we learn RAG.
Now we learn agents.
Now we learn fine-tuning.
```

Instead, every topic should answer:

```text
How does this make humanities interpretation more explicit, grounded, testable, or reviewable?
```

### Avoid premature automation

Students may want to automate too early.

Require manual versions first:

```text
manual skill
manual RAG
manual loop
manual harness review
manual annotation review
```

Then show where tools could help.

### Avoid treating fine-tuning as the goal

Fine-tuning is a model adaptation option, not the endpoint of the course.

The endpoint is a research platform.

### Avoid hiding uncertainty

Students should not optimize away ambiguity.

A good humanities system often preserves uncertainty rather than resolving it.

### Avoid confusing structure with truth

A JSON output can be structurally valid and interpretively weak.

A high score can still require human review.

A loop can improve style without improving evidence.

---

## Capstone Evaluation Rubric

| Criterion | Excellent | Developing | Needs Work |
|---|---|---|---|
| Research question | Clear, focused, humanities-relevant | Somewhat focused | Vague or too broad |
| Corpus | Documented and appropriate | Partially documented | Missing or unclear |
| Theory | Relevant and operationalized | Present but weakly connected | Missing or decorative |
| Skill | Reusable method package | Some reusable instructions | Only a prompt |
| RAG | Context is source-grounded | Context included but weak | No clear retrieval |
| Loop | Roles, state, and stopping condition clear | Loop present but vague | Just repeated prompting |
| Harness | Policies, checks, and review points explicit | Some checks present | No external harness |
| Annotations | Structured and reviewed | Present but inconsistent | Missing or unusable |
| Adaptation memo | Honest decision with justification | Mentions fine-tuning superficially | Assumes training is automatically better |
| Reflection | Clear limitations and next steps | Some reflection | Minimal reflection |

---

## Final Instructor Takeaway

The advanced course should train students not simply to use LLMs, but to design accountable research environments around them.

The desired final transformation is:

```text
from answer generation
to method design

from chat transcript
to research platform

from automation enthusiasm
to accountable human-AI scholarship
```
