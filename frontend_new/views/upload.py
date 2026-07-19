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

             file_card(
                file.name,
                file.size / 1024,
                "Indexed"
        )