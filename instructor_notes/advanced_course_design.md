# Instructor Notes — Advanced Course Design

## Recommended integration with existing repo

Add this package into the existing `humanities-llm-tutorial` repository.

Do not create a separate repo yet.

Reason:

- the advanced module continues the same pedagogical arc
- students can see the transition from introductory methods to systems
- GitHub history remains unified

A separate repo can be created later if the advanced materials become a full independent course.

## Suggested GitHub structure

```text
advanced_topics/
skills/
advanced_projects/
instructor_notes/
```

## Pedagogical transition

Introductory course:

```text
prompting → files → taxonomies → multi-turn → role agents
```

Advanced course:

```text
skills → tools → RAG → loops → harnesses → fine-tuning → platform
```

## Core distinction

Skills package methods.
Tools execute actions.
MCP connects tools.
Agents coordinate skills and tools over time.
Fine-tuning internalizes behavior.
