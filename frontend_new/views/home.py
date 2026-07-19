import streamlit as st
from components.action_card import action_card
from components.progress_overview import progress_overview
from components.recent_files import recent_files
from components.hero import hero

def show():
    """Render the Home page."""

    # ---------- Hero ----------
    left, right = st.columns([3, 2], gap="large")

    with left:
      hero(
    "StudyMate AI",
    """
    Study smarter, not harder

    Upload your notes, chat with AI, generate quizzes,
    create flashcards, and monitor your learning progress—
    all from one clean and modern workspace.
    """
)

        
    if st.button("Get Started", type="primary"):
            st.session_state.current_page = "Upload Notes"
            st.rerun()

    with right:
        st.info(
            """
### What you can do

- Upload notes
- Ask AI questions
- Generate quizzes
- Create flashcards
- Track study progress
            """
        )
    st.divider()

    st.subheader("Quick Actions")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        action_card(
    "📁",
    "Upload Notes",
    "Upload PDFs or lecture notes to begin studying.",
    "Upload Notes",
        )
        action_card(
    "💬",
    "AI Chat",
    "Ask questions and receive simple explanations.",
    "AI Chat",
        )
    with col2:
        action_card(
    "📝",
    "Quiz",
    "Generate AI-powered quizzes from your uploaded notes.",
    "Quiz",
        )     

        action_card(
        "🧠",
        "Flashcards",
        "Create interactive flashcards for quick revision.",
        "Flashcards"
        )        
    with st.container(border=True):

      st.subheader("📊 Study Progress")

      progress_overview()
   
    with st.container(border=True):

      st.subheader("📂 Recent Files")

      recent_files()

    