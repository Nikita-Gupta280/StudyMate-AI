import streamlit as st
from components.stat_card import stat_card

def progress_overview():
    
    col1, col2, col3 = st.columns(3)

    with col1:
     stat_card(
        "Study Streak",
        "7 Days",
        "+2"
    )

    with col2:
      stat_card(
        "Quizzes",
        "18",
        "+3"
    )

    with col3:
      stat_card(
        "Flashcards",
        "246",
        "+41"
    )