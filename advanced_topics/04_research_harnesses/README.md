# Advanced Lesson 4 — Research Harnesses and Evaluation Harnesses

## Goal

Learn how to build a research harness: an operational wrapper around an LLM-assisted humanities method.

This lesson broadens the idea of an **evaluation harness**.

An evaluation harness tests outputs.

A research harness operationalizes a method.

The key idea:

```text
A humanities research harness is not just an evaluation table.
It is the operational wrapper around an LLM-assisted method.
```

It turns research judgment into:

```text
guides
resources
tools
checks
permissions
policies
state
archives
human review points
```

---

## Why This Lesson Matters

Earlier lessons built the parts:

```text
Lesson 1:
skills, tools, MCP, Python helpers

Lesson 2:
RAG and context engineering

Lesson 3:
loops, roles, orchestration, and termination
```

This lesson asks:

```text
How do we wrap those parts into a reproducible research apparatus?
```

The answer is:

```text
a research harness
```

---

## Core Distinctions

| Concept | Purpose | Main question |
|---|---|---|
| Workflow | Produces an answer | What steps generate the result? |
| Loop | Improves one answer | How do we critique and revise? |
| Evaluation harness | Tests a method across cases | Does the method work reliably? |
| Research harness | Operationalizes a research method | What rules, resources, tools, checks, and archives make the method accountable? |

Short version:

```text
Workflow = produces an answer.
Loop = improves an answer.
Evaluation harness = tests a method.
Research harness = operationalizes the method.
```

---

## What Is a Research Harness?

A research harness is a structured environment around the model.

It defines:

```text
what evidence the model may use
what claims are allowed or disallowed
what tools may be called
what output structure is required
what counts as a failure
what must be checked
when to stop
when a human must review
what gets archived
```

For humanities research:

```text
Model = interpretive engine
Harness = research environment around the model
```

The harness does not make interpretation automatically correct.

Instead, it makes interpretation:

```text
constrained
grounded
comparable
revisable
auditable
reproducible
human-reviewable
```

---

## Engineering Analogy

In engineering discussions of agent harnesses, the harness is the system around the model.

It may provide:

```text
state
tools
environment
permissions
feedback
constraints
logs
tests
```

For humanities, we translate this carefully.

We are usually not verifying interpretation the way we verify code.

Instead, we are asking whether interpretation is:

```text
source-bounded
evidence-aware
ambiguity-preserving
methodologically consistent
culturally careful
auditable
```

So the analogy is useful, but only after translation.

---

## Feedforward Guides and Feedback Sensors

A useful way to think about a harness is:

```text
guides before action
sensors after action
```

### Feedforward Guides

Guides steer the model before it acts.

Examples:

```text
research question
corpus boundaries
allowed sources
theory packet
taxonomy
skill instructions
citation rules
uncertainty policy
forbidden claims
output schema
```

### Feedback Sensors

Sensors check the output after the model acts.

Examples:

```text
schema checker
citation check
evidence check
overinterpretation check
ambiguity check
cultural sensitivity review
rubric score
human review
LLM-assisted critique
```

The harness combines both.

```text
Guides constrain the method.
Sensors test whether the method was followed.
```

---

## Harness Components

| Harness component | Engineering analogy | Humanities version |
|---|---|---|
| Guides | system prompts, rules, docs | research question, theory, taxonomy, interpretive rules |
| Resources | repo, docs, APIs | corpus, theory library, annotations, bibliography |
| Tools | tests, linters, CLIs | retrieval, schema checker, citation checker, annotation scorer |
| State | task memory, files | session notes, loop state, revision history |
| Sensors | logs, tests, monitors | evidence rubric, ambiguity check, overinterpretation check |
| Guardrails | permissions, sandbox | source boundaries, privacy rules, no unsupported claims |
| Orchestration | agent loop | Analyst → Skeptic → Editor → Evaluator |
| Archive | traces and logs | reproducible research package |

---

## Evaluation Harness as One Part of a Research Harness

An evaluation harness is still important.

It tests whether a method works across multiple cases.

It contains:

```text
test inputs
fixed prompt or skill
expected features
outputs
scores
report
```

But in this lesson, evaluation is only one part of the larger research harness.

```text
Research harness = policy + resources + workflow + tools + evaluation + archive
```

---

## LLM-as-Judge: Use Carefully

A harness may include an LLM evaluator, but students should not rely on it blindly.

Use three levels of evaluation:

```text
Level 1: structural checks
Python checks whether required fields exist.

Level 2: human rubric scoring
Student or instructor scores evidence, ambiguity, and overinterpretation.

Level 3: LLM-assisted scoring
An LLM suggests scores, but a human reviews them.
```

Avoid the circular problem:

```text
LLM produces output.
Same LLM says output is good.
```

A good harness externalizes evaluation through files, rubrics, scripts, and human review.

---

## Worked Example: Metaphor Analysis Research Harness

The worked example tests and operationalizes the metaphor-analysis method from earlier lessons.

Research task:

```text
Annotate metaphors in short humanities texts while preserving evidence, ambiguity, and uncertainty.
```

The harness includes:

```text
research policy
allowed sources
corpus / test texts
guides
prompts
tools
outputs
scores
report
```

Use:

```text
harness_example/
```

---

## Example Harness Workflow

```text
1. Select a text from the test set.
2. Provide allowed context only.
3. Run the Analyst prompt.
4. Save the output as JSON.
5. Run the structural checker.
6. Run Skeptic or Evaluator prompt if needed.
7. Score the output with the rubric.
8. Record score in scores.csv.
9. Decide pass / revise.
10. Archive output and notes.
```

---

## What Makes This Different from Lesson 3?

Lesson 3 loop:

```text
The model improves one answer.
```

Lesson 4 harness:

```text
The researcher defines the environment in which improvement is allowed to happen.
```

The harness says:

```text
What sources are allowed?
What claims are forbidden?
What counts as evidence?
What checks must be passed?
What gets logged?
When must a human intervene?
```

---

## Lab 4 — Build a Mini Research Harness

### Part A — Define a research task

Example:

```text
Annotate metaphors in short passages.
```

### Part B — Define research policy

Use:

```text
templates/research_policy_template.md
```

### Part C — Define allowed sources

Use:

```text
templates/allowed_sources_template.md
```

### Part D — Define guides

Include at least:

```text
taxonomy
skill or method instructions
uncertainty policy
citation policy
```

### Part E — Define sensors

Include at least:

```text
schema check
human rubric
overinterpretation check
ambiguity check
```

### Part F — Run the harness

Use at least three test texts.

Save outputs in:

```text
outputs/
```

### Part G — Score and report

Fill:

```text
scores.csv
```

Write:

```text
harness_report.md
```

---

## Deliverables

Submit:

```text
research_policy.md
allowed_sources.md
guides/taxonomy.md
guides/uncertainty_policy.md
prompts/analyst_prompt.md
tools/check_output_structure.py
outputs/
scores.csv
harness_report.md
```

---

## Final Reflection Questions

1. What research behavior did the harness allow?
2. What research behavior did the harness forbid?
3. What resources did the model have access to?
4. What did the external tool check?
5. What did the rubric check that the tool could not?
6. Where was human review required?
7. Did the harness improve robustness?
8. Did the harness function as a guardrail?
9. What would need to change for another corpus or method?
10. What should remain outside automation?

---

## Final Takeaway

An evaluation harness helps test a method.

A research harness helps make a method operational.

For humanities research, a harness should make LLM-assisted work:

```text
grounded
constrained
comparable
auditable
reproducible
ethically reviewable
```
