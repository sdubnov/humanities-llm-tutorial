# Advanced MCP Section — Connecting a Tool

## Purpose

This section explains how a local script, such as `check_output.py`, could become a tool exposed to an AI assistant through MCP.

This section is optional.

The main course goal is conceptual literacy.

The advanced goal is to understand the connection architecture.

---

## MCP Architecture

```text
LLM application / MCP host
        ↓
MCP client
        ↓
MCP server
        ↓
local tool or data source
        ↓
result returned to model
```

In this architecture:

- the LLM application is the host environment
- the MCP client communicates with an MCP server
- the MCP server exposes tools or data sources
- the tool performs an action
- the result returns to the model

---

## Example: Exposing the Metaphor Checker

The local script:

```text
metaphor_analysis_skill_example/
└── scripts/
    └── check_output.py
```

could become an MCP tool:

```text
Tool name:
check_metaphor_annotation

Input:
JSON annotation

Action:
run validation

Output:
valid / missing fields
```

The skill still defines the interpretive method.

The script still performs the validation.

The MCP server exposes the script as a callable tool.

The LLM application can now call the checker during an agent workflow.

---

## Tool Schema Concept

A tool exposed through MCP needs a clear input/output description.

Conceptual schema:

```json
{
  "name": "check_metaphor_annotation",
  "description": "Check whether a metaphor annotation contains the required fields.",
  "input": {
    "annotation": {
      "type": "object",
      "description": "A metaphor annotation JSON object."
    }
  },
  "output": {
    "valid": "boolean",
    "missing_fields": "array"
  }
}
```

---

## Agent Workflow Example

An agent might:

1. produce a metaphor annotation
2. call the checker
3. receive missing fields
4. revise the annotation
5. call the checker again
6. save the final result

Workflow:

```text
LLM generates annotation
→ MCP tool checks annotation
→ tool returns missing fields
→ LLM revises annotation
→ tool checks again
→ output is accepted
```

Stopping condition:

```text
valid = true
```

---

## Optional Demo Plan

The instructor may show this sequence conceptually or implement it in a later technical workshop.

```text
Stage 1: Run Python manually.
Stage 2: Wrap Python in a simple command-line interface.
Stage 3: Describe the tool input/output schema.
Stage 4: Connect through an MCP server.
Stage 5: Let an agent call the tool in a loop.
```

---

## Why This Matters for Humanities

Even when the annotation is structurally valid, it may still be interpretively weak.

The tool can check structure.

The human must still judge:

- evidence quality
- cultural context
- interpretive plausibility
- ambiguity
- ethical sensitivity

This is the key distinction:

```text
Tool validity is not interpretive validity.
```

---

## MCP Safety Checklist

Before using an MCP server, ask:

1. What data does it access?
2. Can it modify files?
3. Can it run commands?
4. Does it send data outside the machine?
5. Does it require credentials?
6. Is the server maintained and trustworthy?
7. Could prompt injection cause unsafe tool use?
8. Is private or copyrighted material being exposed?

Practical rule:

```text
Do not connect private archives, student data, unpublished manuscripts, copyrighted PDFs, or personal notes to unknown MCP servers without review.
```
