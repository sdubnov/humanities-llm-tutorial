# Curriculum Integration: Postmodern Vibe Agentic Matrixing

## Why this belongs in `projects/`

This project belongs in:

```text
projects/postmodern-vibe-agentic-matrixing/
```

The project synthesizes introductory-course methods rather than requiring the advanced-course stack. It practices structured prompting, saved artifacts, taxonomies, multi-turn refinement, role-based agents, qualitative coding, and lightweight Python reporting.

It does **not yet require** advanced-course infrastructure such as skills, tools, MCP, RAG, agent loops at scale, evaluation harnesses, annotation datasets, fine-tuning, or a research platform.

## Relationship to the introductory course

| Basic course lesson | What students practice in this project |
|---|---|
| Lesson 1 — Environment Setup | Maintaining prompts, configs, CSV files, reports, and rubrics as research artifacts. |
| Lesson 2 — Prompting as Method | Converting an interpretive question into a structured, reusable analytical prompt. |
| Lesson 3 — Sessions, CLI, Memory, and Commands | Optional use of a local script and saved artifacts to support restartability. |
| Lesson 4 — Humanities Concepts, Taxonomy, Ontology | Translating concepts such as ontology, paranoia, affect, pastiche, and media friction into analytical dimensions. |
| Lesson 5 — Multi-Turn Interaction and In-Context Learning | Revising agent outputs, using examples, and comparing results across iterations. |
| Lesson 6 — Agent Roles for Interpretive Analysis | Splitting interpretation across specialized analytical roles instead of asking for one generic answer. |

## Relationship to the advanced course

This project can be used as a **bridge** to advanced topics but should not be presented as a full advanced project.

| Advanced topic | Current project status | Possible advanced extension |
|---|---|---|
| Skills / Tools / MCP | Not required. | Package the workflow as a reusable skill with a `SKILL.md`. |
| RAG for Humanities | Not required. | Retrieve textual passages or scholarly context rather than using summaries. |
| Loop Patterns | Lightly introduced through manual repetition. | Automate loops across texts, agents, and prompt variants. |
| Evaluation Harnesses | Only informal critique. | Compare outputs to human annotations and track agreement. |
| Annotations / Fine-Tuning | Not included. | Build a small labeled dataset of human vibe judgments. |
| Research Platform | Not included. | Create a pipeline with corpus, retrieval, prompts, outputs, evaluation, and reports. |

## Recommended teaching sequence

```text
Introductory Lessons 1–6
        ↓
projects/postmodern-vibe-agentic-matrixing/
        ↓
advanced_topics/01–06
        ↓
advanced_projects/postmodern-vibe-research-harness/
```

## Pedagogical value

The project helps students understand that an LLM analysis is not a single answer. It is an apparatus composed of prompts, roles, corpus choices, scoring decisions, and interpretive review.

The key lesson is methodological transparency: the matrix should expose assumptions rather than hide them.
