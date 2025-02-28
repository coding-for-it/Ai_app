import streamlit as st
import fitz  # PyMuPDF for PDF extraction
from transformers import pipeline

# Load the question-answering model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text("text")  # Extract text from each page
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text

# Streamlit UI Function
def qna_page():
    st.title("📖 Question & Answer from PDF/Text")

    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    text_input = st.text_area("Or type/paste your text here:", height=200)

    # Extract text from PDF if uploaded
    context = ""
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            context = extract_text_from_pdf(uploaded_file)
            if context:
                st.success("PDF text extracted successfully! ✅")
            else:
                st.warning("No text found in the uploaded PDF.")

    elif text_input:
        context = text_input

    # User enters a question
    question = st.text_input("Enter your question:")

    # Answer button
    if st.button("Get Answer"):
        if context and question:
            with st.spinner("Finding the answer..."):
                try:
                    result = qa_pipeline(question=question, context=context)
                    answer = result.get("answer", "No answer found.")
                    st.success(f"**Answer:** {answer}")
                except Exception as e:
                    st.error(f"Error processing question: {e}")
        else:
            st.warning("Please upload a PDF or enter text and ask a question.")
