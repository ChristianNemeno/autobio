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
        
        /* Add spacing between sections */
        .stMarkdown h5 {
            margin-top: 2rem !important;
            margin-bottom: 1.5rem !important;
        }
        
        /* Add spacing to containers */
        [data-testid="stVerticalBlock"] > div {
            margin-bottom: 1.5rem !important;
        }
        
        /* Add spacing to dividers */
        hr {
            margin-top: 2.5rem !important;
            margin-bottom: 2.5rem !important;
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

st.divider()
st.success("Currently a 3rd Year Computer Science student | Available for internship opportunities!")

st.divider()
st.markdown("#####  Connect with Me")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ChristianNemeno)")

with col2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/christian-nemeño-94a4972a5)")

with col3:
    st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](christiannemeno80@gmail.com)")



st.divider()
st.markdown("##### ⚡ Interests & Hobbies")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.markdown("**Gaming**")
        st.caption("Strategy & RPG games")

with col2:
    with st.container(border=True):

        st.markdown("**Coding**")
        st.caption("Building web apps")

with col3:
    with st.container(border=True):

        st.markdown("**Reading**")
        st.caption("Tech & sci-fi books")

with col4:
    with st.container(border=True):

        st.markdown("**Music**")
        st.caption("Lo-fi & instrumental")

st.divider()
st.markdown("##### Recent Achievements")

achievement_col1, achievement_col2, achievement_col3 = st.columns(3)

with achievement_col1:
    with st.container(border=True):
        st.markdown("#### Academic Excellence")
        st.write("**Dean's List**")
        st.caption("Semester 1-4, GWA 4.5 ++")
        st.progress(0.60, text="Achievement Level: 60%")

with achievement_col2:
    with st.container(border=True):
        st.markdown("#### 💡 Science Quiz bee")
        st.write("**Division level**")
        st.caption("Completed: October 2015")
        st.progress(1.0, text="Achievement Level: 100%")

with achievement_col3:
    with st.container(border=True):
        st.markdown("#### DOST JLSS scholar")
        st.write("**National level**")
        st.caption("Completed: October 2025")
        st.progress(1.0, text="Achievement Level: 100%")
