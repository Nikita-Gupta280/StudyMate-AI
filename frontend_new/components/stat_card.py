import streamlit as st


def stat_card(title: str, value: str, delta: str):

    st.markdown(
        f"""
<div class="stat-card">
    <div class="stat-title">{title}</div>
    <div class="stat-value">{value}</div>
    <div class="stat-delta">▲ {delta}</div>
</div>
""",
        unsafe_allow_html=True,
    )