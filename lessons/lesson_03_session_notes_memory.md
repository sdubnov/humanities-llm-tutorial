# Lesson 3 — Session Notes, Rules, and Memory

## Goal

Learn how to preserve LLM work across sessions.

## Important terms

### Context

The information currently visible to the LLM.

### Session

One continuous interaction with an LLM.

### Session notes

A short summary of what happened in a session.

### Rules file

A document that stores the current principles of analysis.

### Method file

A document that stores the step-by-step procedure.

### Compression

Summarizing a long conversation into a shorter reusable note.

### Restarting

Beginning a new session by loading the rules, method, and session summary.

## Recommended practice

At the end of each session, create a file like:

```text
session_notes/session_001.md
```

Include:

- date
- goal
- prompt used
- text analyzed
- important output
- problems noticed
- next steps

## Key idea

LLMs do not automatically preserve research continuity.

You preserve continuity through files.
