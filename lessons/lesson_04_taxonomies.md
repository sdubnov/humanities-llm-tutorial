# Lesson 4 — Building Taxonomies from Theory Texts

## Goal

Use an LLM to help turn a scholarly article, book chapter, or theory text into an analytical taxonomy.

## What is a taxonomy?

A taxonomy is a structured list of categories.

For example:

- metaphor
- metonymy
- irony
- repetition
- voice
- genre marker
- cultural reference

## What is an ontology?

An ontology is a richer structure that explains relationships between concepts.

For example:

```text
metaphor
├── source domain
├── target domain
├── mapping
├── emotional tone
└── cultural frame
```

## Example prompt

```text
Read the theory text below.

Extract a taxonomy for analyzing literary or cultural texts.

For each concept, provide:

1. name
2. short definition
3. inclusion criteria
4. exclusion criteria
5. example
6. possible ambiguity
```

## Output

Save the result as:

```text
projects/project_name/taxonomy_v1.md
```

## Key idea

The LLM is not replacing theory.

It is helping translate theory into a usable research instrument.
