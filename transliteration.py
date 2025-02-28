import streamlit as st
import pdfplumber
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Define supported Indian languages
INDIAN_LANGUAGES = {
    "Hindi": {"script": sanscript.DEVANAGARI},
    "Marathi": {"script": sanscript.DEVANAGARI},
    "Sanskrit": {"script": sanscript.DEVANAGARI},
    "Bengali": {"script": sanscript.BENGALI},
    "Gujarati": {"script": sanscript.GUJARATI},
    "Kannada": {"script": sanscript.KANNADA},
    "Malayalam": {"script": sanscript.MALAYALAM},
    "Punjabi": {"script": sanscript.GURMUKHI},
    "Tamil": {"script": sanscript.TAMIL},
    "Telugu": {"script": sanscript.TELUGU},
    "Odia": {"script": sanscript.ORIYA}
}

def transliterate_text(input_text, target_language):
    """Transliterates text into the selected Indian language."""
    if not input_text.strip():
        return "⚠️ No text provided for transliteration."
    
    script_type = INDIAN_LANGUAGES[target_language]["script"]
    
    try:
        return transliterate(input_text, sanscript.ITRANS, script_type)
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def extract_text_from_pdf(uploaded_file):
    """Extracts text from an uploaded PDF."""
    with pdfplumber.open(uploaded_file) as pdf:
        extracted_text = "".join([page.extract_text() or "" for page in pdf.pages])
    return extracted_text

def transliterate_page():
    """Streamlit page for transliteration."""
    st.title("🔠 Indian Language Transliterator")
    st.write("Transliterate text/PDF content into **11 Indian languages** accurately.")
    
    # Upload PDF
    uploaded_file = st.file_uploader("📂 Upload a PDF for Transliteration", type=["pdf"])
    extracted_text = ""
    if uploaded_file:
        st.success(f"✅ PDF Uploaded: {uploaded_file.name}")
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.text_area("📜 Extracted Text:", extracted_text, height=200)
    
    # User Input for Manual Text Transliteration
    input_text = st.text_area("✍️ Enter Text for Transliteration:", extracted_text, height=150)
    
    # Select Language for Transliteration
    target_language = st.selectbox("🎯 Choose Target Language:", list(INDIAN_LANGUAGES.keys()))
    
    # 🔄 Transliteration Button
    if st.button("🔄 Transliterate"):
        if input_text.strip():
            with st.spinner("Transliterating..."):
                output_text = transliterate_text(input_text, target_language)
                st.subheader("📜 Transliterated Text:")
                st.text_area("", output_text, height=200)
        else:
            st.warning("⚠️ Please enter or extract text before transliterating.")
    
    # 📥 Download Button
    if "output_text" in locals() and output_text:
        st.download_button(label="📥 Download Transliterated Text", data=output_text, file_name="transliterated_text.txt", mime="text/plain")
