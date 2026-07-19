import streamlit as st


def recent_activity(data):
    """
    Displays the user's recent learning activity.
    """

    st.subheader("🕒 Recent Activity")

    activities = data["recent_activity"]

    if not activities:
        st.info("No recent activity found.")
        return

    for activity in activities:

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"### {activity['title']}"
                )

                st.caption(activity["time"])

            with col2:

                if "Quiz" in activity["title"]:
                    st.markdown(
                        """
                        <div style="
                            font-size:40px;
                            text-align:center;
                        ">
                            📝
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                elif "Flashcard" in activity["title"]:
                    st.markdown(
                        """
                        <div style="
                            font-size:40px;
                            text-align:center;
                        ">
                            🧠
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                elif "Upload" in activity["title"]:

                    st.markdown(
                        """
                        <div style="
                            font-size:40px;
                            text-align:center;
                        ">
                            📄
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                else:

                    st.markdown(
                        """
                        <div style="
                            font-size:40px;
                            text-align:center;
                        ">
                            📌
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )