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
            if st.button("🗂 Study Roadmap"):
                send_message("Create a study roadmap from my uploaded notes. List the topics in the order they should be studied.")

        with c2:
            if st.button("📚 Explain in detail"):
                send_message("Explain this topic in more detail with examples.")

        with c3:
            if st.button("⚡ Quick revision"):
                send_message("Give me a quick revision of the uploaded notes in under 150 words.")

        with c4:
            if st.button("🧠 Memory tricks"):
                send_message("Suggest easy ways or memory tricks to remember the important concepts from my uploaded notes.")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything about your notes...")

    if prompt:
        send_message(prompt)