import streamlit as st



st.header("Portfolio")
st.divider()




st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <p style='font-size: 1.1rem; color: #888;'>
            Showcasing my technical skills, projects, and continuous learning journey
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Skills & Technologies")

st.markdown("#### Programming Languages")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Python</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>JavaScript</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Java</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>C++</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>SQL</p>", unsafe_allow_html=True)

# Web Development
st.markdown("#### Web Development")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>HTML5</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>CSS3</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.svg", width=80)
        st.markdown("<p style='text-align: center;'>Streamlit</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>React</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Bootstrap</p>", unsafe_allow_html=True)

# Data Science & Tools
st.markdown("#### Data Science & Tools")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Git</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>GitHub</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Pandas</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>NumPy</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg", width=80)
        st.markdown("<p style='text-align: center;'>Jupyter</p>", unsafe_allow_html=True)

st.markdown("---")
st.caption("💡 Skill levels are self-assessed based on project experience and proficiency")
