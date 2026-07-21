import streamlit as st

from components.page_header import page_header
from components.quiz.quiz_settings import quiz_settings
from components.quiz.question_card import question_card
from components.quiz.quiz_navigation import quiz_navigation
from components.quiz.score_card import score_card
from utils.api import generate_quiz


def show():

    # ======================================================
    # SESSION STATE
    # ======================================================

    if "quiz" not in st.session_state:
        st.session_state.quiz = {
            "questions": [],
            "current": 0,
            "answers": {},
            "score": None,
            "submitted": False,
            "generated_quiz": None,
        }

    # ======================================================
    # PAGE HEADER
    # ======================================================

    page_header(
        "📝 Quiz Generator",
        "Practice with AI-generated questions from your uploaded notes."
    )
    with st.container(border=True):
        st.markdown("""
    ### 💡 How it works

    1. 📂 Upload your study notes
    2. 🚀 Generate an AI Quiz
    3. 📝 Test your understanding instantly
    """
    )
  

    # ======================================================
    # TEMPORARY SAMPLE QUESTIONS
    # Replace this with backend later
    # ======================================================

    if st.button("📝 Generate Quiz", use_container_width=True):

        with st.spinner("📝 AI is generating quiz questions..."):

            result = generate_quiz()

            st.session_state.quiz["generated_quiz"] = result["answer"]

    if st.session_state.quiz.get("generated_quiz"):

        st.markdown("##📝 Generate Quiz")

        with st.container(border=True):
            st.markdown(
                st.session_state.quiz["generated_quiz"].replace("\\n", "\n")
            )  
    return


    



    #questions = st.session_state.quiz["questions"]

    #current = st.session_state.quiz["current"]

    # ======================================================
    # SHOW SCORE PAGE
    # ======================================================

    if st.session_state.quiz["submitted"]:

        with st.container(border=True):

            score_card(
                questions=questions,
                answers=st.session_state.quiz["answers"],
            )

        return

    # ======================================================
    # CURRENT QUESTION
    # ======================================================

    current_question = questions[current]

    # ======================================================
    # QUESTION CARD
    # ======================================================

    with st.container(border=True):

        selected_answer = question_card(
            question=current_question,
            current=current,
            total=len(questions),
        )

    # Save selected answer

    st.session_state.quiz["answers"][current] = selected_answer

    st.write("")

    # ======================================================
    # NAVIGATION
    # ======================================================

    with st.container(border=True):

        action = quiz_navigation(
            current=current,
            total=len(questions),
        )

    # ======================================================
    # NAVIGATION LOGIC
    # ======================================================

    if action == "next":

        if current < len(questions) - 1:

            st.session_state.quiz["current"] += 1

            st.rerun()

    elif action == "previous":

        if current > 0:

            st.session_state.quiz["current"] -= 1

            st.rerun()

    elif action == "submit":

        st.session_state.quiz["submitted"] = True

        st.rerun()