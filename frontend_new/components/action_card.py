import streamlit as st


def action_card(
    icon: str,
    title: str,
    description: str,
    page: str,
):
    """
    A reusable action card used on the Home page.
    """

    with st.container(border=True):

        st.markdown(f"## {icon}")

        st.markdown(f"### {title}")

        st.caption(description)

        st.write("")

        if st.button(
            "Open",
            key=f"open_{page}",
            use_container_width=True,
        ):
            st.session_state.current_page = page
            st.rerun()