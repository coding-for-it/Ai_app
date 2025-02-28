import streamlit as st

def home_page():
    # --- Home Page ---
    st.markdown("""
        <style>
            .main-title {
                font-size: 36px;
                font-weight: bold;
                color: #2c3e50;
                text-align: center;
            }
            .sub-title {
                font-size: 22px;
                color: #7f8c8d;
                text-align: center;
            }
            .feature-box {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                text-align: center;
            }
            .feature-box h3 {
                color: #3498db;
                font-size: 20px;
            }
            .feature-box p {
                font-size: 16px;
                color: #7f8c8d;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main title
    st.markdown('<h1 class="main-title">📄 AI Document Processor</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">An AI-powered tool to process, analyze, and extract insights from documents.</h2>', unsafe_allow_html=True)

    # Features Section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="feature-box">
                <h3>📂 Upload PDF and Extract Text</h3>
                <p>Easily upload PDFs and extract data for further analysis.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="feature-box">
                <h3>📑 Summarize Extracted Text</h3>
                <p>Generate concise summaries using AI-based summarization.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-box">
                <h3>🌎 Translate Text</h3>
                <p>Translate extracted text into multiple languages with ease.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="feature-box">
                <h3>🖼️ Extract Images</h3>
                <p>Automatically extract images from PDF documents.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-box">
                <h3>🔍 Search & Analyze</h3>
                <p>Search, highlight, and analyze important keywords.</p>
            </div>
        """, unsafe_allow_html=True)

