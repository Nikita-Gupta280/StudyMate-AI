import streamlit as st


def recent_files():
    """Display the user's recent uploaded files."""

    uploaded_files = st.session_state.get("uploaded_files", [])

    if not uploaded_files:
        st.info("""
### 📁 **Ready to start learning?**

Upload your first PDF, lecture notes, or study material to unlock all AI-powered study tools.

**Once your notes are uploaded, you can:**

- 💬 Chat with your notes
- 📝 Generate AI-powered quizzes
- 🧠 Create flashcards for revision
""")

        st.caption("💡 **One PDF is supported at a time**. Uploading a new PDF automatically replaces the previous one.")
    
        if st.button("📁 Upload Notes", key="empty_upload"):
            st.session_state.current_page = "Upload Notes"
            st.rerun()

        return

    st.success("### ✅ Current Uploaded PDF")

    file = uploaded_files[0]

    st.markdown(f"""
    **📄 {file['name']}**

    📦 Size: **{file['size']:.1f} KB**

    Ready for:

    - 💬 AI Chat
    - 📝 Quiz Generator
    - 🧠 Flashcards
    """)