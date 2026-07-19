import streamlit as st


def file_card(filename: str, size_kb: float, status: str = "Ready"):
    col1, col2 = st.columns([6, 1])

    with col1:
        st.markdown(f"### 📄 {filename}")
        st.caption(f"{size_kb:.1f} KB")

    with col2:
        if status == "Ready":
            st.success("Ready")
        elif status == "Processing":
            st.warning("Processing")
        else:
            st.error(status)

    st.divider()