import streamlit as st
import pdfplumber
from deep_translator import GoogleTranslator
from io import BytesIO

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extract_text() or ""
    return pdf_text

# Function for translating text into selected language
def translate_text(text, target_language):
    language_map = {
        "Hindi": "hi",
        "Marathi": "mr",
        "Tamil": "ta",
        "Telugu": "te",
        "Gujarati": "gu",
        "Bengali": "bn",
        "Kannada": "kn",
        "Punjabi": "pa",
        "French": "fr",
        "Spanish": "es"
    }
    target_code = language_map.get(target_language, "en")
    translator = GoogleTranslator(source='auto', target=target_code)
    return translator.translate(text)

# Function to create a downloadable file
def create_download_link(text, filename="translated_text.txt"):
    file_data = BytesIO()
    file_data.write(text.encode())
    file_data.seek(0)
    st.download_button(label="📥 Download Translated Text",
                        data=file_data,
                        file_name=filename,
                        mime="text/plain")

# Function to display Translation UI
def translate_text_page():
    st.title("🌎 Translate Text")
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], help="Upload a PDF to extract and translate text.")

    extracted_text = ""
    if uploaded_file is not None:
        st.success(f"✅ File Uploaded: {uploaded_file.name}")
        extracted_text = extract_text_from_pdf(uploaded_file)
        if not extracted_text.strip():
            st.warning("⚠ No text found in the PDF!")
    
    # Option to enter text manually
    st.markdown("*OR*")
    user_text = st.text_area("Enter text to translate:", height=150)
    
    # Select target language for translation
    target_language = st.selectbox("Select Target Language", [
        "Hindi", "Marathi", "Tamil", "Telugu", "Gujarati", "Bengali", "Kannada", "Punjabi", "French", "Spanish"
    ])

    # Translate the text into the selected language
    if st.button("🌍 Translate"):
        text_to_translate = user_text.strip() or extracted_text.strip()
        if text_to_translate:
            with st.spinner("Translating text..."):
                translated_text = translate_text(text_to_translate, target_language)
                st.subheader(f"📜 Translated Text in {target_language}:")
                st.write(translated_text)
                create_download_link(translated_text)
        else:
            st.warning("⚠ No text available to translate. Please enter text or upload a valid PDF.")