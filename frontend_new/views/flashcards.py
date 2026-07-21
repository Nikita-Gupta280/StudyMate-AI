import streamlit as st

from components.page_header import page_header
from components.flashcards.flashcard_settings import flashcard_settings
from utils.api import generate_flashcards


def show():

    # ==========================================================
    # SESSION STATE
    # ==========================================================

    if "flashcards" not in st.session_state:

        st.session_state.flashcards = {
            "generated": None
        }

    # ==========================================================
    # PAGE HEADER
    # ==========================================================

    page_header(
        "🧠 AI Flashcards",
        "Review concepts generated from your uploaded notes."
    )

    with st.container(border=True):
        st.markdown(
            """
### 💡 How it works

1. 📂 Upload your notes
2. 🚀 Click **Generate Flashcards**
3. 📖 Review concepts instantly
""")
    st.write("")

    # ==========================================================
    # GENERATE FLASHCARDS
    # ==========================================================

    if st.button("🚀 Generate Flashcards", use_container_width=True):

        with st.spinner("🧠 AI is creating flashcards..."):

            result = generate_flashcards()

            st.session_state.flashcards["generated"] = result["answer"]

        

    # ==========================================================
    # DISPLAY FLASHCARDS
    # ==========================================================

    if st.session_state.flashcards.get("generated"):

        st.markdown("## 🚀 Generate Flashcards")

        flashcards = st.session_state.flashcards["generated"].replace("\\n", "\n")

        cards = flashcards.split("Flashcard ")
        cards = [c for c in cards if c.strip().startswith(tuple(str(i) for i in range(1, 10)))]

        for card in cards:

            if not card.strip():
                continue

            lines = card.strip().split("\n")

            title = lines[0]

            content = "\n".join(lines[1:])

            with st.expander(f"🧠 Flashcard {title}"):

                content = (
                    content
                    .replace("Front", "**📌 Question**")
                    .replace("Back", "**💡 Answer**")
                    .replace("🧠", "")
                    .replace("---", "")
                    .strip()                        
                )

                import re

                content = re.sub(r"\n{3,}", "\n\n", content)


                st.markdown(content)