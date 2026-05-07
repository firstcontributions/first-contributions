# AI Workflow Tutorials

A practical guide to building AI workflows — structured pipelines where language models, tools, and human input work together to accomplish complex tasks.

## Contents

### [Introduction](./introduction-to-ai-workflows.md)
Start here. What AI workflows are, why they matter, and what this series covers.

### Core Concepts
Foundation knowledge you need before building anything.

| Tutorial | Description |
|---|---|
| [What Is an AI Workflow?](./core-concepts/what-is-an-ai-workflow.md) | Anatomy of a workflow, real-world examples |
| [Types of AI Models](./core-concepts/types-of-ai-models.md) | LLMs, embedding models, vision, specialized models |
| [Prompt Engineering](./core-concepts/prompt-engineering.md) | Writing reliable prompts for workflow steps |
| [Tokens and Context](./core-concepts/tokens-and-context.md) | Context windows, costs, and strategies for large inputs |

### Building Workflows
Hands-on patterns with working code examples.

| Tutorial | Description |
|---|---|
| [Sequential Workflows](./building-workflows/sequential-workflows.md) | Step-by-step pipelines |
| [Parallel Workflows](./building-workflows/parallel-workflows.md) | Running steps concurrently |
| [Branching Workflows](./building-workflows/branching-workflows.md) | Routing based on model output or rules |
| [Human-in-the-Loop](./building-workflows/human-in-the-loop.md) | Adding human review checkpoints |

### Tools and Frameworks
Practical tutorials for popular workflow libraries.

| Tutorial | Description |
|---|---|
| [LangChain](./tools-and-frameworks/langchain-tutorial.md) | Chains, RAG, and LCEL |
| [LlamaIndex](./tools-and-frameworks/llamaindex-tutorial.md) | Document ingestion and query engines |
| [Anthropic SDK](./tools-and-frameworks/anthropic-sdk-tutorial.md) | Direct API usage, tool use, caching |

### Advanced Topics
Production-grade techniques.

| Tutorial | Description |
|---|---|
| [Chaining Models](./advanced-topics/chaining-models.md) | Map-reduce, validate loops, cheap router patterns |
| [Evaluating Outputs](./advanced-topics/evaluating-outputs.md) | Rule checks, LLM-as-judge, regression testing |
| [Memory and State](./advanced-topics/memory-and-state.md) | In-context, session, and vector memory |
| [Deploying AI Workflows](./advanced-topics/deploying-ai-workflows.md) | Production checklist, retries, observability |

## Prerequisites

- Basic Python knowledge
- An API key from a model provider (Anthropic, OpenAI, etc.)
- Familiarity with how language models work at a high level

## Contributing

Translations are welcome. See the [translations](./translations/) folder.
