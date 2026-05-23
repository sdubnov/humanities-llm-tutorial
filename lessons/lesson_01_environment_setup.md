# Lesson 1 — Build the Research Environment

## Goal

Create a local folder that works like a lab notebook for LLM-assisted humanities analysis.

## Why not only chat?

A chat window is convenient, but it is weak for research because it is hard to track:

- which prompt produced which result
- what source text was used
- what rules were active
- what the human evaluator accepted or rejected
- how the method changed over time

The repository solves this by making prompts, rules, outputs, and evaluations visible as files.

## Step 1 — Open an editor

Recommended editors:

- Zed
- VS Code
- Cursor
- Any text editor that can open folders

Open the repository folder in the editor.

## Step 2 — Open a terminal

In Zed or VS Code, open the built-in terminal.

Typical menu names:

```text
Terminal → New Terminal
```

or:

```text
View → Terminal
```

## Step 3 — Run the setup script

From the repository root, run:

```bash
bash scripts/setup_project.sh my_first_llm_study
```

If bash is not available, use Python:

```bash
python scripts/setup_project.py my_first_llm_study
```

This creates:

```text
my_first_llm_study/
├── source_texts/
├── theory_texts/
├── prompts/
├── rules_methods/
├── session_notes/
├── outputs/
├── annotations/
├── evaluations/
├── examples/
└── figures/
```

## Step 4 — Open the hello-world prompt

Open:

```text
my_first_llm_study/prompts/hello_world_prompt.md
```

Copy it into ChatGPT, Claude, Gemini, or another LLM.

Save the result as:

```text
my_first_llm_study/outputs/output_001.md
```

## Lab 1

1. Run the setup script.
2. Copy the hello-world prompt into an LLM.
3. Save the output.
4. Fill in `session_notes/session_001.md`.

