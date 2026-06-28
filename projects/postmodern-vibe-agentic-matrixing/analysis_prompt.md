# Analysis Prompt Template

Use this template once per text and once per agent. Replace the placeholders before running the prompt.

```markdown
# Context

You are analyzing one entry from a small postmodern literature corpus.

Title: {{TITLE}}
Author: {{AUTHOR}}
Source note or description: {{DESCRIPTION_OR_EXCERPT}}

# Agent role

You are acting as:

{{AGENT_NAME}}

Your assigned metric is:

{{METRIC_NAME}}

Your role instruction is:

{{AGENT_SYSTEM_INSTRUCTION}}

# Task

Evaluate the text only through your assigned lens. Do not produce a general book summary.

## Part 1 — Vector score

Score the assigned metric from 1 to 10.

Return:

- Score:
- One-sentence justification:
- Evidence from the provided description or excerpt:

## Part 2 — Vibe synthesis

Write a 3-sentence qualitative critique of the text's vibe signature from your assigned perspective.

Avoid generic labels such as “absurdist,” “complex,” “postmodern,” or “experimental” unless you define exactly what they mean in this case.

## Part 3 — Reliability warning

Name one reason your score might be unreliable. For example: limited summary, canonical reputation, lack of full text, agent role too broad, or insufficient evidence.
```

## Instructor note

Students should save both the score and the reliability warning. The warning is not extra; it is part of the method.
