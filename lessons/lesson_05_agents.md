# Lesson 5 — Multi-Agent Interpretive Workflows

## Goal

Understand how different LLM roles can support a more rigorous interpretive process.

## What is an agent?

An agent is an LLM assigned a role, task, and procedure.

In this tutorial, agents do not need to be fully automated.

They can simply be repeated prompt roles.

## Basic agents

### 1. Theorist Agent

Builds concepts, definitions, and taxonomies from scholarly sources.

### 2. Analyst Agent

Applies the taxonomy to a text.

### 3. Skeptic Agent

Checks for overinterpretation, weak evidence, or inconsistency.

### 4. Comparator Agent

Compares two texts, authors, genres, or groups.

### 5. Archivist Agent

Summarizes the session and updates the rule files.

## Example workflow

```text
source text
  ↓
Theorist builds taxonomy
  ↓
Analyst applies taxonomy
  ↓
Skeptic critiques analysis
  ↓
Analyst revises
  ↓
Archivist saves method and results
```

## Key idea

Multiple agents are useful because humanities interpretation often benefits from multiple perspectives.
