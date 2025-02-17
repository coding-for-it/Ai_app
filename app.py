import streamlit as st

# Configure page settings
st.set_page_config(page_title="AI Document Processor", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔍 Features")
st.sidebar.write("Navigate to different sections:")

# Define page navigation
selected_function = st.sidebar.radio(
    "Select Functionality:",
    [
        "🏠 Home",
        "📂 Upload PDF and Extract Text",
        "📑 Summarize Text",
        "🌎 Translate Text",
        "🖼️ Extract Images",
        "🔠 Transcribe Text",
        "🔍 Search & Analyze"
    ]
)

# --- Routing to Different Pages ---
if selected_function == "🏠 Home":
    try:
        from home import home_page
        home_page()  # Call function from home.py
    except ImportError:
        st.error("⚠️ Home module not found!")

elif selected_function == "📂 Upload PDF and Extract Text":
    try:
        from pdf_upload import pdf_upload_page
        pdf_upload_page()  # Call function from pdf_upload.py
    except ImportError:
        st.error("⚠️ PDF Upload module not found!")

elif selected_function == "📑 Summarize Text":
    try:
        from pdf_summarize import pdf_summarize_page
        pdf_summarize_page()  # Call function from pdf_summarize.py
    except ImportError:
        st.error("⚠️ Summarization module not found!")

elif selected_function == "🌎 Translate Text":
    try:
        from translate_text import translate_text_page
        translate_text_page()  # Call function from translate_text.py
    except ImportError:
        st.error("⚠️ Translate Text module not found!")

elif selected_function == "🖼️ Extract Images":
    try:
        from extract_images import extract_images_page
        extract_images_page()  # Call function from extract_images.py
    except ImportError:
        st.error("⚠️ Extract Images module not found!")

elif selected_function == "🔠 Transcribe Text":
    try:
        from transcribe_text import transcribe_text_page
        transcribe_text_page()  # Call function from transcribe_text.py
    except ImportError:
        st.error("⚠️ Transcribe Text module not found!")

elif selected_function == "🔍 Search & Analyze":
    try:
        from search_analyze import search_analyze_page
        search_analyze_page()  # Call function from search_analyze.py
    except ImportError:
        st.error("⚠️ Search & Analyze module not found!")

else:
    st.title(f"{selected_function} Functionality")
    st.write("🚀 This section will allow you to use various AI-based functionalities for document processing.")

# Footer
st.markdown("---")
st.write("💡 **Pro Tip:** Use the sidebar to navigate between features!")
