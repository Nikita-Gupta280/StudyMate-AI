import streamlit as st


def section_card(title: str):
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-card-title">
                {title}
            </div>
        """,
        unsafe_allow_html=True,
    )