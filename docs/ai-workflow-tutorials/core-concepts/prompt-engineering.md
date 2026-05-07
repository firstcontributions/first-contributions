# Prompt Engineering

A prompt is the instruction you send to a model. In a workflow, every model call has a prompt — getting it right determines the quality and reliability of the step's output.

## Anatomy of a Good Prompt

```
[Role]       You are a customer support specialist.
[Context]    The user has a billing issue with subscription plan X.
[Task]       Draft a polite reply that explains how to request a refund.
[Format]     Keep it under 100 words. Use plain language.
[Input]      User message: "{{user_message}}"
```

Each section serves a purpose:

- **Role** — sets the model's perspective and tone
- **Context** — supplies facts the model cannot know on its own
- **Task** — states exactly what to produce
- **Format** — controls output shape (length, structure, language)
- **Input** — the variable part injected at runtime

## System vs. User Prompts

Most APIs split the prompt into two roles:

| Role | Purpose |
|---|---|
| `system` | Persistent instructions that define the model's behavior across the conversation |
| `user` | The current input from the human or previous step |

Keep stable instructions in `system`. Put dynamic content in `user`.

## Few-Shot Examples

When you want consistent output format, show examples inside the prompt:

```
Classify the sentiment of the review. Reply with only: positive, negative, or neutral.

Examples:
Review: "Loved it!" → positive
Review: "Terrible service." → negative
Review: "It arrived on time." → neutral

Review: "{{review_text}}" →
```

## Chain-of-Thought

For reasoning tasks, ask the model to think before answering:

```
Think step by step before giving your final answer.
Wrap your reasoning in <thinking> tags and your answer in <answer> tags.
```

This improves accuracy on math, logic, and multi-step problems.

## Structured Output

Ask for JSON to make the output machine-readable and easy to pass to the next step:

```
Return a JSON object with these fields:
{
  "category": "billing | technical | general",
  "priority": "low | medium | high",
  "summary": "one sentence"
}
```

## Common Mistakes

- **Too vague** — "Summarize this" without specifying length, audience, or format
- **Over-constraining** — So many rules the model gets confused
- **Missing context** — Expecting the model to know things it cannot see
- **No output format** — Getting inconsistent structures that break the next step

---

Next: [Tokens and Context](./tokens-and-context.md)
