Front Interface
import streamlit as st
from PyPDF2 import PdfReader

st.title("QA Bot - Document Based Question Answering")

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    document_text = ""
    for page in reader.pages:
        document_text += page.extract_text()
    
    st.write("Document uploaded successfully.")
    
    user_query = st.text_input("Enter your query:")

    if user_query:
        answer = generate_answer(document_text, user_query)  # Call backend function
        st.write(f"Answer: {answer}")
