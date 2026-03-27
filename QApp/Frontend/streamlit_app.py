# QApp/Frontend/streamlit_app.py
import streamlit as st
from Backend.qa_service import answer_question
 
st.title("QApp - Simple Docker Demo")
question = st.text_input("Ask a question")
 
if st.button("Ask") and question.strip():
    st.success(answer_question(question))
