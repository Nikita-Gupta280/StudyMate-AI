import streamlit as st
from components.sidebar import render_sidebar
from views.home import show as show_home
from views.upload import show as show_upload
from views.chat import show as show_chat
from views.quiz import show as show_quiz
from views.flashcards import show as show_flashcards

def load_css():
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()
render_sidebar()



# Temporary content


page = st.session_state.current_page

if page == "Home":
    show_home()

elif page == "Upload Notes":
    show_upload()

elif page == "AI Chat":
    show_chat()

elif page == "Quiz":
    show_quiz()

elif page == "Flashcards":
    show_flashcards()

