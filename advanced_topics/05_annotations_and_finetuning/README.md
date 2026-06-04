# Advanced Lesson 5 — Annotation Assets and Model Adaptation

## Goal

Understand how humanities annotations can become reusable research assets.

This lesson reframes fine-tuning as one possible use of annotation data, not the default goal.

The central question is:

```text
Should this method remain external as a skill, RAG workflow, loop, and research harness,
or is there enough reason and enough data to adapt a model?
```

---

## Why This Lesson Comes After Research Harnesses

The previous lessons built the external research method:

```text
Lesson 1:
skill, tools, MCP, Python helpers

Lesson 2:
RAG and context engineering

Lesson 3:
loops, agents, orchestration, termination

Lesson 4:
research harnesses: policy, resources, checks, evaluation, archive
```

Only now should students ask whether model adaptation is useful.

The important principle:

```text
Do not fine-tune a method that has not been tested.
```

Before model adaptation, students should have:

- a clear task
- an output schema
- examples
- a rubric
- a research policy
- a test set
- known failure modes
- human-reviewed annotations

---

## Core Distinctions

| Approach | What changes? | Best use |
|---|---|---|
| Prompting | instruction only | early exploration |
| Skill | external method package | reusable procedure |
| RAG | external knowledge/context | grounded answers |
| Loop | external revision process | improving one output |
| Research harness | external policy/testing environment | accountability and robustness |
| Fine-tuning | model behavior | repeated, stable behavior |
| Distillation | smaller model behavior | efficiency or deployment |
| LoRA / adapters | lightweight trainable modules | open-source technical track |

The key distinction:

```text
Skills externalize method.
RAG externalizes knowledge.
Harnesses externalize policy and evaluation.
Fine-tuning internalizes behavior.
Distillation transfers behavior to a smaller model.
LoRA/adapters internalize behavior through lightweight trainable modules.
```

---

## Is Fine-Tuning Practical?

Fine-tuning is possible, but it is usually not the first practical step for humanities students.

For this course, fine-tuning is treated as:

```text
a possible future use of high-quality annotation assets
```

not as a required implementation.

### Practical for this course

Students can practically create:

```text
annotation schema
human-reviewed examples
few-shot prompt examples
evaluation split
fine-tuning-format JSONL
model adaptation decision memo
```

### Optional advanced technical path

A computationally advanced group may later try:

```text
provider fine-tuning
open-source LoRA / QLoRA
adapter training
distillation into a smaller model
```

But that requires:

- enough examples
- compute or API access
- careful train/dev/test split
- evaluation harness
- documentation of data provenance
- attention to copyright and ethics

---

## What Counts as Enough Data?

Five examples are useful for teaching format.

Five examples are not enough for serious fine-tuning.

Suggested interpretation:

```text
5 examples:
demonstrate schema and few-shot prompting

20–50 examples:
small pilot annotation set

100–500 examples:
possible narrow fine-tuning experiment, depending on task

500+ examples:
more plausible fine-tuning dataset, still requiring evaluation
```

For humanities research, quality and consistency matter more than raw size.

A small, carefully reviewed dataset is better than a large inconsistent one.

---

## Annotation Assets

Students have already created many assets that can become annotation data:

```text
taxonomy
skill examples
RAG context packets
reasoning traces
loop outputs
skeptic critiques
research harness scores
human review notes
```

These can be repurposed as:

```text
few-shot examples
RAG examples
evaluation data
training data
distillation data
rubric calibration examples
```

---

## Annotation Example

```json
{
  "text_id": "city_mirror",
  "passage": "The city was a broken mirror, reflecting every dream I had lost.",
  "device": "metaphor",
  "evidence": "The city was a broken mirror",
  "source_domain": "broken mirror",
  "target_domain": "city",
  "affect": "loss, fragmentation",
  "interpretation": "The city is represented as damaged and reflective of lost hopes.",
  "alternative_reading": "The mirror may also suggest self-recognition or distorted memory.",
  "confidence": 4,
  "uncertainty_note": "The metaphor supports loss and fragmentation, but the balance between city, memory, and self-image remains uncertain.",
  "review_status": "human_reviewed"
}
```

---

## Same Annotation, Different Uses

The same annotation can be used in several ways.

### Few-shot prompting

Paste examples into a prompt to guide future outputs.

### Skill example

Place examples inside a skill package.

### RAG memory

Retrieve prior annotations as context.

### Evaluation harness

Use examples to calibrate scores or expected features.

### Fine-tuning

Format examples as input/output pairs.

### Distillation

Use teacher-model outputs plus human review to train a smaller model.

---

## Fine-Tuning Format

A fine-tuning dataset usually separates input from expected output.

Example:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You annotate metaphors in humanities texts using structured JSON."
    },
    {
      "role": "user",
      "content": "Annotate this passage: The city was a broken mirror, reflecting every dream I had lost."
    },
    {
      "role": "assistant",
      "content": "{\"text_id\":\"city_mirror\",\"passage\":\"The city was a broken mirror\",\"device\":\"metaphor\",\"evidence\":\"The city was a broken mirror\",\"source_domain\":\"broken mirror\",\"target_domain\":\"city\",\"affect\":\"loss, fragmentation\",\"interpretation\":\"The city is represented as damaged and reflective of lost hopes.\",\"alternative_reading\":\"The mirror may also suggest self-recognition.\",\"confidence\":4,\"uncertainty_note\":\"The metaphor supports loss and fragmentation, but the precise emphasis remains ambiguous.\"}"
    }
  ]
}
```

This format is useful pedagogically even if students do not actually fine-tune.

---

## Model Adaptation Decision Tree

Use this decision tree before fine-tuning.

```text
Is the task stable?
    no → keep using prompts, skills, and RAG
    yes ↓

Is the output format stable?
    no → improve schema and examples
    yes ↓

Do we have enough human-reviewed examples?
    no → build annotation dataset
    yes ↓

Does the method pass a research harness?
    no → revise method before training
    yes ↓

Does fine-tuning solve a real problem?
    no → keep method external
    yes ↓

Consider fine-tuning, LoRA/adapters, or distillation.
```

Fine-tuning may be justified if:

- outputs need consistent JSON
- the task repeats many times
- the model ignores the schema despite prompting
- the domain labels are stable
- evaluation shows the method is reliable
- cost or latency matters at scale

Fine-tuning may not be justified if:

- the taxonomy is still changing
- source grounding is the main problem
- citations are required
- the task depends on changing documents
- the corpus is small
- ambiguity is central
- human review remains essential

---

## Distillation

Distillation means using a stronger teacher model or expert process to help train a smaller or more efficient model.

Humanities framing:

```text
strong model + human review → high-quality annotations → smaller model or adapted model
```

Possible use:

```text
A large model helps generate candidate annotations.
A human corrects them.
The corrected examples become training data for a smaller model.
```

Risks:

- teacher-model bias
- loss of nuance
- over-standardization of interpretation
- hidden errors becoming training examples
- copyright and provenance issues

---

## LoRA and Adapters

LoRA and adapters are advanced technical methods for adapting open-source models without training all model parameters.

For this course, they are optional concepts.

Useful framing:

```text
Full fine-tuning:
update many model parameters

LoRA / adapters:
freeze most of the model and train small additional components
```

This can be useful for computational research groups, but it is not required for the humanities platform capstone.

---

## Lab 5 — Build a Model-Adaptation Dossier

Students do not need to train a model.

Instead, they prepare a dossier that could support future adaptation.

Use:

```text
model_adaptation_dossier/
```

### Part A — Define the schema

Complete:

```text
annotation_schema.json
```

### Part B — Create annotations

Create at least 10 annotations.

Save:

```text
annotations.jsonl
```

At least 3 should be human-reviewed.

### Part C — Create few-shot examples

Save:

```text
few_shot_prompt.md
```

### Part D — Create an evaluation split

Save:

```text
evaluation_split.jsonl
```

### Part E — Convert to fine-tuning format

Save:

```text
fine_tuning_format.jsonl
```

### Part F — Write a decision memo

Save:

```text
model_adaptation_decision.md
```

Answer:

1. What behavior would fine-tuning internalize?
2. What should remain external as a skill?
3. What should remain retrievable through RAG?
4. What should remain governed by the research harness?
5. What data is missing?
6. Is fine-tuning justified now?
7. Would distillation or LoRA make sense later?

---

## Deliverables

Submit:

```text
model_adaptation_dossier/annotation_schema.json
model_adaptation_dossier/annotations.jsonl
model_adaptation_dossier/few_shot_prompt.md
model_adaptation_dossier/evaluation_split.jsonl
model_adaptation_dossier/fine_tuning_format.jsonl
model_adaptation_dossier/model_adaptation_decision.md
```

---

## Final Takeaway

In humanities research, the first goal is not to change the model.

The first goal is to make the method:

```text
explicit
grounded
testable
reviewable
reproducible
ethically accountable
```

Only after that should we ask whether the behavior should be internalized into a model.
