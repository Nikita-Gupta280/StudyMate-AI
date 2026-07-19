import streamlit as st


def study_streak(data):
    """
    Displays the user's current study streak.
    """

    streak = data["study_streak"]

    st.subheader("🔥 Study Streak")

    with st.container(border=True):

        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown(
                f"""
                <div style="
                    font-size:70px;
                    text-align:center;
                ">
                    🔥
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:

            st.markdown("### Current Streak")

            st.markdown(
                f"""
                <h1 style="margin-bottom:0;">
                    {streak} Days
                </h1>
                """,
                unsafe_allow_html=True,
            )

            st.caption(
                "Keep studying every day to maintain your streak."
            )

            # -----------------------------------------
            # Progress towards next milestone
            # -----------------------------------------

            next_milestone = ((streak // 10) + 1) * 10

            progress = streak / next_milestone

            st.progress(progress)

            st.caption(
                f"Next milestone: {next_milestone} Days"
            )