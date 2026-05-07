# Types of AI Models

Not every task needs the same model. Understanding the landscape helps you pick the right tool for each step in your workflow.

## Language Models (LLMs)

Large language models predict the next token given a sequence. They are the backbone of most AI workflows.

**Use for:** text generation, summarization, classification, code generation, question answering.

**Examples:** Claude (Anthropic), GPT-4 (OpenAI), Gemini (Google), LLaMA (Meta)

**Key tradeoff:** Larger models are more capable but slower and more expensive. Use smaller models for simple routing steps.

## Embedding Models

These convert text into a vector of numbers that captures semantic meaning. Similar texts produce similar vectors.

**Use for:** semantic search, clustering, deduplication, retrieval-augmented generation (RAG).

**Examples:** `text-embedding-3-small` (OpenAI), `embed-english-v3.0` (Cohere)

**Key tradeoff:** Embeddings are cheap and fast but tell you nothing about content — only similarity.

## Vision Models

Accept images (and sometimes video) as input alongside text.

**Use for:** image classification, OCR, document parsing, visual Q&A.

**Examples:** Claude 3 (Anthropic), GPT-4o (OpenAI), Gemini Vision (Google)

## Specialized Models

Purpose-built for a narrow task — often faster and cheaper than a general LLM.

| Type | Example Task |
|---|---|
| Speech-to-text | Transcribe audio |
| Text-to-speech | Generate spoken audio |
| Code completion | Fill in code at the cursor |
| Named entity recognition | Extract names/dates/places |
| Sentiment classifier | Label reviews as positive/negative |

## Choosing a Model for Your Step

Ask these questions:

1. **What is the input?** Text, image, audio, structured data?
2. **What is the expected output?** Free text, a label, a number, a vector?
3. **How much latency can this step tolerate?** Interactive steps need fast models.
4. **How often will this step run?** High-volume steps need cheap models.

---

Next: [Prompt Engineering](./prompt-engineering.md)
