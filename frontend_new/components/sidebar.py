import streamlit as st

# Navigation items
NAV_ITEMS = [
    ("🏠", "Home"),
    ("📁", "Upload Notes"),
    ("💬", "AI Chat"),
    ("📝", "Quiz"),
    ("🧠", "Flashcards"),
    ("📊", "Progress Dashboard"),
]


def render_sidebar():
    """Render the application sidebar."""

    with st.sidebar:
        st.markdown("# StudyMate AI")
        st.caption("Your AI Study Companion")

        st.divider()

        st.markdown("### Navigation")

        # Create the page state the first time the app runs
        if "current_page" not in st.session_state:
            st.session_state.current_page = "Home"

        # Navigation buttons
        for icon, page in NAV_ITEMS:
            if st.button(
                f"{icon}  {page}",
                use_container_width=True,
                key=f"nav_{page}"
            ):
                st.session_state.current_page = page

        st.divider()

        st.caption("Built for better learning.")