import streamlit as st


def flashcard_settings():
    """
    Flashcard Settings Panel
    """

    st.subheader("⚙️ Flashcard Settings")

    st.write("")

    # -------------------------------------------------
    # File Selection
    # -------------------------------------------------

    selected_file = st.selectbox(
        "📄 Select Study Material",
        [
            "Physics.pdf",
            "Chemistry.pdf",
            "Biology.pdf",
            "Mathematics.pdf",
            "Computer Science.pdf",
        ],
    )

    st.write("")

    # -------------------------------------------------
    # Number of Cards
    # -------------------------------------------------

    number_of_cards = st.slider(
        "🗂 Number of Flashcards",
        min_value=5,
        max_value=50,
        value=10,
        step=5,
    )

    st.write("")

    # -------------------------------------------------
    # Difficulty
    # -------------------------------------------------

    difficulty = st.radio(
        "🎯 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard",
        ],
        horizontal=True,
    )

    st.write("")

    # -------------------------------------------------
    # Generate Button
    # -------------------------------------------------

    generate = st.button(
        "🚀 Generate Flashcards",
        use_container_width=True,
    )

    if generate:

        st.success("Flashcards generated successfully!")

        # Later this will call the backend.
        #
        # Example:
        #
        # response = backend.generate_flashcards(
        #       file=selected_file,
        #       difficulty=difficulty,
        #       count=number_of_cards
        # )
        #
        # st.session_state.flashcards["cards"] = response

    return {
        "file": selected_file,
        "difficulty": difficulty,
        "count": number_of_cards,
    }