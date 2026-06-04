# Advanced Lesson 1 — Skills, Tools, MCP, and Plugins

## Goal

Understand the difference between skills, tools, workflows, agents, and MCP servers.

## Key terms

- **Prompt:** a one-time instruction.
- **Template:** a reusable prompt pattern.
- **Skill:** a reusable method package containing instructions, examples, rubrics, schemas, scripts, or templates.
- **Tool:** an executable capability outside plain language generation, such as reading a PDF, running Python, querying Zotero, transcribing audio, or searching files.
- **MCP server:** a standardized way to expose tools to LLM applications.
- **Workflow:** an ordered process using skills and tools.
- **Agent:** an LLM system that coordinates steps, tools, memory, and stopping conditions over time.

## Humanities skill example

```text
metaphor_analysis_skill/
├── SKILL.md
├── examples.md
├── rubric.md
├── output_schema.json
├── failure_modes.md
└── scripts/
    └── score_annotations.py
```

## Lab

Design a humanities skill folder for one of the following:

- metaphor analysis
- translation comparison
- cultural reference detection
- close reading
- discourse analysis
- voice annotation

Create:

```text
SKILL.md
examples.md
rubric.md
output_schema.json
failure_modes.md
```

## Evaluation criteria

- Is the method clearly described?
- Are examples specific enough?
- Is the output schema usable?
- Does the rubric identify failure modes?
- Could another student reuse the skill?
