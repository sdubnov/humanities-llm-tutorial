# Advanced Course References and Bibliography

## Purpose

This bibliography supports the advanced sequence:

```text
Skills / Tools / MCP
→ RAG and Context Engineering
→ Multi-Turn Loops and Agent Orchestration
→ Research Harnesses
→ Annotation Assets and Model Adaptation
→ Humanities Research Platforms
```

It combines academic papers, official documentation, engineering guides, software tools, and digital-humanities resources.

---

# 1. Skills, MCP, and Tool Ecosystems

## OpenAI Codex Skills

OpenAI. **Agent Skills — Codex.**  
https://developers.openai.com/codex/skills

Course use: Lesson 1. Use this to explain skills as reusable method packages that may include `SKILL.md`, references, resources, and optional scripts.

## Anthropic MCP Introduction

Anthropic. **Introducing the Model Context Protocol.** 2024.  
https://www.anthropic.com/news/model-context-protocol

Course use: Lesson 1. Introduces MCP as a connector standard between AI applications, tools, and data sources.

## MCP Official Documentation

Model Context Protocol. **Introduction.**  
https://modelcontextprotocol.io/introduction

Course use: Lesson 1. General reference for what MCP is and how the architecture is described.

## MCP Registry

Model Context Protocol. **MCP Registry.**  
https://registry.modelcontextprotocol.io

Registry documentation:  
https://modelcontextprotocol.io/registry/about

GitHub repository:  
https://github.com/modelcontextprotocol/registry

Course use: Lesson 1. Use for MCP discovery activity.

## Awesome MCP Servers

Punkpeye. **Awesome MCP Servers.**  
https://github.com/punkpeye/awesome-mcp-servers

Course use: Lesson 1. Useful for browsing possible servers and tool categories.

## MCP.so

**MCP.so.**  
https://mcp.so

Course use: Lesson 1. MCP discovery directory.

## Composio Toolkits

Composio. **Toolkits.**  
https://composio.dev/toolkits

Course use: Lesson 1. Examples of toolkits and app integrations.

## MCP Security and Maintainability

Hasan, Mohammed Mehedi, Hao Li, Emad Fallahzadeh, Bram Adams, and Ahmed E. Hassan. **Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers.** arXiv, 2025.  
https://arxiv.org/abs/2506.13538

Li, Xiaofan, and Xing Gao. **Toward Understanding Security Issues in the Model Context Protocol Ecosystem.** arXiv, 2025.  
https://arxiv.org/abs/2510.16558

Course use: Lesson 1 safety discussion. Use to motivate privacy, credentials, prompt injection, unsafe tool access, and maintenance concerns.

---

# 2. Agent Design and Orchestration

## LangGraph Overview

LangChain. **LangGraph Overview.**  
https://docs.langchain.com/oss/python/langgraph/overview

Course use: Lesson 3. Optional technical reference for graph-based agent workflows.

## LangGraph Workflows vs Agents

LangChain. **Workflows and Agents.**  
https://docs.langchain.com/oss/python/langgraph/workflows-agents

Course use: Lesson 3. Supports the distinction between fixed workflows and dynamic agents.

## LangChain Overview

LangChain. **LangChain Python Documentation.**  
https://python.langchain.com

Course use: Advanced optional reference for students who want to implement chains, agents, and retrievers.

---

# 3. Multi-Turn Interaction and Agent Reasoning

## NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models

Workshop site:  
https://workshop-multi-turn-interaction.github.io/

OpenReview venue:  
https://openreview.net/group?id=NeurIPS.cc/2025/Workshop/MTI-LLM

SlidesLive video collection:  
https://slideslive.com/neurips-2025/workshop-workshop-on-multiturn-interactions-in-large-language-models

Course use: Lesson 3. Current research anchor for multi-turn interaction, memory, task progress, and evaluation.

## Multi-Turn Survey

Li, Yubo, Xiaobin Shen, Xinyu Yao, Xueying Ding, Yidi Miao, Ramayya Krishnan, and Rema Padman. **Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models.** arXiv, 2025.  
https://arxiv.org/abs/2504.04717

Course use: Lesson 3. Background survey for multi-turn evaluation and enhancement methods.

## Chain-of-Thought

Wei, Jason, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.** arXiv, 2022.  
https://arxiv.org/abs/2201.11903

Course use: Introductory reasoning-traces lesson. Translate CoT into visible evidence-to-claim reasoning.

## Self-Consistency

Wang, Xuezhi, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. **Self-Consistency Improves Chain of Thought Reasoning in Language Models.** arXiv, 2022.  
https://arxiv.org/abs/2203.11171

Course use: Lesson 3. Use carefully: convergence across samples may reveal stability, but does not prove interpretive truth.

## Tree of Thoughts

Yao, Shunyu, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik Narasimhan. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models.** arXiv, 2023.  
https://arxiv.org/abs/2305.10601

Code repository:  
https://github.com/princeton-nlp/tree-of-thought-llm

Course use: Lesson 3. Translate into competing interpretive branches.

## ReAct

Yao, Shunyu, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. **ReAct: Synergizing Reasoning and Acting in Language Models.** arXiv, 2022.  
https://arxiv.org/abs/2210.03629

Google Research blog:  
https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/

Code repository:  
https://github.com/ysymyth/ReAct

Course use: Lesson 3. Reason → act → observe → reason. For humanities, “act” often means retrieve, inspect, cite, or check.

## Reflexion

Shinn, Noah, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. **Reflexion: Language Agents with Verbal Reinforcement Learning.** arXiv, 2023.  
https://arxiv.org/abs/2303.11366

OpenReview:  
https://openreview.net/forum?id=vAElhFcKW6

Code repository:  
https://github.com/noahshinn/reflexion

Course use: Lesson 3. Useful for externalized lessons learned and retry loops.

---

# 4. RAG and Retrieval

## Original RAG Paper

Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.** arXiv, 2020.  
https://arxiv.org/abs/2005.11401

Course use: Lesson 2. Foundational RAG paper.

## LlamaIndex

LlamaIndex documentation:  
https://docs.llamaindex.ai

LlamaIndex RAG introduction:  
https://developers.llamaindex.ai/python/framework/understanding/rag/

Course use: Lesson 2. Practical framework for loading, indexing, retrieving, and querying documents.

## LangChain RAG Concepts and Retrievers

LangChain RAG concepts:  
https://python.langchain.com/docs/concepts/rag/

LangChain retriever integrations:  
https://docs.langchain.com/oss/python/integrations/retrievers

Course use: Lesson 2. Useful for explaining retrievers.

## Blended / Hybrid RAG

Sawarkar, Kunal, Abhilasha Mangal, and Shivam Raj Solanki. **Blended RAG: Improving RAG Accuracy with Semantic Search and Hybrid Query-Based Retrievers.** arXiv, 2024.  
https://arxiv.org/abs/2404.07220

Course use: Optional Lesson 2 extension on hybrid retrieval.

## Vector Databases

Chroma:  
https://www.trychroma.com

Qdrant:  
https://qdrant.tech

Weaviate:  
https://weaviate.io

Course use: Lesson 2. Optional infrastructure references for vector retrieval.

---

# 5. Evaluation and Research Harnesses

## OpenAI Evals

OpenAI. **Evals.**  
https://platform.openai.com/docs/guides/evals

Course use: Lesson 4. Reference for systematic evaluation.

## Promptfoo

Promptfoo:  
https://www.promptfoo.dev

GitHub:  
https://github.com/promptfoo/promptfoo

Course use: Lesson 4. Practical prompt/model comparison and red-teaming tool.

## HELM

Stanford CRFM. **Holistic Evaluation of Language Models.**  
https://crfm.stanford.edu/helm

Course use: Lesson 4. Evaluation as broad, transparent, multi-metric comparison.

## LLM-as-a-Judge Survey

Gu, Jiawei, et al. **A Survey on LLM-as-a-Judge.** arXiv, 2024.  
https://arxiv.org/abs/2411.15594

Project page:  
https://llm-as-a-judge.github.io/

Course use: Lesson 4. Helps discuss strengths and risks of LLM-assisted evaluation.

## Evidently AI: LLM-as-a-Judge Guide

Evidently AI. **LLM-as-a-Judge: A Complete Guide to Using LLMs for Evaluations.**  
https://www.evidentlyai.com/llm-guide/llm-as-a-judge

Course use: Practical evaluation guide.

## LangChain: The Anatomy of an Agent Harness

Trivedy, Vivek. **The Anatomy of an Agent Harness.** LangChain Blog, 2026.  
https://www.langchain.com/blog/the-anatomy-of-an-agent-harness

Course use: Lesson 4. Use for “Agent = Model + Harness.”

## Martin Fowler: Harness Engineering

Fowler, Martin. **Harness Engineering for Coding Agent Users.** 2026.  
https://martinfowler.com/articles/harness-engineering.html

Fowler, Martin. **Harness Engineering — First Thoughts.**  
https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html

Course use: Lesson 4. Use for guides/sensors: feedforward and feedback controls.

## Harness Engineering.ai

Harness Engineering. **The Complete Guide to Agent Harness: What It Is and Why It Matters.** 2026.  
https://harness-engineering.ai/blog/agent-harness-complete-guide/

Harness Engineering. **What Is Harness Engineering? The Discipline That Makes AI Agents Reliable.** 2026.  
https://harness-engineering.ai/blog/what-is-harness-engineering/

Course use: Practitioner-oriented reading on harness as environment around agents.

## LangChain Harness Capabilities

LangChain. **Harness Capabilities.**  
https://docs.langchain.com/oss/python/deepagents/harness

Course use: Optional implementation reference.

---

# 6. Fine-Tuning, Distillation, LoRA, QLoRA, and Model Adaptation

## OpenAI Model Optimization

OpenAI. **Model Optimization.**  
https://developers.openai.com/api/docs/guides/model-optimization

Course use: Lesson 5. Model improvement as evals, prompting, fine-tuning, and iterative optimization.

## OpenAI Fine-Tuning

OpenAI. **Fine-Tuning / Supervised Fine-Tuning.**  
https://platform.openai.com/docs/guides/fine-tuning

OpenAI Developer Docs:  
https://developers.openai.com/api/docs/guides/supervised-fine-tuning

Course use: Lesson 5. Practical provider-side fine-tuning.

## OpenAI Reinforcement Fine-Tuning

OpenAI. **Reinforcement Fine-Tuning.**  
https://platform.openai.com/docs/guides/reinforcement-fine-tuning

Developer docs:  
https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning

Course use: Optional Lesson 5 extension.

## LoRA

Hu, Edward J., Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. **LoRA: Low-Rank Adaptation of Large Language Models.** arXiv, 2021.  
https://arxiv.org/abs/2106.09685

Course use: Lesson 5. Parameter-efficient model adaptation.

## QLoRA

Dettmers, Tim, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. **QLoRA: Efficient Finetuning of Quantized LLMs.** arXiv, 2023.  
https://arxiv.org/abs/2305.14314

Course use: Optional technical extension for computational students.

## Hugging Face PEFT and LoRA

Hugging Face. **PEFT.**  
https://huggingface.co/docs/peft/en/index

Hugging Face. **LoRA Conceptual Guide.**  
https://huggingface.co/docs/peft/main/en/conceptual_guides/lora

Course use: Optional technical path for open-source adaptation.

---

# 7. Humanities-Oriented Infrastructure

## Zotero

Zotero:  
https://www.zotero.org

Course use: Bibliography management, literature review, research libraries.

## Zotero MCP

Zotero MCP by 54yyyu:  
https://github.com/54yyyu/zotero-mcp

MCP Zotero by nealcaren:  
https://github.com/nealcaren/mcp-zotero

Course use: Lesson 1 examples of humanities-relevant MCP connectors.

## Obsidian

Obsidian:  
https://obsidian.md

Course use: Markdown-based research notes and personal knowledge bases.

## Obsidian MCP

Piotr1215 MCP Obsidian:  
https://github.com/Piotr1215/mcp-obsidian

Course use: Lesson 1 MCP example for note vaults.

## GitHub

GitHub:  
https://github.com

Course use: Version control, reproducible course projects, collaborative artifacts.

---

# 8. Annotation Platforms

## INCEpTION

INCEpTION:  
https://inception-project.github.io

Course use: Humanities and linguistic annotation.

## Doccano

Doccano:  
https://github.com/doccano/doccano

Course use: Text annotation and classification datasets.

## Label Studio

Label Studio:  
https://labelstud.io

Course use: General annotation workflows.

## CATMA

CATMA:  
https://catma.de

Course use: Literary annotation and text analysis.

## Recogito

Recogito:  
https://recogito.pelagios.org

Course use: Historical, geographic, and textual annotation.

---

# 9. Speech, Voice, and Audio Annotation

## Whisper

OpenAI Whisper:  
https://github.com/openai/whisper

Course use: Speech-to-text and oral history transcription.

## Praat

Praat:  
https://www.fon.hum.uva.nl/praat

Course use: Phonetics, prosody, speech analysis.

## ELAN

ELAN:  
https://archive.mpi.nl/tla/elan

Course use: Linguistic, discourse, and multimodal annotation.

## Audacity

Audacity:  
https://www.audacityteam.org

Course use: Audio editing and preparation.

---

# 10. Digital Humanities Tools

## Voyant Tools

Voyant Tools:  
https://voyant-tools.org

Course use: Text analysis and visualization.

## AntConc

AntConc:  
https://www.laurenceanthony.net/software/antconc

Course use: Concordance and corpus linguistics.

## Gephi

Gephi:  
https://gephi.org

Course use: Network analysis and visualization.

## Palladio

Palladio:  
https://hdlab.stanford.edu/palladio

Course use: Historical data, network, and spatial visualization.

## Omeka

Omeka:  
https://omeka.org

Course use: Digital exhibits and collections.

## Scalar

Scalar:  
https://scalar.me

Course use: Digital publishing and multimedia scholarship.

---

# 11. Suggested Reading Order

If students only read 10 things:

1. OpenAI Codex Skills
2. Anthropic MCP Introduction
3. MCP Documentation / Registry
4. LangGraph Workflows vs Agents
5. Original RAG paper or LlamaIndex RAG introduction
6. ReAct
7. Reflexion
8. Tree of Thoughts or Self-Consistency
9. Harness Engineering / Agent Harness article
10. OpenAI Model Optimization or Fine-Tuning guide

This sequence supports:

```text
Skills
→ Tools
→ MCP
→ Workflows
→ Loops
→ RAG
→ Harnesses
→ Evaluation
→ Fine-Tuning
→ Humanities Research Platform
```

---

# 12. Suggested Placement in the GitHub Course

Recommended files:

```text
instructor_notes/advanced_course_references.md
sources/advanced_course_bibliography.bib
```

Optional future addition:

```text
advanced_topics/README.md
```

can include a short link:

```markdown
For advanced-course references, see:
../instructor_notes/advanced_course_references.md
```
