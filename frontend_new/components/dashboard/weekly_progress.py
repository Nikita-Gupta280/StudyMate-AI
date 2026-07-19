import streamlit as st
import plotly.graph_objects as go


def weekly_progress(data):
    """
    Displays the weekly study progress chart.
    """

    st.subheader("📈 Weekly Study Progress")

    weekly_data = data["weekly_progress"]

    days = [item[0] for item in weekly_data]
    minutes = [item[1] for item in weekly_data]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=days,
            y=minutes,
            mode="lines+markers",
            line=dict(width=3),
            marker=dict(size=10),
            name="Study Time"
        )
    )

    fig.update_layout(
        title="Study Minutes This Week",
        xaxis_title="Day",
        yaxis_title="Minutes",
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=False,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    total_minutes = sum(minutes)
    average_minutes = round(total_minutes / len(minutes), 1)
    best_day = days[minutes.index(max(minutes))]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📚 Total Study Time",
            f"{total_minutes} min"
        )

    with col2:
        st.metric(
            "📊 Daily Average",
            f"{average_minutes} min"
        )

    with col3:
        st.metric(
            "🏆 Best Day",
            best_day
        )