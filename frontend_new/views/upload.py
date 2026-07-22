import streamlit as st
from components.file_card import file_card
from components.page_header import page_header
from utils.api import upload_file


def show():
  
   page_header(
    "📤 Upload Notes",
    "Upload PDFs, DOCX, PPTX and TXT files to unlock AI Chat, Quizzes and Flashcards."
    )

   st.divider()
   with st.container(border=True):
    st.markdown("### Upload Study Material")

    if "uploaded_files" not in st.session_state:
      st.session_state.uploaded_files = []
   
    uploaded_file = st.file_uploader(
    "Upload Files",
    type=["pdf", "docx", "pptx", "txt"],
    accept_multiple_files=False,
    label_visibility="collapsed",
    )

   if (
      uploaded_file
      and (
         "last_uploaded_file" not in st.session_state
         or st.session_state.last_uploaded_file != uploaded_file.name
      )
  ):
      file = uploaded_file
      st.write("Uploading...")
      result = upload_file(file)
      st.session_state.last_uploaded_file = file.name

      st.success(result["message"])

         # Reset previous quiz when a new PDF is uploaded
      if "quiz" in st.session_state:
         st.session_state.quiz = {
            "questions": [],
            "current": 0,
            "answers": {},
            "score": None,
            "submitted": False,
            "generated_quiz": None,
         }
      # Reset previous flashcards
      if "flashcards" in st.session_state:
         st.session_state.flashcards = {
            "generated": None
        }
      # Reset previous chat
      if "messages" in st.session_state:
         st.session_state.messages = []
         

         # Save file information in session
      st.session_state.uploaded_files = [
         {
            "name": file.name,
            "size": file.size / 1024,
         }
      ]

       # Show all uploaded files
   if st.session_state.uploaded_files:

      st.markdown("## 📚 Uploaded Files")

      for file in st.session_state.uploaded_files:

         file_card(
            file["name"],
            file["size"],
            "Indexed"
        )

      with st.container(border=True):

         st.markdown("### 🚀 Next Step")
         st.write("Your study material is ready. Start learning using any AI tool below.")

         col1, col2, col3 = st.columns(3)

         with col1:
            if st.button("💬 AI Chat", use_container_width=True):
               st.session_state.current_page = "AI Chat"
               st.rerun()

         with col2:
            if st.button("📝 Quiz", use_container_width=True):
               st.session_state.current_page = "Quiz"
               st.rerun()

         with col3:
            if st.button("🧠 Flashcards", use_container_width=True):
               st.session_state.current_page = "Flashcards"
               st.rerun()

   