import streamlit as st


def show():

    # =====================================================
    # PAGE HEADER
    # =====================================================

    def show():

        st.title("📚 Study Dashboard")

        st.caption(
            "Everything you need to continue learning from your uploaded notes."
        )

        st.divider()

    st.write("")

    st.subheader("📂 Current Uploaded File")

    st.info(
        """
    The most recently uploaded PDF will be used for:

    - 💬 AI Chat
    - 📝 Quiz Generator
    - 🧠 Flashcards

    Uploading a new PDF automatically replaces the previous one.
    """
    )

    st.divider()

    st.subheader("🤖 AI Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
    ### 💬 AI Chat

    Ask questions directly from your uploaded notes and receive AI-generated answers.
    """
        )

    with col2:
        st.info(
            """
    ### 📝 Quiz Generator

    Generate quizzes instantly to test your understanding.
    """
    )

    with col3:
        st.info(
            """
    ### 🧠 Flashcards

    Create AI-powered flashcards for quick revision.
    """
        )

    st.divider()

    st.subheader("🚀 How StudyMate AI Works")

    st.success(
        """
    1. Upload your PDF notes.

    2. Ask AI questions.

    3. Generate quizzes.

    4. Review flashcards.

    💡 Uploading a new PDF automatically replaces the previous one.
    """
    )