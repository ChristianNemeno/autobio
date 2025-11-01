import streamlit as st

st.title("_Welcome_ to my :red[domain]")
st.divider()
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

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image("resource/profile.jpg")
