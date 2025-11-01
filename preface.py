import streamlit as st

st.title("_Hate_ is a place where a man who can't stand :red[sadness] goes")

st.markdown("""
    <style>
        div[data-testid="stImageContainer"] img {
            border-radius: 50% !important;
            object-fit: cover !important;
            width: 200px !important;
            height: 200px !important;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("resource/profile.jpg")
