import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Assignment sa DAV",
    page_icon=":material/favorite:",
    layout="wide"
)

st.markdown("""
    <style>
    /* Lock main viewport - no page scrolling */
    html, body {
        overflow: hidden !important;
        height: 100vh !important;
        max-height: 100vh !important;
    }
    
    section[data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        max-height: 100vh !important;
    }
    
    section.main {
        overflow: hidden !important;
        max-height: 100vh !important;
    }
    
    /* Main content container - locked height */
    .stMainBlockContainer.block-container {
        max-height: calc(100vh - 3rem) !important;
        overflow: hidden !important;
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
    }
    
    /* Fixed Footer */
    .global-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(90deg, rgba(30, 30, 30, 0.95) 0%, rgba(50, 50, 50, 0.95) 100%);
        color: #e0e0e0;
        padding: 0.75rem 2rem;
        text-align: center;
        font-size: 0.875rem;
        z-index: 999;
        border-top: 2px solid rgba(100, 100, 100, 0.3);
        backdrop-filter: blur(10px);
    }
    
    .global-footer p {
        margin: 0;
        padding: 0;
    }
    
    .global-footer a {
        color: #4da6ff;
        text-decoration: none;
        margin: 0 0.5rem;
        transition: color 0.3s ease;
    }
    
    .global-footer a:hover {
        color: #80c1ff;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# pages
pages = [
    st.Page("intro.py", title="preface", icon=":material/account_circle:"),
    st.Page("early_life.py", title="early life", icon=":material/history:"),
    st.Page("page3.py", title="About me", icon=":material/login:")

]

pg = st.navigation(pages, position = "top")
pg.run()

# Global Footer
st.markdown("""
    <div class="global-footer">
        <p>© 2025 | Data Visualization Project - CS 3rd Year | Created with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)


