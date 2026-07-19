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

    # ==========================================================
    # SETTINGS
    # ==========================================================

    with st.container(border=True):
        flashcard_settings()

    st.write("")

    # ==========================================================
    # GENERATE FLASHCARDS
    # ==========================================================

    if st.button("🧠 Generate AI Flashcards", use_container_width=True):

        with st.spinner("Generating flashcards..."):

            result = generate_flashcards()

            st.session_state.flashcards["generated"] = result["answer"]

    # ==========================================================
    # DISPLAY FLASHCARDS
    # ==========================================================

    if st.session_state.flashcards.get("generated"):

        st.markdown("## 🧠 AI Generated Flashcards")

        with st.container(border=True):

            st.markdown(
                st.session_state.flashcards["generated"].replace("\\n", "\n")
            )