import streamlit as st
import ollama

MODEL = "llama3.2"

SYSTEM = (
    "You are a friendly student assistant. Explain concepts simply with examples. "
    "When asked, make short quizzes, summaries and study plans. "
    "Reply in the same language the student writes in."
)

st.title("AI Student Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Em doubt undi?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    def generate():
        stream = ollama.chat(
            model=MODEL,
            messages=[{"role": "system", "content": SYSTEM}] + st.session_state.messages,
            stream=True,
        )
        for chunk in stream:
            yield chunk["message"]["content"]

    with st.chat_message("assistant"):
        reply = st.write_stream(generate())

    st.session_state.messages.append({"role": "assistant", "content": reply})