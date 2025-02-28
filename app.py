import streamlit as st

# Configure page settings
st.set_page_config(page_title="AI Document Processor", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔍 Features")
st.sidebar.write("Navigate to different sections:")
selected_function = st.sidebar.radio(
    "Select Functionality:",
    [
        "🏠 Home",
        "📂 Extract Text",
        "🌎 Translate Text",
        "🖼️ Extract Images",
        "📑 Summarize Text",
        "🔠 Transliteration Text",
        "❓ Question & Answer"
    ]
)

# --- Routing to Different Pages ---
if selected_function == "🏠 Home":
    try:
        from home import home_page
        home_page()  # Call function from home.py
    except ImportError:
        st.error("⚠️ Home module not found!")

elif selected_function == "📂 Extract Text":
    try:
        from document_upload import document_upload_page
        document_upload_page()  # Call function from extract_text.py
    except ImportError:
        st.error("⚠️ Extract Text module not found!")

elif selected_function == "📑 Summarize Text":
    try:
        from summarize_text import summarize_text_page
        summarize_text_page()  # Call function from summarize_text.py
    except ImportError:
        st.error("⚠️ Summarization module not found!")

elif selected_function == "🌎 Translate Text":
    try:
        from translate_text import translate_text_page
        translate_text_page()  # Call function from translate_text.py
    except ImportError:
        st.error("⚠️ Translation module not found!")

elif selected_function == "🖼️ Extract Images":
    try:
        from extract_images import extract_images_page
        extract_images_page()  # Call function from extract_images.py
    except ImportError:
        st.error("⚠️ Image extraction module not found!")

elif selected_function == "🔠 Transliteration Text":
    try:
        from transliteration import transliterate_page
        transliterate_page()  # Call function from transliteration.py
    except ImportError:
        st.error("⚠️ Transliteration module not found!")

elif selected_function == "❓ Question & Answer":
    try:
        from qna import qna_page
        qna_page()
    except ImportError:
        st.error("⚠️ Question & Answer module not found!")

else:
    st.title(f"{selected_function} Functionality")
    st.write("🚀 This section will allow you to use various AI-based functionalities for document processing.")

# Footer
st.markdown("---")
st.write("💡 **Pro Tip:** Use the sidebar to navigate between features!")
