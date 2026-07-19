import streamlit as st


def quiz_settings():
    st.markdown("### 📄 Select Study Material")
    selected_file = st.selectbox(
    "Choose uploaded notes",
    [
        "Physics.pdf",
        "Chemistry.pdf",
        "Biology.pdf"
    ]
)
    difficulty = st.radio(
    "Difficulty",
    ["Easy", "Medium", "Hard"],
    horizontal=True
)
    question_count = st.slider(
    "Number of Questions",
    min_value=5,
    max_value=20,
    value=10,
    step=5,
)
    generate = st.button(
    "🚀 Generate Quiz",
    use_container_width=True
)
    if generate:
      st.success("Quiz generation will be connected to the backend next.")