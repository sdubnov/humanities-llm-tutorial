# Humanities LLM Research Tutorial

A short, low-code tutorial for using Large Language Models in humanities and qualitative research.

The course moves from casual chat to reproducible research workflows:

```text
chatting → prompting → files → rules → taxonomies → multi-turn analysis → agents
```

## Recommended path

1. Lesson 0 — First contact with LLMs
2. Lesson 1 — Build the research environment
3. Lesson 2 — Prompting as method
4. Lesson 3 — Sessions, CLI tools, memory, and command styles
5. Lesson 4 — Humanities concepts, taxonomy, and ontology
6. Lesson 5 — Multi-turn interaction and in-context learning
7. Lesson 6 — Agent roles for interpretive analysis
8. Final project — Build a small reproducible analysis study

## Quick start

Open this folder in Zed or VS Code. Then run one of the setup scripts:

```bash
bash scripts/setup_project.sh my_first_llm_study
```

or:

```bash
python scripts/setup_project.py my_first_llm_study
```

This creates a working research folder with prompts, source texts, session notes, rules, outputs, and evaluations.

## Philosophy

The goal is not to replace interpretation with automation. The goal is to make humanistic interpretation more explicit, reusable, inspectable, and reproducible.
