import streamlit as st


def score_card(questions, answers):

    total_questions = len(questions)

    correct_answers = 0

    for index, question in enumerate(questions):

        user_answer = answers.get(index)

        if user_answer == question["answer"]:
            correct_answers += 1

    wrong_answers = total_questions - correct_answers

    percentage = (correct_answers / total_questions) * 100

    st.success("🎉 Quiz Completed!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Score", f"{percentage:.0f}%")

    with col2:
        st.metric("Correct", correct_answers)

    with col3:
        st.metric("Wrong", wrong_answers)

    st.divider()

    st.subheader("📋 Answer Review")

    for index, question in enumerate(questions):

        user_answer = answers.get(index)

        correct_answer = question["answer"]

        with st.container(border=True):

            st.markdown(f"**Q{index + 1}. {question['question']}**")

            st.write(f"**Your Answer:** {user_answer}")

            st.write(f"**Correct Answer:** {correct_answer}")

            if user_answer == correct_answer:

                st.success("Correct")

            else:

                st.error("Incorrect")

    st.divider()

    if st.button("🔄 Retake Quiz", use_container_width=True):

        st.session_state.quiz = {
            "questions": [],
            "current": 0,
            "answers": {},
            "score": None,
            "submitted": False,
        }

        st.rerun()