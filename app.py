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
    .stMainBlockContainer.block-container {
        max-height: 100vh !important;
        overflow: hidden !important;
        padding-bottom: 0 !important;
        padding-top: 4rem !important;
    }
    
    
    .stMainBlockContainer div[data-testid="stVerticalBlock"] {
        max-height: 100vh !important;
        overflow-y: hidden !important;
    }
    
    /* Fix the app container */
    section[data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        max-height: 100vh !important;
    }
    
    /* Hide body scrollbar */
    html, body {
        overflow: hidden !important;
        height: 100vh !important;
        max-height: 100vh !important;
    }
    
    /* Fix main section */
    section.main {
        overflow: hidden !important;
        max-height: 100vh !important;
        padding-bottom: 0 !important;
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


