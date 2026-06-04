# Advanced Lesson 5 — Annotations and Fine-Tuning

## Goal

Understand how human annotations can become examples for in-context learning, evaluation, or fine-tuning.

## Annotation schema example

```json
{
  "text": "The city was a broken mirror.",
  "device": "metaphor",
  "evidence": "The city was a broken mirror",
  "source_domain": "broken mirror",
  "target_domain": "city",
  "affect": "loss, fragmentation",
  "alternative_reading": "self-recognition",
  "confidence": 4
}
```

## Uses of annotations

The same annotations can support:

- few-shot prompting
- in-context learning
- RAG examples
- evaluation harnesses
- supervised fine-tuning
- preference or rubric-based training

## Key distinction

```text
Skills externalize method.
Fine-tuning internalizes behavior.
```

## Lab

Create 5 teacher-approved annotations.

Convert them into:

1. a few-shot prompt
2. a JSONL-style training example
3. an evaluation item
