# Advanced Lesson 3 — Loop Patterns for Agentic Humanities Workflows

## Goal

Learn common loop patterns that allow an LLM or agent workflow to repeat until a stopping condition is met.

## Pattern 1 — Critique–Revision Loop

```text
Analyze → Critique → Revise → Repeat until acceptable
```

## Pattern 2 — Taxonomy Refinement Loop

```text
Build taxonomy → Apply taxonomy → Detect ambiguity → Revise taxonomy → Apply again
```

## Pattern 3 — ReAct Loop

```text
Reason → Act with tool → Observe result → Reason again
```

## Pattern 4 — Reflexion Loop

```text
Generate → Critique → Write lesson learned → Retry
```

Externalize the lesson into:

```text
session_notes/lessons_learned.md
```

## Pattern 5 — Tree-of-Thought Loop

```text
Generate multiple interpretations → evaluate each → select or synthesize
```

## Pattern 6 — Debate Loop

```text
Agent A: formal reading
Agent B: historical reading
Agent C: cultural reading
Judge: compares evidence
```

## Pattern 7 — Evaluator–Optimizer Loop

```text
Generate output → score with rubric → revise prompt/taxonomy → repeat until threshold
```

## Lab

Run a manual critique–revision loop:

1. Ask Analyst to analyze a text.
2. Ask Skeptic to score evidence and overinterpretation.
3. Ask Editor to revise.
4. Repeat once.
5. Save all steps.

## Evaluation criteria

- Did the loop improve the output?
- Did the stopping condition make sense?
- Was the critique specific?
- Were changes externalized into files?
