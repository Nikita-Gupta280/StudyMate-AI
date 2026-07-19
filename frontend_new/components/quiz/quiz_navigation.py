import streamlit as st


def quiz_navigation(current: int, total: int):
    """
    Displays Previous / Next / Submit navigation.

    Returns
    -------
    str
        One of:
        "previous"
        "next"
        "submit"
        None
    """

    left, spacer, right = st.columns([1, 4, 1])

    action = None

    # Previous Button
    with left:
        if current > 0:
            if st.button("⬅ Previous", use_container_width=True):
                action = "previous"

    # Next or Submit Button
    with right:
        if current < total - 1:
            if st.button("Next ➡", use_container_width=True):
                action = "next"
        else:
            if st.button("✅ Submit Quiz", use_container_width=True):
                action = "submit"

    return action