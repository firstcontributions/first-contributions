# Evaluating Outputs

You cannot improve what you do not measure. Evaluation tells you whether your workflow is working — and which step is responsible when it is not.

## Types of Evaluation

### 1. Automated Rule-Based Checks

Fast and cheap. Catch obvious failures immediately.

```python
def validate_output(text):
    checks = {
        "not_empty":       len(text.strip()) > 0,
        "not_refusal":     "I cannot" not in text and "I'm sorry" not in text,
        "within_length":   len(text) < 2000,
        "is_json":         is_valid_json(text),  # only if JSON expected
    }
    failed = [name for name, passed in checks.items() if not passed]
    return failed
```

### 2. Model-Graded Evaluation (LLM-as-Judge)

Use a model to evaluate another model's output. Effective for quality dimensions that are hard to define with rules.

```python
import anthropic
import json

client = anthropic.Anthropic()

def grade_response(question, answer, criteria):
    prompt = f"""
Grade the following answer on a scale of 1-5 for each criterion.
Return JSON: {{"scores": {{"accuracy": N, "clarity": N, "completeness": N}}, "reasoning": "..."}}

Question: {question}
Answer: {answer}
Criteria: {criteria}
"""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.content[0].text)

result = grade_response(
    question="What is prompt chaining?",
    answer=workflow_output,
    criteria="accuracy, clarity, completeness"
)
print(result["scores"])
```

### 3. Human Evaluation

Ground truth. Use a small labeled set to calibrate your automated metrics.

Build a simple annotation interface:

```python
for i, (question, answer) in enumerate(samples):
    print(f"\n[{i+1}/{len(samples)}] Q: {question}")
    print(f"A: {answer}")
    score = int(input("Score 1-5: "))
    notes = input("Notes (optional): ")
    annotations.append({"question": question, "answer": answer, "score": score, "notes": notes})
```

## What to Measure

| Metric | Description | Method |
|---|---|---|
| Accuracy | Is the answer factually correct? | LLM judge or human |
| Groundedness | Is the answer supported by retrieved docs? | LLM judge |
| Refusal rate | How often does the model refuse valid requests? | Rule check |
| Latency | How long does each step take? | Timing |
| Cost | How many tokens does each step consume? | Usage field |
| Format compliance | Does the output match the expected structure? | Parser |

## Building an Evaluation Dataset

1. Collect 50–200 representative inputs
2. Generate outputs with your current workflow
3. Label each output (human or LLM judge)
4. Store as `{"input": "...", "output": "...", "label": "..."}` in a JSONL file

Run this dataset after every workflow change to catch regressions.

## Regression Testing

```python
import json

def run_eval(test_file, workflow_fn):
    with open(test_file) as f:
        cases = [json.loads(line) for line in f]

    passed = 0
    for case in cases:
        output = workflow_fn(case["input"])
        grade = grade_response(case["input"], output, "accuracy")
        if grade["scores"]["accuracy"] >= 4:
            passed += 1

    print(f"Pass rate: {passed}/{len(cases)} ({100*passed//len(cases)}%)")

run_eval("eval_set.jsonl", my_workflow)
```

## A/B Testing Prompts

When changing a prompt, test both versions on the same inputs and compare scores before switching:

```python
results_a = [grade(q, prompt_a(q)) for q in test_questions]
results_b = [grade(q, prompt_b(q)) for q in test_questions]

avg_a = sum(r["scores"]["accuracy"] for r in results_a) / len(results_a)
avg_b = sum(r["scores"]["accuracy"] for r in results_b) / len(results_b)

print(f"Prompt A: {avg_a:.2f} | Prompt B: {avg_b:.2f}")
```

---

Next: [Memory and State](./memory-and-state.md)
