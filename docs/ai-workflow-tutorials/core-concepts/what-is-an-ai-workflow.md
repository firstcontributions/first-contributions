# What Is an AI Workflow?

An AI workflow is a **directed graph of steps** where each node is an operation — a model call, a function, a retrieval, or a human review — and the edges define how data flows between them.

## Key Properties

**Composable** — Small, focused steps are easier to debug and replace than one giant prompt.

**Stateful or stateless** — Some workflows carry memory across steps (chatbots), others process each input independently (batch classifiers).

**Deterministic or probabilistic** — Code steps are deterministic; model calls are probabilistic. Good workflow design minimizes uncontrolled randomness.

## Anatomy of a Step

Every step in an AI workflow has three parts:

```
Input ──▶ [ Processor ] ──▶ Output
```

The processor can be:

- An LLM prompt
- A function or API call
- A database query or vector search
- A human review checkpoint
- A routing condition

## Workflow vs. Single Prompt

| Single Prompt | Workflow |
|---|---|
| One model call | Many coordinated steps |
| Hard to debug | Each step is inspectable |
| Context limit bottleneck | Distribute context across steps |
| All-or-nothing | Retry individual failing steps |

## Real-World Examples

**Customer support bot**
1. Classify the ticket category
2. Retrieve relevant documentation
3. Draft a response
4. Route to human if confidence is low

**Code review assistant**
1. Parse changed files
2. Check for security issues (one model)
3. Check for style violations (rules engine)
4. Summarize findings

**Research summarizer**
1. Accept a topic
2. Search and retrieve sources
3. Summarize each source independently
4. Combine summaries into a final report

---

Next: [Types of AI Models](./types-of-ai-models.md)
