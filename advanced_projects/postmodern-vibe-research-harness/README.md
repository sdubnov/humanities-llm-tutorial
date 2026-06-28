# Advanced Project Plan: Postmodern Vibe Research Harness

> Status: planning document only. This is not yet a complete advanced project package.

## Proposed path

```text
advanced_projects/postmodern-vibe-research-harness/
```

## Why this is separate from the introductory project

The introductory project `projects/postmodern-vibe-agentic-matrixing/` teaches role-based prompting, theory-to-taxonomy translation, matrix construction, and critique.

This advanced project would rebuild that case study using the advanced-course stack:

```text
skills → tools → RAG → loops → harnesses → annotations/fine-tuning → research platform
```

## Advanced learning goals

Students would learn to:

- package an interpretive method as a reusable skill;
- retrieve textual evidence with a RAG workflow instead of relying on summaries;
- automate repeated analysis across texts, agents, and prompt variants;
- construct an evaluation harness comparing LLM scores to human annotations;
- track disagreement, uncertainty, and model drift;
- design a miniature humanities research platform with corpus, retrieval, prompts, outputs, evaluations, and reports.

## Relationship to `advanced_topics`

| Advanced topic | Implementation in this project |
|---|---|
| `01_skills_tools_mcp` | Create a reusable `SKILL.md` for postmodern vibe analysis and expose workflow steps as repeatable actions. |
| `02_rag_for_humanities` | Retrieve passages from public-domain or instructor-provided texts, criticism, or excerpts before scoring. |
| `03_loop_patterns` | Run loops across corpus items, agents, prompt variants, and repeated trials. |
| `04_research_harnesses` | Compare model-generated scores with human/instructor benchmark annotations. |
| `05_annotations_and_finetuning` | Create a small labeled dataset of human vibe judgments; discuss whether fine-tuning is appropriate. |
| `06_humanities_research_platform` | Integrate corpus, retrieval, agents, scoring, evaluation, and reports into a coherent mini-platform. |

## Proposed files for the future implementation

```text
advanced_projects/postmodern-vibe-research-harness/
├── README.md
├── SKILL.md
├── corpus/
│   ├── passages.csv
│   └── source_notes.md
├── prompts/
│   ├── agent_roles.json
│   ├── retrieval_prompt.md
│   └── scoring_prompt.md
├── harness/
│   ├── run_harness.py
│   ├── evaluate_agreement.py
│   └── schema.py
├── annotations/
│   ├── human_benchmark_template.csv
│   └── annotation_guidelines.md
├── outputs/
│   └── example_report.md
└── instructor_notes.md
```

## Proposed development stages

### Stage 1 — Convert the method into a skill

Write a `SKILL.md` that defines the procedure, inputs, expected outputs, and failure modes.

### Stage 2 — Add retrieval

Replace book summaries with retrieved or instructor-provided passages. The key methodological goal is to reduce summary bias and reputation bias.

### Stage 3 — Add loop automation

Run all agents across all texts and prompt variants. Store each run with metadata.

### Stage 4 — Add evaluation

Have humans annotate a small benchmark set. Compare model outputs with human annotations. Track agreement, disagreement, and recurring failure patterns.

### Stage 5 — Platform reflection

Students write a research-platform design memo explaining what would be needed for a serious digital humanities system.

## Prerequisites

Students should complete the introductory project first, then the advanced topics through at least:

- Skills / Tools / MCP;
- RAG for Humanities;
- Loop Patterns;
- Evaluation Harnesses.

Annotations and fine-tuning are optional extensions.
