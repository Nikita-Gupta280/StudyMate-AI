import streamlit as st


def flashcard_navigation(current: int, total: int):
    """
    Flashcard Navigation Component

    Returns
    -------
    str | None

    previous
    next
    known
    review
    """

    st.divider()

    # --------------------------------------------------------
    # Progress Information
    # --------------------------------------------------------

    st.caption(f"Card {current + 1} of {total}")

    st.write("")

    # --------------------------------------------------------
    # Row 1
    # Previous / Next
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            use_container_width=True,
            disabled=current == 0,
        ):
            return "previous"

    with col2:

        if st.button(
            "Next ➡",
            use_container_width=True,
            disabled=current == total - 1,
        ):
            return "next"

    st.write("")

    # --------------------------------------------------------
    # Row 2
    # Known / Review
    # --------------------------------------------------------

    col3, col4 = st.columns(2)

    with col3:

        if st.button(
            "✅ I Know This",
            use_container_width=True,
            type="primary",
        ):
            return "known"

    with col4:

        if st.button(
            "🔁 Review Again",
            use_container_width=True,
        ):
            return "review"

    return None