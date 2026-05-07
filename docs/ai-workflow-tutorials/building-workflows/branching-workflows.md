# Branching Workflows

A branching workflow routes input down different paths depending on a condition — either a model's classification or a deterministic rule. This makes workflows adaptive rather than rigid.

## Structure

```
Input ──▶ Router ──┬──▶ Path A ──▶ Output A
                  ├──▶ Path B ──▶ Output B
                  └──▶ Path C ──▶ Output C
```

## Types of Branching

**Model-based routing** — A cheap model classifies the input, and the result determines which path runs.

**Rule-based routing** — A deterministic condition (keyword, length, format) determines the path.

**Threshold routing** — A confidence score decides whether to use automation or escalate to a human.

## Example: Customer Support Router

```python
import anthropic
import json

client = anthropic.Anthropic()

def classify_intent(message):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=64,
        system="""Classify the customer message into one category.
Return only valid JSON: {"category": "billing|technical|general|escalate"}""",
        messages=[{"role": "user", "content": message}]
    )
    return json.loads(response.content[0].text)["category"]

def handle_billing(message):
    return "I can help with your billing question..."

def handle_technical(message):
    return "Let me walk you through the technical steps..."

def handle_general(message):
    return "Here is some general information..."

def escalate_to_human(message):
    return "Connecting you to a support agent..."

handlers = {
    "billing":   handle_billing,
    "technical": handle_technical,
    "general":   handle_general,
    "escalate":  escalate_to_human,
}

user_message = "I was charged twice this month."
category = classify_intent(user_message)
response = handlers[category](user_message)
print(f"[{category}] {response}")
```

## Example: Confidence-Based Escalation

Only automate when the model is confident. Otherwise, route to a human:

```python
def classify_with_confidence(text):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=64,
        system="""Classify the sentiment. Return JSON:
{"sentiment": "positive|negative|neutral", "confidence": 0.0-1.0}""",
        messages=[{"role": "user", "content": text}]
    )
    return json.loads(response.content[0].text)

result = classify_with_confidence("The product is fine I guess.")

if result["confidence"] >= 0.85:
    auto_respond(result["sentiment"])
else:
    queue_for_human_review(result)
```

## Keeping Routers Simple

The router's only job is to classify — it should not try to solve the problem. Keep router prompts short and their outputs structured (JSON labels, not prose).

**Good router prompt:** `"Classify the intent: billing, technical, or general. Reply with only the category."`

**Bad router prompt:** `"Understand the user's problem and figure out what they need help with."`

## Nested Branching

Branches can themselves contain branches. Keep depth shallow — two or three levels is usually the maximum before the workflow becomes hard to follow.

```
Router (intent)
  └── technical
        └── Router (platform)
              ├── web
              └── mobile
```

---

Next: [Human-in-the-Loop](./human-in-the-loop.md)
