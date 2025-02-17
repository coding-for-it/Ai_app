import streamlit as st
import pdfplumber
from transformers import pipeline

# Load Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150):
    """Summarizes the given text using a transformer model."""
    if not text.strip():
        return "No text available for summarization."
    
    try:
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Error in summarization: {str(e)}"

def pdf_summarize_page():
    st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>📑 Summarize PDF</h1>", unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], help="Upload a PDF to extract and summarize text.")

    if uploaded_file is not None:
        st.success(f"✅ File Uploaded: {uploaded_file.name}")
        
        # Extract text from PDF using pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            pdf_text = ""
            for page in pdf.pages:
                pdf_text += page.extract_text() or ""
        
        # Display extracted text with preserved formatting
        st.text_area("Extracted Text:", pdf_text, height=300)

        # Summarize entire PDF
        if st.button("🔍 Summarize Entire PDF"):
            with st.spinner("Summarizing entire document..."):
                summary = summarize_text(pdf_text, max_length=300)
                st.subheader("📜 Summarized Text:")
                st.write(summary)

        # Summarize selected text
        selected_text = st.text_area("🔎 Paste or Select Text for Summarization:", "", height=150)
        
        if st.button("✂️ Summarize Selected Text"):
            if selected_text.strip():
                with st.spinner("Summarizing selected text..."):
                    summary = summarize_text(selected_text, max_length=150)
                    st.subheader("📜 Summarized Text:")
                    st.write(summary)
            else:
                st.warning("⚠️ Please enter or select some text to summarize.")

    # NEW: Additional text summarization for any user input
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>📝 Summarize Any Text</h2>", unsafe_allow_html=True)

    user_text = st.text_area("Enter any text to summarize:", "", height=200)

    if st.button("📌 Summarize Text"):
        if user_text.strip():
            with st.spinner("Summarizing text..."):
                summary = summarize_text(user_text, max_length=200)
                st.subheader("📜 Summarized Text:")
                st.write(summary)
        else:
            st.warning("⚠️ Please enter text to summarize.")

# Prevent script from running on import
if __name__ == "__main__":
    pdf_summarize_page()
