import streamlit as st


def overview_metrics(data):
    """
    Displays the top overview metrics for the dashboard.
    """

    st.subheader("📈 Overview")

    study_time = data["study_time_today"]
    streak = data["study_streak"]
    average_score = data["average_score"]
    cards_mastered = data["cards_mastered"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📚 Study Today",
            value=f"{study_time} min"
        )

    with col2:
        st.metric(
            label="🔥 Study Streak",
            value=f"{streak} Days"
        )

    with col3:
        st.metric(
            label="📝 Avg Quiz Score",
            value=f"{average_score}%"
        )

    with col4:
        st.metric(
            label="🧠 Cards Mastered",
            value=cards_mastered
        )