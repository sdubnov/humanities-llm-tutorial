# Lesson 2 — Prompting and Structured Analysis

## Goal

Learn how to turn an open-ended interpretive question into a structured LLM task.

## Weak prompt

```text
Analyze this poem.
```

This is too open-ended.

## Stronger prompt

```text
Analyze this poem using the following categories:
metaphor, simile, repetition, imagery, speaker, tone, cultural reference.

For each category, quote evidence and explain your reasoning.
```

## Research prompt

```text
You are assisting with a humanities analysis project.

Task:
Analyze the text according to the taxonomy below.

Return your answer in this format:

1. passage
2. category
3. definition of category
4. evidence
5. interpretation
6. ambiguity or alternative reading
7. confidence score from 1–5
```

## Why structure matters

Structure helps the model produce comparable outputs across many texts.

This is the beginning of a method.
