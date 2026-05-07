# LlamaIndex Tutorial

LlamaIndex focuses on **data ingestion and retrieval** for AI workflows. Where LangChain is a general workflow framework, LlamaIndex specializes in connecting LLMs to your own data — documents, databases, APIs.

## Installation

```bash
pip install llama-index llama-index-llms-anthropic
```

## Core Concepts

| Concept | Description |
|---|---|
| `Document` | A loaded piece of content (PDF, webpage, database row) |
| `Node` | A chunk of a document after splitting |
| `Index` | A searchable structure built from nodes |
| `Retriever` | Fetches relevant nodes for a query |
| `Query Engine` | Retrieves nodes and generates an answer |

## Loading and Indexing Documents

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings

# Configure the LLM
Settings.llm = Anthropic(model="claude-haiku-4-5-20251001")

# Load all documents from a folder
documents = SimpleDirectoryReader("./docs").load_data()

# Build a searchable index
index = VectorStoreIndex.from_documents(documents)
```

## Querying the Index

```python
query_engine = index.as_query_engine()
response = query_engine.query("What is the return policy?")
print(response)
```

LlamaIndex automatically retrieves relevant document chunks and generates an answer grounded in your data.

## Persisting the Index

Rebuilding the index from scratch every run is slow. Save it to disk:

```python
# Save
index.storage_context.persist("./index_storage")

# Load later
from llama_index.core import StorageContext, load_index_from_storage

storage = StorageContext.from_defaults(persist_dir="./index_storage")
index = load_index_from_storage(storage)
```

## Chat Engine (Conversational RAG)

Turn the index into a chatbot that remembers the conversation:

```python
chat_engine = index.as_chat_engine(chat_mode="condense_plus_context")

response = chat_engine.chat("What documents do I need for onboarding?")
print(response)

follow_up = chat_engine.chat("Can you summarize that in bullet points?")
print(follow_up)
```

## Querying Structured Data

LlamaIndex can also query SQL databases using natural language:

```python
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from sqlalchemy import create_engine

engine = create_engine("sqlite:///company.db")
sql_database = SQLDatabase(engine, include_tables=["orders", "customers"])

query_engine = NLSQLTableQueryEngine(sql_database=sql_database)
response = query_engine.query("How many orders were placed in April?")
print(response)
```

## LlamaIndex vs. LangChain

| Feature | LlamaIndex | LangChain |
|---|---|---|
| Primary focus | Data ingestion and RAG | General workflow orchestration |
| Document loaders | Extensive built-in support | Available via integrations |
| Query engines | First-class concept | Build manually with chains |
| Agents | Supported | More mature ecosystem |

Use LlamaIndex when your workflow is heavily document-centric. Use LangChain when you need more general control flow.

---

Next: [Anthropic SDK Tutorial](./anthropic-sdk-tutorial.md)
