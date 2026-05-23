# Lesson 3 — Sessions, CLI Tools, Memory, and Commands

## Goal

Understand how LLM work changes when you move from browser chat to command-line or editor-based assistants.

## Browser chat

In browser chat, the main unit is the conversation. The model sees the current conversation context, including recent messages, uploaded files, and sometimes saved memory depending on the product.

Good for:

- brainstorming
- reading a document
- explanation
- early prompt development

Weak for:

- repeatability
- file editing
- version control
- exact experiment tracking

## CLI or editor agent

A CLI agent runs in a terminal and can often see the local project folder. Examples include OpenAI Codex CLI, Claude Code, and Gemini CLI. Codex is described as a local coding agent; Claude Code is an agentic coding tool that can understand a codebase, edit files, and run commands; Gemini CLI is an open-source terminal agent that uses a reason-and-act loop with tools.

Important: each CLI has its own command style. Do not assume that `/commands` are universal.

## Common command patterns

Different systems may include:

- slash commands such as `/help`, `/model`, `/clear`, `/init`, or `/compact`
- project instruction files such as `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`
- session reset or context clearing commands
- model selection commands
- approval modes for file editing or terminal commands
- tool permissions

These are not general LLM laws. They are interface conventions of specific tools.

## Memory and context

LLMs do not literally remember everything forever. They operate through some combination of:

- current context window
- uploaded files
- retrieved documents
- saved user memory, if enabled
- project instruction files
- session summaries
- external databases or repositories

For research, assume that memory must be externalized into files.

## Compression

Compression means summarizing an older session into a shorter file that can be reused later.

Example:

```text
session_notes/session_003_summary.md
```

This file should include:

- goal
- model used
- source text
- active rules
- important findings
- unresolved problems
- next prompt

## Lab 3

Create a session summary from one previous LLM interaction.

Save it as:

```text
session_notes/session_002_summary.md
```

Then start a new browser chat and paste only that summary plus a new task. Observe what carries over and what is lost.

