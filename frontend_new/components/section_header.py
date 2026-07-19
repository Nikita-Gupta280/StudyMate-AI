import streamlit as st


def section_header(title: str, subtitle: str = ""):
    """
    Display a consistent section heading across the application.
    """

    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)

    st.divider()