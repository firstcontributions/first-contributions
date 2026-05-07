# Introduction to AI Workflows

An **AI workflow** is a structured sequence of steps where AI models, tools, and human input work together to accomplish a task. Instead of asking one model one question, you design a pipeline — each step processes input, produces output, and passes it forward.

## Why AI Workflows Matter

A single prompt has limits. Workflows let you:

- Break complex problems into smaller, manageable steps
- Use specialized models for each sub-task
- Add validation, branching, and retry logic
- Keep humans in the loop where judgment matters
- Build repeatable, testable automation

## What You Will Learn

This tutorial series covers:

| Section | Topics |
|---|---|
| [Core Concepts](./core-concepts/what-is-an-ai-workflow.md) | Models, prompts, tokens, context |
| [Building Workflows](./building-workflows/sequential-workflows.md) | Sequential, parallel, and branching flows |
| [Tools & Frameworks](./tools-and-frameworks/langchain-tutorial.md) | LangChain, LlamaIndex, Anthropic SDK |
| [Advanced Topics](./advanced-topics/chaining-models.md) | Memory, evaluation, deployment |

## A Simple Example

```
User question
     │
     ▼
[Step 1] Classify intent (is this a question or a task?)
     │
     ├── question ──▶ [Step 2a] Retrieve relevant docs ──▶ [Step 3] Generate answer
     │
     └── task ──────▶ [Step 2b] Plan subtasks ──────────▶ [Step 3] Execute each step
```

This is the core idea: **route, process, respond**.

## Prerequisites

- Basic familiarity with how large language models (LLMs) work
- A working Python or JavaScript environment
- An API key from any model provider (Anthropic, OpenAI, etc.)

---

Next: [What Is an AI Workflow?](./core-concepts/what-is-an-ai-workflow.md)
