import streamlit as st
from components.page_header import page_header
from utils.api import ask_ai


def send_message(question):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:
        result = ask_ai(question)
        answer = result["answer"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"❌ Error: {e}"
            }
        )

    st.rerun()


def show():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    page_header(
        "💬 AI Study Assistant",
        "Ask questions about your uploaded notes and get simple explanations."
    )

    left, right = st.columns([5, 1])

    with right:
        if st.button("🗑 Clear"):
            st.session_state.messages = []
            st.rerun()

    if len(st.session_state.messages) == 0:

        with st.container(border=True):

            st.markdown("## 👋 Welcome!")

            st.write("""
I'm your AI study assistant.

I can help you:

- 📚 Explain difficult concepts
- 📝 Summarize your notes
- 🎯 Generate quiz questions
- 🧠 Create flashcards
""")

        st.subheader("✨ Try asking")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            if st.button("📖 Summarize my notes"):
                send_message("Summarize my notes.")

        with c2:
            if st.button("📝 Generate a quiz"):
                send_message("Generate a quiz.")

        with c3:
            if st.button("💡 Explain simply"):
                send_message("Explain this topic simply.")

        with c4:
            if st.button("🧠 Create flashcards"):
                send_message("Create flashcards.")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything about your notes...")

    if prompt:
        send_message(prompt)