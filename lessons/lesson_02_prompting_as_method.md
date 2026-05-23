# Lesson 2 — Prompting as Method

## Goal

Learn how a prompt becomes a research protocol.

## Casual prompt

```text
Analyze this poem.
```

This is easy but not reproducible.

## Structured prompt

```text
You are a humanities research assistant.
Analyze the text using the following steps:
1. Identify rhetorical or literary devices.
2. Quote exact evidence.
3. Explain the interpretation.
4. Give an alternative reading.
5. Rate confidence from 1 to 5.

Return the answer as a table.
```

This is better because it specifies roles, steps, evidence, uncertainty, and output format.

## Prompt as protocol

A research prompt should usually specify:

- role
- task
- definitions
- source text
- output format
- evidence requirement
- uncertainty handling
- what not to do

## Lab 2

Create:

```text
prompts/structured_analysis_prompt_v1.md
```

Use the template above and apply it to a short paragraph, poem, speech excerpt, or song lyric.

Save output as:

```text
outputs/structured_analysis_001.md
```

Then write a brief human evaluation:

```text
evaluations/evaluation_001.md
```

Answer:

- Did the model follow the prompt?
- Did it quote evidence?
- Did it over-interpret?
- What should be changed in the next prompt version?

