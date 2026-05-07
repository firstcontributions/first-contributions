# Human-in-the-Loop Workflows

Not every step should be automated. **Human-in-the-loop (HITL)** design adds checkpoints where a person reviews, approves, or corrects the model's output before the workflow continues.

## Why HITL Matters

- Models make mistakes, especially on edge cases
- Some decisions carry legal, financial, or reputational risk
- Automated workflows can fail silently — humans catch what metrics miss
- Users trust systems more when they know a human can intervene

## Patterns

### 1. Gate Pattern

The workflow pauses and waits for human approval before proceeding.

```
AI drafts response ──▶ Human approves/edits ──▶ Response is sent
```

**Use when:** The output has significant consequences (sending an email, publishing content, making a payment).

### 2. Review Queue Pattern

The AI processes everything automatically, but flags low-confidence results for human review.

```
AI classifies ──▶ High confidence ──▶ Auto-complete
                └▶ Low confidence  ──▶ Add to review queue ──▶ Human reviews ──▶ Complete
```

**Use when:** Volume is high, most cases are easy, but a small fraction are ambiguous.

### 3. Correction Loop Pattern

A human reviews a sample of AI outputs and corrects errors. Corrections feed back into prompt improvements.

```
AI output ──▶ Random sample ──▶ Human reviews ──▶ Flag errors ──▶ Improve prompts
```

**Use when:** You want to improve the workflow over time.

## Implementation: Simple Approval Gate

```python
def request_human_approval(draft):
    print("\n--- AI Draft ---")
    print(draft)
    print("----------------")
    decision = input("Approve? (yes / edit / reject): ").strip().lower()

    if decision == "yes":
        return draft
    elif decision == "edit":
        return input("Enter your revised version: ")
    else:
        return None  # workflow stops

draft = generate_draft(user_request)
approved = request_human_approval(draft)

if approved:
    send_to_user(approved)
else:
    print("Draft rejected. Workflow stopped.")
```

## Implementation: Confidence-Based Queue

```python
CONFIDENCE_THRESHOLD = 0.9
review_queue = []

for item in batch:
    result = classify(item)
    if result["confidence"] >= CONFIDENCE_THRESHOLD:
        auto_process(item, result)
    else:
        review_queue.append({"item": item, "ai_result": result})

# Human processes the queue separately
for entry in review_queue:
    print(f"Item: {entry['item']}")
    print(f"AI suggestion: {entry['ai_result']}")
    correct_label = input("Your label: ")
    manual_process(entry["item"], correct_label)
```

## Designing Good HITL Checkpoints

**Show reasoning** — Display the model's confidence and why it made the choice. A reviewer who understands the model's logic can correct it faster.

**Make it easy to override** — A cumbersome review UI means reviewers rubber-stamp everything. The UI should make editing as fast as approving.

**Track every decision** — Log what the model predicted and what the human chose. This data is invaluable for improving the model.

**Set escalation thresholds thoughtfully** — Too low: humans review everything (defeats the purpose). Too high: risky decisions get auto-approved.

---

Next: [LangChain Tutorial](../tools-and-frameworks/langchain-tutorial.md)
