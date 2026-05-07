# LangChain Tutorial

LangChain is a Python and JavaScript framework for building AI workflows. It provides composable building blocks — chains, retrievers, memory, agents — so you spend less time wiring plumbing and more time building logic.

## Installation

```bash
pip install langchain langchain-anthropic
```

## Your First Chain

A chain connects a prompt template to a model:

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Reply concisely."),
    ("human", "{question}")
])

chain = prompt | model

response = chain.invoke({"question": "What is a language model?"})
print(response.content)
```

The `|` operator pipes the prompt output into the model — this is LangChain's expression language (LCEL).

## Sequential Chain

Chain multiple steps together:

```python
from langchain_core.output_parsers import StrOutputParser

summarize_prompt = ChatPromptTemplate.from_template(
    "Summarize the following in 2 sentences:\n\n{text}"
)

translate_prompt = ChatPromptTemplate.from_template(
    "Translate the following to Spanish:\n\n{text}"
)

parser = StrOutputParser()

pipeline = (
    summarize_prompt | model | parser
    | (lambda text: {"text": text})
    | translate_prompt | model | parser
)

result = pipeline.invoke({"text": long_article})
print(result)
```

## Retrieval-Augmented Generation (RAG)

RAG retrieves relevant documents before answering — letting the model work with facts it was never trained on.

```python
from langchain_community.vectorstores import FAISS
from langchain_anthropic import AnthropicEmbeddings
from langchain_core.runnables import RunnablePassthrough

embeddings = AnthropicEmbeddings()
vectorstore = FAISS.from_texts(your_documents, embeddings)
retriever = vectorstore.as_retriever()

rag_prompt = ChatPromptTemplate.from_template("""
Answer using only the context below.

Context: {context}

Question: {question}
""")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | model
    | StrOutputParser()
)

answer = rag_chain.invoke("What is our refund policy?")
```

## Streaming Output

Stream tokens as they are generated instead of waiting for the full response:

```python
for chunk in chain.stream({"question": "Tell me about AI workflows."}):
    print(chunk.content, end="", flush=True)
```

## When to Use LangChain

**Good fit:**
- RAG pipelines
- Multi-step chains with structured data passing
- Integrating many third-party tools (databases, APIs, search)

**Consider alternatives when:**
- You only need a single model call (use the SDK directly)
- You need fine-grained control over every API parameter
- You find the abstractions make debugging harder

---

Next: [LlamaIndex Tutorial](./llamaindex-tutorial.md)
