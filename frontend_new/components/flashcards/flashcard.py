import streamlit as st


def flashcard(card: dict):
    """
    Displays a single flashcard.

    Parameters
    ----------
    card : dict

    Example

    {
        "question": "...",
        "answer": "..."
    }
    """

    # --------------------------------------------------------
    # Progress Header
    # --------------------------------------------------------

    current = st.session_state.flashcards["current"] + 1

    total = len(st.session_state.flashcards["cards"])

    st.caption(f"Card {current} of {total}")

    st.progress(current / total)

    st.write("")

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.markdown("## ❓ Question")

    st.info(card["question"])

    st.write("")

    # --------------------------------------------------------
    # FLIP BUTTON
    # --------------------------------------------------------

    if not st.session_state.flashcards["show_answer"]:

        if st.button(
            "🔄 Flip Card",
            use_container_width=True,
            key=f"flip_{current}"
        ):

            st.session_state.flashcards["show_answer"] = True

            st.rerun()

    # --------------------------------------------------------
    # ANSWER
    # --------------------------------------------------------

    if st.session_state.flashcards["show_answer"]:

        st.write("")

        st.markdown("## ✅ Answer")

        st.success(card["answer"])