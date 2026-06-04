# Advanced Lesson 2 — RAG for Humanities Research

## Goal

Understand retrieval-augmented generation as a transparent alternative to relying only on model memory.

## What is RAG?

```text
question
→ retrieve relevant documents
→ insert retrieved context
→ generate grounded answer
```

## Humanities RAG sources

- theory readings
- primary texts
- annotations
- session summaries
- taxonomy files
- translation notes
- historical context
- bibliography records

## Why RAG matters

RAG makes interpretation more inspectable because sources remain visible.

## Lab

Create a manual RAG simulation:

1. Select one short theory excerpt.
2. Select one short primary text.
3. Select one taxonomy or rule file.
4. Paste all three into the LLM.
5. Ask the model to analyze using only provided materials.
6. Save output and evaluate grounding.

## Evaluation criteria

- Did the model use retrieved material?
- Did it avoid unsupported claims?
- Did it cite or refer to evidence?
- Was the analysis better than a no-context prompt?
