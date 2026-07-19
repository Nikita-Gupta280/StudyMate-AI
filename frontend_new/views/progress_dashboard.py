import streamlit as st

from components.page_header import page_header

from components.dashboard.overview_metric_card import overview_metrics
from components.dashboard.study_streak import study_streak
from components.dashboard.weekly_progress import weekly_progress
from components.dashboard.quiz_performance import quiz_performance
from components.dashboard.flashcard_mastery import flashcard_mastery
from components.dashboard.recent_activity import recent_activity
from components.dashboard.achievements import achievements

from data.sample_dashboard_data import DASHBOARD_DATA


def show():

    # =====================================================
    # PAGE HEADER
    # =====================================================

    page_header(
        "📊 Progress Dashboard",
        "Track your learning progress, quiz performance, and study habits."
    )

    st.write("")

    # =====================================================
    # OVERVIEW METRICS
    # =====================================================

    overview_metrics(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # STUDY STREAK
    # =====================================================

    study_streak(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # WEEKLY PROGRESS
    # =====================================================

    weekly_progress(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # QUIZ PERFORMANCE
    # =====================================================

    quiz_performance(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # FLASHCARD MASTERY
    # =====================================================

    flashcard_mastery(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # RECENT ACTIVITY
    # =====================================================

    recent_activity(DASHBOARD_DATA)

    st.write("")
    st.divider()

    # =====================================================
    # ACHIEVEMENTS
    # =====================================================

    achievements(DASHBOARD_DATA)