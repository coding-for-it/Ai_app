import streamlit as st
import pdfplumber

def pdf_upload_page():

    # Title with a styled header
    st.markdown("""
        <h1 style='text-align: center; color: #4F8BF9;'>📄 PDF Upload and Viewer</h1>
    """, unsafe_allow_html=True)

    # Introduction text
    st.write("Upload a PDF file to view its content.")

    # File uploader with a card-like container
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], help="Supported format: .pdf")

    # Process and display the PDF content if a file is uploaded
    if uploaded_file is not None:
        st.success(f"File Uploaded Successfully: {uploaded_file.name}")
        
        # Extract text from the PDF using pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            pdf_text = ""
            for page in pdf.pages:
                pdf_text += page.extract_text() or ""
        
        # Display extracted text inside a nicely styled text area
        st.text_area("Extracted Text from PDF:", pdf_text, height=300, help="Scroll to read the full content.")

        # Download button for the extracted text
        st.download_button(
            label="Download Extracted Text",
            data=pdf_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
