import streamlit as st


def flashcard_stats():
    """
    Displays flashcard learning statistics.
    """

    flashcards = st.session_state.flashcards

    total = len(flashcards["cards"])

    known = len(flashcards["known"])

    review = len(flashcards["review"])
    reviewed = len(set(flashcards["known"] + flashcards["review"]))

    remaining = total - reviewed

    completion = 0

    if total > 0:
        completion = int(((known + review) / total) * 100)

    st.subheader("📊 Study Progress")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="✅ Known",
            value=known
        )

    with col2:
        st.metric(
            label="🔁 Review",
            value=review
        )

    with col3:
        st.metric(
            label="📚 Remaining",
            value=remaining
        )

    with col4:
        st.metric(
            label="🎯 Completion",
            value=f"{completion}%"
        )