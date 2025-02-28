import streamlit as st
import pdfplumber
import docx
from transformers import pipeline
import os

# Load summarization model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = "".join(page.extract_text() or "" for page in pdf.pages)
    return text

# Extract text from DOCX
def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])

# Summarize text
def summarize_text(text):
    summarizer = load_summarizer()
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Streamlit UI
def summarize_text_page():
    st.markdown("""
        <h1 style='text-align: center; color: #4F8BF9;'>📑 Text Summarization</h1>
    """, unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.file_uploader("Upload a text document (PDF/DOCX)", type=["pdf", "docx"], help="Supported formats: .pdf, .docx")
    
    # Text input box
    user_input_text = st.text_area("Or paste text below for summarization:", "", height=200)
    
    extracted_text = ""
    if uploaded_file is not None:
        st.success(f"File Uploaded Successfully: {uploaded_file.name}")
        
        # Extract text
        if uploaded_file.name.endswith(".pdf"):
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            extracted_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format!")
            return

    # Use extracted text if file uploaded, otherwise use user input
    final_text = extracted_text if extracted_text else user_input_text

    if final_text.strip():
        # Summarize text
        summarized_text = summarize_text(final_text)
        
        # Display summarized text
        st.subheader("📝 Summarized Text:")
        st.write(summarized_text)
        
        # Download button
        st.download_button(
            label="💾 Download Summarized Text",
            data=summarized_text,
            file_name="summarized_text.txt",
            mime="text/plain"
        )
    else:
        st.info("Please upload a file or paste text for summarization.")

if __name__ == "__main__":
    summarize_text_page()
