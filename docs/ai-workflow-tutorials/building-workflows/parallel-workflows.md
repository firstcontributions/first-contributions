# Parallel Workflows

A parallel workflow runs multiple steps at the same time, then combines their results. Use this pattern when steps are independent — running them sequentially wastes time.

## Structure

```
         ┌──▶ Step A ──▶┐
Input ───┤──▶ Step B ──▶├──▶ Combine ──▶ Output
         └──▶ Step C ──▶┘
```

## When to Use Parallel Workflows

- When steps do not depend on each other
- When speed matters (parallel cuts total time to the slowest step)
- When you need multiple perspectives on the same input (ensemble)
- When processing a list of independent items

## Example: Multi-Aspect Document Review

**Goal:** Analyze a contract for security risks, legal issues, and tone — simultaneously.

```python
import anthropic
import concurrent.futures

client = anthropic.Anthropic()

def analyze(system, document):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=system,
        messages=[{"role": "user", "content": document}]
    )
    return response.content[0].text

document = open("contract.txt").read()

reviewers = {
    "legal":    "Identify clauses that create legal liability. List them as bullets.",
    "security": "Identify any data handling or privacy obligations in this contract.",
    "tone":     "Rate the tone: formal, neutral, or aggressive. Give one sentence of justification.",
}

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {
        name: executor.submit(analyze, prompt, document)
        for name, prompt in reviewers.items()
    }
    results = {name: future.result() for name, future in futures.items()}

print(results["legal"])
print(results["security"])
print(results["tone"])
```

## Example: Batch Processing a List

Process a list of items in parallel instead of one by one:

```python
reviews = ["Great product!", "Terrible experience.", "It was okay."]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    sentiments = list(executor.map(classify_sentiment, reviews))

# sentiments = ["positive", "negative", "neutral"]
```

## Combining Parallel Results

After parallel steps finish, you typically need to **aggregate** their outputs:

```python
# Option 1: Concatenate and pass to a final step
combined = "\n\n".join(f"## {k}\n{v}" for k, v in results.items())
final_summary = summarize(combined)

# Option 2: Structured merge
report = {
    "legal_risks":    results["legal"],
    "security_notes": results["security"],
    "tone":           results["tone"],
}
```

## Handling Partial Failures

One failed step should not kill the whole workflow. Use try/except per step:

```python
def safe_analyze(system, doc):
    try:
        return analyze(system, doc)
    except Exception as e:
        return f"ERROR: {e}"
```

## Concurrency Limits

Model APIs have rate limits. If you run too many parallel calls, you will get 429 errors. Use a semaphore or a bounded thread pool to cap concurrency:

```python
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    ...
```

---

Next: [Branching Workflows](./branching-workflows.md)
