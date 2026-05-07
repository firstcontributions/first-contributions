# Memory and State

AI models are stateless — each API call is independent. To build workflows that remember context, you must explicitly manage state and pass it between calls.

## Types of Memory

| Type | What It Stores | Lifespan |
|---|---|---|
| In-context (window) | The current conversation history | One session |
| External short-term | Session data in a database or cache | Minutes to hours |
| External long-term | User facts, preferences, past interactions | Days to permanent |
| Semantic (vector) | Searchable embeddings of past content | Permanent |

## In-Context Memory

The simplest approach: keep the full conversation in a list and pass it every call.

```python
import anthropic

client = anthropic.Anthropic()
history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=history
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply
```

**Limit:** History grows until it hits the context window. For long sessions, you need compression.

## Summarization Compression

When history gets long, summarize older turns:

```python
MAX_TURNS = 10

def compress_history(history):
    if len(history) <= MAX_TURNS:
        return history

    old_turns = history[:-MAX_TURNS]
    recent_turns = history[-MAX_TURNS:]

    summary_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in old_turns
    )

    summary = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        messages=[{
            "role": "user",
            "content": f"Summarize this conversation in 3 sentences:\n{summary_text}"
        }]
    ).content[0].text

    compressed = [
        {"role": "user", "content": f"[Earlier conversation summary: {summary}]"},
        {"role": "assistant", "content": "Understood."}
    ]
    return compressed + recent_turns
```

## External Short-Term Memory (Session Store)

Store session data in Redis or a simple dict keyed by session ID:

```python
import json

session_store = {}  # replace with Redis in production

def get_history(session_id):
    return session_store.get(session_id, [])

def save_history(session_id, history):
    session_store[session_id] = history

def chat(session_id, user_message):
    history = get_history(session_id)
    history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=history
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    save_history(session_id, history)
    return reply
```

## Semantic Memory (Vector Store)

Store facts as embeddings. Retrieve relevant memories by similarity before each call.

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

encoder = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
memories = []

def remember(fact):
    embedding = encoder.encode([fact])
    index.add(np.array(embedding))
    memories.append(fact)

def recall(query, top_k=3):
    embedding = encoder.encode([query])
    _, indices = index.search(np.array(embedding), top_k)
    return [memories[i] for i in indices[0] if i < len(memories)]

# Store facts
remember("User prefers concise answers.")
remember("User is a Python developer.")
remember("User is building a customer support bot.")

# Retrieve before each call
context = recall("What is the user working on?")
print(context)  # ["User is building a customer support bot.", ...]
```

## Choosing the Right Memory Type

- **Simple chatbot, short session** → In-context only
- **Multi-session chatbot** → In-context + external session store
- **Personalized assistant** → In-context + long-term vector store
- **Document Q&A** → Vector store for documents, in-context for conversation

---

Next: [Deploying AI Workflows](./deploying-ai-workflows.md)
