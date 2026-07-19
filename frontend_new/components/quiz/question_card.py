import streamlit as st


def question_card(question: dict, current: int, total: int):
    """
    Displays a single quiz question.

    Parameters
    ----------
    question : dict
        Example:
        {
            "question": "What is Artificial Intelligence?",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Option B"
        }

    current : int
        Current question index (starts from 0).

    total : int
        Total number of questions.

    Returns
    -------
    str
        The option selected by the user.
    """

    # -----------------------------
    # Progress Header
    # -----------------------------
    st.caption(f"Question {current + 1} of {total}")

    progress = (current + 1) / total
    st.progress(progress)

    st.write("")

    # -----------------------------
    # Question
    # -----------------------------
    st.markdown(f"### {question['question']}")

    st.write("")

    # -----------------------------
    # Options
    # -----------------------------
    selected_answer = st.radio(
        label="Choose your answer",
        options=question["options"],
        key=f"question_{current}",
        label_visibility="collapsed",
    )

    return selected_answer