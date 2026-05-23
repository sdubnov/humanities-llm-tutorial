#!/usr/bin/env bash
set -e
PROJECT_NAME=${1:-my_llm_humanities_project}
mkdir -p "$PROJECT_NAME"/{source_texts,theory_texts,prompts,rules_methods,session_notes,outputs,annotations,evaluations,examples,figures}
cat > "$PROJECT_NAME/README.md" <<EOT
# $PROJECT_NAME

A small LLM-assisted humanities research project.

## Workflow

1. Put primary texts in source_texts/
2. Put theory readings in theory_texts/
3. Write prompts in prompts/
4. Store rules/taxonomies in rules_methods/
5. Save each session summary in session_notes/
6. Save model outputs in outputs/
7. Save human checks in evaluations/
EOT
cat > "$PROJECT_NAME/prompts/hello_world_prompt.md" <<'EOT'
You are helping with a humanities research project.
Analyze the short text below using three steps:
1. Identify one literary or rhetorical feature.
2. Quote the evidence.
3. Explain why the feature matters.

Text:
"The city was a broken mirror, reflecting every dream I had lost."
EOT
cat > "$PROJECT_NAME/session_notes/session_001.md" <<'EOT'
# Session 001

Date:
Model used:
Goal:
Prompt file:
Input text:
Output file:
Human evaluation:
What changed in the rules:
Next step:
EOT
cat > "$PROJECT_NAME/rules_methods/analysis_rules_v1.md" <<'EOT'
# Analysis Rules v1

Use evidence from the text.
Do not over-interpret without explaining uncertainty.
Distinguish observation from interpretation.
Give alternative readings when the passage is ambiguous.
EOT
echo "Created $PROJECT_NAME"
