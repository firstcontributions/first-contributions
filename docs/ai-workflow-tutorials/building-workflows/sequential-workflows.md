# Sequential Workflows

A sequential workflow runs steps one after another, where each step's output becomes the next step's input. This is the simplest and most common workflow pattern.

## Structure

```
Input ──▶ Step 1 ──▶ Step 2 ──▶ Step 3 ──▶ Output
```

Each step is isolated — it only knows about its own input and produces its own output.

## When to Use Sequential Workflows

- When steps have a natural order (translate, then summarize)
- When later steps depend on earlier results
- When you want clear, inspectable intermediate states
- When each step solves a different sub-problem

## Example: Article Processing Pipeline

**Goal:** Take a raw article URL, extract content, translate it, and summarize it.

```python
import anthropic

client = anthropic.Anthropic()

def call_model(system, user):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    return response.content[0].text

# Step 1: Extract the main content
raw_html = fetch_article(url)  # your own fetch function
content = call_model(
    system="Extract only the main article text. Remove navigation, ads, and footers.",
    user=raw_html
)

# Step 2: Translate to English
translated = call_model(
    system="Translate the following text to English. Preserve meaning and tone.",
    user=content
)

# Step 3: Summarize
summary = call_model(
    system="Write a 3-bullet summary of the article. Each bullet is one sentence.",
    user=translated
)

print(summary)
```

## Debugging Sequential Workflows

Log each intermediate result. When something goes wrong you will know exactly which step failed.

```python
steps = [
    ("extract",    extract_content),
    ("translate",  translate_to_english),
    ("summarize",  summarize),
]

result = raw_input
for name, fn in steps:
    result = fn(result)
    print(f"[{name}] → {result[:200]}")  # log first 200 chars
```

## Adding Validation Between Steps

Validate output before passing it forward to catch model errors early:

```python
translation = translate(content)

if len(translation) < 50:
    raise ValueError("Translation too short — model may have refused or failed")

summary = summarize(translation)
```

## Common Pitfall: Cascading Errors

In a sequential pipeline, an error in step 1 corrupts every downstream step. Always handle:

- Empty outputs
- Model refusals ("I can't help with that")
- Truncated or malformed JSON

---

Next: [Parallel Workflows](./parallel-workflows.md)
