# Deploying AI Workflows

A workflow that only runs on your laptop is a prototype. Deploying it means making it available, reliable, and observable in production.

## Deployment Checklist

Before going live, verify:

- [ ] API keys stored in environment variables, never in code
- [ ] Rate limiting and retry logic in place
- [ ] Timeouts set on every model call
- [ ] Errors logged with enough context to diagnose
- [ ] Input validation at system boundaries
- [ ] Cost tracking enabled

## Environment Variables

```bash
# .env file (never commit this)
ANTHROPIC_API_KEY=sk-ant-...
```

```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
```

## Retry with Backoff

Model APIs can return transient errors (rate limits, timeouts). Retry automatically:

```python
import time
import anthropic

def call_with_retry(client, **kwargs, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.messages.create(**kwargs)
        except anthropic.RateLimitError:
            wait = 2 ** attempt  # 1s, 2s, 4s
            print(f"Rate limited. Retrying in {wait}s...")
            time.sleep(wait)
        except anthropic.APIConnectionError:
            if attempt == max_retries - 1:
                raise
            time.sleep(1)
    raise RuntimeError("Max retries exceeded")
```

## Serving as an API with FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import anthropic

app = FastAPI()
client = anthropic.Anthropic()

class WorkflowRequest(BaseModel):
    question: str

@app.post("/ask")
async def run_workflow(req: WorkflowRequest):
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            messages=[{"role": "user", "content": req.question}]
        )
        return {"answer": response.content[0].text}
    except anthropic.APIStatusError as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Timeouts

Always set a timeout. A hung model call will block a thread (or a request slot) forever:

```python
import httpx

client = anthropic.Anthropic(
    timeout=httpx.Timeout(30.0, connect=5.0)
)
```

## Observability

Log structured events so you can debug production failures:

```python
import logging
import time
import json

logger = logging.getLogger(__name__)

def traced_call(step_name, fn, *args, **kwargs):
    start = time.time()
    try:
        result = fn(*args, **kwargs)
        logger.info(json.dumps({
            "step": step_name,
            "duration_ms": int((time.time() - start) * 1000),
            "status": "ok"
        }))
        return result
    except Exception as e:
        logger.error(json.dumps({
            "step": step_name,
            "duration_ms": int((time.time() - start) * 1000),
            "status": "error",
            "error": str(e)
        }))
        raise
```

## Cost Monitoring

Track usage per request. Sum up tokens to calculate monthly spend:

```python
COST_PER_M_INPUT  = 0.25   # $ per million input tokens (Haiku example)
COST_PER_M_OUTPUT = 1.25   # $ per million output tokens

def estimate_cost(usage):
    input_cost  = usage.input_tokens  / 1_000_000 * COST_PER_M_INPUT
    output_cost = usage.output_tokens / 1_000_000 * COST_PER_M_OUTPUT
    return input_cost + output_cost

response = client.messages.create(...)
print(f"Request cost: ${estimate_cost(response.usage):.6f}")
```

## Scaling Considerations

| Concern | Approach |
|---|---|
| High request volume | Queue requests; use async workers |
| Reducing latency | Cache frequent responses; use streaming |
| Reducing cost | Use smaller models for simple steps; cache prompts |
| Reliability | Multi-region API keys; circuit breakers |
| Security | Validate and sanitize all user inputs |

---

You have completed the AI Workflows tutorial series. Return to the [introduction](../introduction-to-ai-workflows.md) for a full overview.
