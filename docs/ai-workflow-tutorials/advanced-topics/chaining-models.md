# Chaining Models

Model chaining uses the output of one model call as the input to the next. Done well, it produces results no single call could achieve. Done poorly, it compounds errors.

## Why Chain?

- **Decompose hard tasks** — A single prompt asking a model to "read this 50-page contract and identify every risk" often produces worse results than a chain that summarizes each section first
- **Use specialized models** — Use a cheap fast model for classification, a capable model only for generation
- **Exceed context limits** — Process data that is too large for a single context window
- **Self-check outputs** — Have one call generate, another validate

## Pattern 1: Generate → Validate

```python
import anthropic
import json

client = anthropic.Anthropic()

def generate(prompt):
    return client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    ).content[0].text

# Step 1: Generate a SQL query
sql = generate(f"Write a SQL query to find customers who spent over $1000 last month.")

# Step 2: Validate the query
validation = generate(f"""
Review this SQL query for correctness and security issues.
Return JSON: {{"valid": true/false, "issues": ["..."], "fixed_query": "..."}}

Query:
{sql}
""")

result = json.loads(validation)
final_query = result["fixed_query"] if not result["valid"] else sql
```

## Pattern 2: Map → Reduce

Process many chunks in parallel (map), then combine (reduce):

```python
import concurrent.futures

def summarize_chunk(chunk):
    return generate(f"Summarize this passage in 2 sentences:\n\n{chunk}")

def final_summary(summaries):
    combined = "\n\n".join(summaries)
    return generate(f"Synthesize these summaries into a single coherent overview:\n\n{combined}")

# Split large document into chunks
chunks = split_into_chunks(document, max_tokens=2000)

# Map: summarize each chunk in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    summaries = list(executor.map(summarize_chunk, chunks))

# Reduce: combine into final output
report = final_summary(summaries)
```

## Pattern 3: Cheap Router → Expensive Worker

Use a fast, cheap model for routing. Only invoke the expensive model when needed.

```python
haiku = anthropic.Anthropic()
sonnet = anthropic.Anthropic()

def route(question):
    response = haiku.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=16,
        system="Reply with only: simple or complex",
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text.strip()

def answer_simple(question):
    return haiku.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        messages=[{"role": "user", "content": question}]
    ).content[0].text

def answer_complex(question):
    return sonnet.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": question}]
    ).content[0].text

question = "What is the capital of France?"
difficulty = route(question)
answer = answer_simple(question) if difficulty == "simple" else answer_complex(question)
```

## Avoiding Error Propagation

Every link in a chain is a failure point. Strategies:

1. **Validate outputs structurally** — If a step must return JSON, parse it and catch errors immediately
2. **Set fallbacks** — If validation fails, retry with a clearer prompt or fall through to a safe default
3. **Log intermediate outputs** — So you can diagnose exactly where a bad chain broke down
4. **Keep chains short** — Each added step multiplies latency and failure probability

## Cost Accounting

Track tokens at each step to understand where your costs come from:

```python
response = client.messages.create(...)
print(f"Step 1 — input: {response.usage.input_tokens}, output: {response.usage.output_tokens}")
```

---

Next: [Evaluating Outputs](./evaluating-outputs.md)
