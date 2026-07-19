import streamlit as st
import plotly.graph_objects as go


def flashcard_mastery(data):
    """
    Displays flashcard mastery analytics.
    """

    st.subheader("🧠 Flashcard Mastery")

    flashcards = data["flashcards"]

    known = flashcards["known"]
    review = flashcards["review"]

    total = known + review

    mastery = round((known / total) * 100) if total else 0

    # ---------------------------------------------------
    # Donut Chart
    # ---------------------------------------------------

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Known", "Review"],
                values=[known, review],
                hole=0.6,
                textinfo="label+percent",
            )
        ]
    )

    fig.update_layout(
        title="Flashcard Learning Status",
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        template="plotly_dark",
        showlegend=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    # ---------------------------------------------------
    # Statistics
    # ---------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "✅ Mastered",
            known,
        )

    with col2:
        st.metric(
            "🔁 Need Review",
            review,
        )

    with col3:
        st.metric(
            "🎯 Mastery",
            f"{mastery}%",
        )

    st.write("")

    # ---------------------------------------------------
    # Recommendation
    # ---------------------------------------------------

    if mastery >= 90:
        st.success(
            "🌟 Excellent! You've mastered almost all your flashcards."
        )

    elif mastery >= 75:
        st.info(
            "👍 Good progress! Review a few remaining cards to strengthen your memory."
        )

    elif mastery >= 50:
        st.warning(
            "📚 You're halfway there. Spend some time reviewing difficult cards."
        )

    else:
        st.error(
            "💡 Focus on reviewing your flashcards regularly to improve retention."
        )