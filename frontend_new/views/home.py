import streamlit as st
from components.action_card import action_card
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
    Your AI-powered study companion

    Upload your notes, chat with AI, generate quizzes,
    and create flashcards—all from one clean and modern workspace.
    """
    )
    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button(
            "📁 Upload Notes",
            type="primary",
            use_container_width=True
        ):
            st.session_state.current_page = "Upload Notes"
            st.rerun()

        
    st.success("""
    🚀 **Quick Start**

    1. Upload your PDF notes
    2. Ask AI questions
    3. Generate quizzes
    4. Review flashcards
    """)

    with right:
        st.info(
            """
### What you can do

- Upload notes
- Ask AI questions
- Generate quizzes
- Create flashcards
            """
        )
    st.divider()

    st.subheader("📚 Learning Tools")
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

      st.subheader("📂 Upload Status")

      recent_files()

    st.divider()

    st.caption(
        "Built with ❤️ using FastAPI • Streamlit • LangChain • ChromaDB • Groq"
    )