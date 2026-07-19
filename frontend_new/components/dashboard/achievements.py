import streamlit as st

def achievements(data):
    st.subheader("🏆 Achievements")

    if not data["achievements"]:
        st.info("No achievements unlocked yet.")
        return

    cols = st.columns(2)

    for i, achievement in enumerate(data["achievements"]):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown("## 🏅")
                st.markdown(f"**{achievement}**")