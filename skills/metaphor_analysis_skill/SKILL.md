# Metaphor Analysis Skill

## Purpose

Use this skill to identify and analyze metaphorical language in humanities texts.

## Method

For each possible metaphor:

1. Quote exact evidence.
2. Identify source domain.
3. Identify target domain.
4. Explain the mapping.
5. Identify affect or tone.
6. Note ambiguity or alternative reading.
7. Assign confidence from 1–5.
8. Avoid unsupported cultural claims.

## Output format

Return a table with:

- passage
- device
- source domain
- target domain
- affect
- interpretation
- alternative reading
- confidence
- evidence note

## Failure modes

- confusing theme with metaphor
- overinterpreting vague imagery
- inventing cultural context
- ignoring ambiguity
- failing to quote evidence

## Optional tool use

Use `scripts/score_annotations.py` when comparing model output with human annotations.
