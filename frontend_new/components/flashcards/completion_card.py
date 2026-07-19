import streamlit as st


def completion_card():
    """
    Displays the completion screen after all flashcards
    have been reviewed.
    """

    flashcards = st.session_state.flashcards

    total = len(flashcards["cards"])
    known = len(flashcards["known"])
    review = len(flashcards["review"])

    accuracy = 0

    if total > 0:
        accuracy = round((known / total) * 100) if total else 0

    st.success("🎉 Congratulations!")

    st.title("Flashcard Session Completed")

    st.write(
        "You have reviewed all the flashcards in this study session."
    )

    st.write("")

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Total Cards",
            total,
        )

    with col2:
        st.metric(
            "✅ Known",
            known,
        )

    with col3:
        st.metric(
            "🔁 Review",
            review,
        )

    with col4:
        st.metric(
            "🎯 Accuracy",
            f"{accuracy}%"
        )

    st.divider()

    # ----------------------------------------------------
    # Restart Session
    # ----------------------------------------------------

    if st.button(
        "🔄 Restart Session",
        use_container_width=True,
    ):

        flashcards["current"] = 0
        flashcards["known"] = []
        flashcards["review"] = []
        flashcards["completed"] = False
        flashcards["show_answer"] = False

        st.rerun()

    # ----------------------------------------------------
    # Generate New Flashcards
    # ----------------------------------------------------

    if st.button(
        "✨ Generate New Flashcards",
        use_container_width=True,
    ):

        flashcards["cards"] = []
        flashcards["current"] = 0
        flashcards["known"] = []
        flashcards["review"] = []
        flashcards["completed"] = False
        flashcards["show_answer"] = False

        st.rerun()