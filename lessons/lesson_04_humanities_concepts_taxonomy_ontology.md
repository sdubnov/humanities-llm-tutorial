# Lesson 4 — Humanities Concepts, Taxonomy, and Ontology

## Goal

Move from loose interpretation to explicit categories that can be applied consistently.

## Common humanities analysis concepts

A humanities analysis can examine many levels:

### Language and rhetoric

- metaphor: one domain understood through another
- simile: explicit comparison using like/as or similar phrasing
- metonymy: one associated thing stands for another
- synecdoche: part stands for whole, or whole for part
- irony: meaning conflicts with literal statement or expectation
- ambiguity: multiple plausible meanings
- pun: meaning depends on sound, double meaning, or wordplay
- repetition: recurrence of sound, word, phrase, image, or structure
- allusion: reference to another text, history, religion, culture, or event

### Narrative and structure

- speaker or persona
- addressee
- plot movement
- conflict
- transformation
- scene or setting
- voice
- temporality

### Cultural and social analysis

- identity markers
- gender roles
- class references
- race or ethnicity references
- place and geography
- political references
- cultural codes
- genre conventions

### Affect and tone

- anger
- grief
- pride
- intimacy
- irony
- vulnerability
- triumph
- threat

## Taxonomy vs ontology

A taxonomy is a classification list.

Example:

```text
Literary device
├── metaphor
├── simile
├── metonymy
└── irony
```

An ontology describes entities and relationships.

Example:

```text
metaphor has source_domain
metaphor has target_domain
speaker expresses affect
allusion refers_to cultural_object
```

## Mini example

Text:

```text
The city was a broken mirror, reflecting every dream I had lost.
```

Possible taxonomy entry:

```json
{
  "device": "metaphor",
  "source_domain": "broken mirror",
  "target_domain": "city",
  "affect": "loss, fragmentation",
  "evidence": "The city was a broken mirror",
  "confidence": 5,
  "alternative_reading": "The mirror may also suggest self-recognition rather than only urban decay."
}
```

## How to construct a taxonomy with an LLM

Prompt:

```text
Read the following theory excerpt. Extract the major analytical concepts. For each concept, give:
1. definition
2. inclusion criteria
3. exclusion criteria
4. example
5. common ambiguity
6. relationship to other concepts

Then organize the concepts into a taxonomy and an ontology.
```

## Lab 4

Choose one short theory text or article excerpt about poetry, rhetoric, metaphor, genre, or narrative.

Ask the LLM to produce:

```text
rules_methods/taxonomy_v1.md
rules_methods/ontology_v1.md
```

Then manually revise the result and mark anything that seems vague, excessive, or unsupported.

