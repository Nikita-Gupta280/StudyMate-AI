import streamlit as st
import plotly.graph_objects as go


def quiz_performance(data):
    """
    Displays quiz performance analytics.
    """

    st.subheader("📝 Quiz Performance")

    quiz_data = data["quiz_scores"]

    quizzes = [item[0] for item in quiz_data]
    scores = [item[1] for item in quiz_data]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=quizzes,
            y=scores,
            text=scores,
            textposition="outside",
            name="Quiz Score",
        )
    )

    fig.update_layout(
        title="Quiz Scores",
        xaxis_title="Quiz",
        yaxis_title="Score (%)",
        yaxis=dict(range=[0, 100]),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=False,
        template="plotly_dark",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    highest = max(scores)
    lowest = min(scores)
    average = round(sum(scores) / len(scores), 1)

    highest_quiz = quizzes[scores.index(highest)]
    lowest_quiz = quizzes[scores.index(lowest)]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🏆 Highest Score",
            value=f"{highest}%",
            delta=highest_quiz,
        )

    with col2:
        st.metric(
            label="📉 Lowest Score",
            value=f"{lowest}%",
            delta=lowest_quiz,
            delta_color="inverse",
        )

    with col3:
        st.metric(
            label="📊 Average Score",
            value=f"{average}%",
        )

    st.write("")

    if average >= 90:
        st.success("🌟 Outstanding performance! Keep it up.")
    elif average >= 75:
        st.info("👍 Good work! You're making solid progress.")
    elif average >= 60:
        st.warning("📚 You're improving. Review weaker topics for better scores.")
    else:
        st.error("💡 Spend more time reviewing before attempting the next quiz.")