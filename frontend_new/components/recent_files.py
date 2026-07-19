import streamlit as st


def recent_files():
    """Display the user's recent uploaded files."""

    # Temporary: assume there are no uploaded files yet
    uploaded_files = []

    if not uploaded_files:
        st.info(
            """
### 📂 No files uploaded yet

Upload your first PDF, lecture notes, or study material to start using StudyMate AI.

You will then be able to:
- 💬 Chat with your notes
- 📝 Generate quizzes
- 🧠 Create flashcards
- 📊 Track your learning progress
"""
        )

        if st.button("📁 Upload Notes", key="empty_upload"):
            st.session_state.current_page = "Upload Notes"
            st.rerun()

        return

    # Future: display uploaded files here