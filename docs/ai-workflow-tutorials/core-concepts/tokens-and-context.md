# Tokens and Context

Every model has a **context window** — the maximum amount of text it can process at once. Understanding tokens is essential for designing workflows that don't fail silently when inputs grow large.

## What Is a Token?

Models do not read characters — they read **tokens**, which are chunks of text determined by a tokenizer. As a rough rule of thumb:

- 1 token ≈ 4 characters in English
- 1 token ≈ 0.75 words
- 100 tokens ≈ 75 words

Examples:
```
"Hello, world!" → 4 tokens
"AI workflows are composable pipelines." → 7 tokens
```

## Context Window

The context window is the total number of tokens a model can see in one call — this includes your system prompt, the conversation history, and the expected output.

| Model | Approximate Context |
|---|---|
| Claude 3 Haiku | 200,000 tokens |
| Claude 3.5 Sonnet | 200,000 tokens |
| GPT-4o | 128,000 tokens |
| Gemini 1.5 Pro | 1,000,000 tokens |

A 200,000-token context can hold roughly a 150,000-word book — but using a large context increases cost and latency.

## Input Tokens vs. Output Tokens

APIs charge separately for input (what you send) and output (what the model generates). Input tokens are usually cheaper than output tokens.

**Workflow implication:** Keep intermediate steps concise. Don't pass full documents through every step when only a summary is needed.

## What Happens When You Exceed the Limit?

- The API returns an error
- Or the oldest messages get silently truncated (in chat APIs)

Design your workflow to never depend on silent truncation — it produces unpredictable results.

## Strategies for Managing Context

**Summarize early** — Before passing a long document to multiple steps, summarize it once.

**Chunk and process** — Split large inputs into chunks, process each independently, then combine.

**Selective retrieval** — Instead of passing everything, use an embedding search to retrieve only the relevant parts (RAG).

**Compress history** — In long conversations, periodically summarize older turns instead of keeping every message.

## Counting Tokens in Code

```python
import anthropic

client = anthropic.Anthropic()

# Count tokens before sending
response = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    system="You are a helpful assistant.",
    messages=[{"role": "user", "content": "Explain AI workflows in one paragraph."}]
)

print(response.input_tokens)  # e.g., 24
```

---

Next: [Sequential Workflows](../building-workflows/sequential-workflows.md)
