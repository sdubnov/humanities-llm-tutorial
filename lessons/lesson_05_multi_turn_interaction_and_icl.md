# Lesson 5 — Multi-Turn Interaction and In-Context Learning

## Goal

Use repeated interaction with the LLM as a controlled research process.

## Why multi-turn matters

A single prompt can produce an analysis. A multi-turn session can develop a method.

In multi-turn research, the model can:

- propose categories
- apply them
- receive critique
- revise the categories
- test them on another example
- compare outputs
- summarize the revised method

Recent research on multi-turn LLM interaction treats extended interaction, memory, planning, evaluation, and tool use as central problems for practical LLM systems.

## In-context learning

In-context learning means the model adapts to examples placed in the prompt or conversation without changing its weights.

Example:

```text
Example 1:
Text: "My heart is a locked room."
Analysis: metaphor; source domain = locked room; target domain = emotional self; affect = guardedness.

Example 2:
Text: "She moves like rain on glass."
Analysis: simile; source domain = rain on glass; target domain = movement; affect = softness/fluidity.

Now analyze:
Text: "The city was a broken mirror."
```

The examples teach the model the local style of analysis.

## Multi-turn protocol

Use this sequence:

1. Build initial taxonomy.
2. Apply taxonomy to a short text.
3. Human critiques the output.
4. LLM revises taxonomy.
5. Apply revised taxonomy to a new text.
6. Compare version 1 and version 2.
7. Save final rules and session summary.

## Reflexive prompt

```text
Review your previous analysis. Identify three possible errors:
1. unsupported interpretation
2. missing textual evidence
3. unclear category boundary

Then revise the analysis using stricter evidence.
```

## Lab 5

Run a three-turn experiment:

Turn 1:
Ask the LLM to analyze a text using your taxonomy.

Turn 2:
Give a human critique.

Turn 3:
Ask the LLM to revise both the analysis and the taxonomy.

Save:

```text
outputs/multiturn_output_001.md
evaluations/human_critique_001.md
rules_methods/taxonomy_v2.md
session_notes/multiturn_session_001.md
```

