# Anthropic SDK Tutorial

The Anthropic SDK is the direct interface to Claude models. Use it when you want full control without framework abstractions.

## Installation

```bash
pip install anthropic
```

## Basic Message

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain prompt chaining in one paragraph."}
    ]
)

print(message.content[0].text)
```

## System Prompts

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=512,
    system="You are a senior software engineer. Be concise and technical.",
    messages=[
        {"role": "user", "content": "What is the difference between RAG and fine-tuning?"}
    ]
)
```

## Multi-Turn Conversations

Build a conversation by appending messages:

```python
messages = []

def chat(user_message):
    messages.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=messages
    )
    assistant_message = response.content[0].text
    messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

print(chat("What is a token?"))
print(chat("How many tokens are in a typical paragraph?"))
```

## Tool Use (Function Calling)

Let Claude call functions in your code:

```python
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"]
        }
    }
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=512,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}]
)

# Check if Claude wants to use a tool
if response.stop_reason == "tool_use":
    tool_call = next(b for b in response.content if b.type == "tool_use")
    print(f"Calling {tool_call.name} with {tool_call.input}")
    # Execute the tool and send the result back
```

## Streaming

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "List 5 AI workflow patterns."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

## Prompt Caching

Cache expensive parts of your prompt (long system prompts, large documents) to reduce cost and latency on repeated calls:

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": very_long_document,
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": "Summarize the key risks."}]
)
```

The first call pays full input cost. Subsequent calls with the same cached prefix are significantly cheaper.

## Error Handling

```python
from anthropic import APIStatusError, APIConnectionError

try:
    response = client.messages.create(...)
except APIStatusError as e:
    if e.status_code == 429:
        print("Rate limited — back off and retry")
    elif e.status_code == 400:
        print(f"Bad request: {e.message}")
except APIConnectionError:
    print("Network error — check your connection")
```

---

Next: [Chaining Models](../advanced-topics/chaining-models.md)
