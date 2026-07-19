import streamlit as st


def card(title: str, description: str):
    """
    Render a reusable card.
    """

    with st.container(border=True):

        st.markdown(f"### {title}")

        st.caption(description)