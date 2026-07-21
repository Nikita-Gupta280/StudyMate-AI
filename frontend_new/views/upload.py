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
   
    uploaded_files = st.file_uploader(
    "Upload Files",
    type=["pdf", "docx", "pptx", "txt"],
    accept_multiple_files=True,
    label_visibility="collapsed",
    )

   if uploaded_files:
      for file in uploaded_files:

         result = upload_file(file)

         st.success(result["message"])

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