import streamlit as st

st.markdown("""
    <style>
        /* Rainbow gradient header styling */
        h2 {
            color: transparent !important;
            background-clip: text !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-image: linear-gradient(to right, rgb(255, 108, 108), rgb(255, 189, 69), rgb(255, 255, 194), rgb(92, 228, 136), rgb(61, 157, 243), rgb(178, 126, 255), rgb(109, 63, 192)) !important;
            font-weight: 700 !important;
            font-size: 2.5rem !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
        }
        
        /* Center divider */
        hr {
            margin: 1.5rem auto !important;
            max-width: 60% !important;
        }
        
        /* Center the fullscreen frame wrapper */
        [data-testid="stFullScreenFrame"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 2rem auto !important;
        }
        
        /* Center the emotion cache wrapper */
        .st-emotion-cache-p75nl5 {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 0 auto !important;
            width: auto !important;
            max-width: 200px !important;
        }
        
        /* Center the stImage wrapper */
        .stImage {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 200px !important;
        }
        
        /* Center the image container */
        div[data-testid="stImageContainer"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 200px !important;
            height: 200px !important;
        }
        
        /* Circular profile image */
        div[data-testid="stImageContainer"] img {
            border-radius: 50% !important;
            object-fit: cover !important;
            width: 200px !important;
            height: 200px !important;
            max-width: 200px !important;
            display: block !important;
        }
        
        /* Center text content with spacing */
        div[data-testid="stMarkdownContainer"] p {
            text-align: center !important;
            max-width: 600px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: 1rem !important;
            margin-bottom: 1rem !important;
        }
    </style>
    
""", unsafe_allow_html=True)

st.header("Introduction")
st.divider()

st.image("resource/profile.jpg")


st.write(
        "Hello! I am a computer science student, and I like to build something with 1s and 0s.\n"
)
st.write("Feel free to explore the different sections.")
