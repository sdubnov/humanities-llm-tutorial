# Lesson 6 — Agent Roles for Interpretive Analysis

## Goal

Understand agents as roles in a research workflow, even before using technical agent frameworks.

## Agent as role

An agent does not have to be a complicated software system. At the beginning, an agent can simply be a stable role prompt.

## Recommended roles

### Theorist

Extracts concepts from scholarly sources and proposes taxonomies.

### Analyst

Applies the taxonomy to primary texts.

### Skeptic

Checks for over-interpretation, missing evidence, and unclear categories.

### Comparativist

Compares authors, genres, periods, groups, or cultural contexts.

### Archivist

Summarizes sessions and updates files.

## Example role prompt

```text
You are the Skeptic agent.
Your job is not to produce a new interpretation.
Your job is to test whether the previous analysis is supported by textual evidence.
Check:
1. Is the quoted evidence sufficient?
2. Are categories applied consistently?
3. Are there alternative readings?
4. Is any cultural claim unsupported?
Return corrections only.
```

## Lab 6

Run one text through three roles:

1. Analyst
2. Skeptic
3. Archivist

Save each output separately:

```text
outputs/analyst_output_001.md
outputs/skeptic_output_001.md
session_notes/archivist_summary_001.md
```

