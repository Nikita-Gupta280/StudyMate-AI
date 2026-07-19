import streamlit as st

def hero(title, subtitle):
    with st.container(border=True):
        st.title(title)
        st.markdown(subtitle)