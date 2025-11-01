import streamlit as st

st.markdown("""
    <style>
        h2 {
            color: transparent !important;
            background-clip: text !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-image: linear-gradient(to right, rgb(255, 108, 108), rgb(255, 189, 69), rgb(255, 255, 194), rgb(92, 228, 136), rgb(61, 157, 243), rgb(178, 126, 255), rgb(109, 63, 192)) !important;
            text-align: center !important;
            font-weight: 700 !important;
            font-size: 2.5rem !important;
        }
        
        div[data-testid="stImageContainer"] img {
            border-radius: 50% !important;
            object-fit: cover !important;
            width: 200px !important;
            height: 200px !important;
        }
        
        div[data-testid="stMarkdownContainer"] p {
            text-align: center !important;
        }
    </style>
    
""", unsafe_allow_html=True)

st.header("Introduction")
st.divider()

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image("resource/profile.jpg")



st.write(
        "Hello! I am a computer science student, and I like to build something with 1s and 0s.\n"
)
st.write("Feel free to explore the different sections.")
