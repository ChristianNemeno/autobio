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
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Python</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>JavaScript</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Java</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>C++</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>SQL</p>", unsafe_allow_html=True)

# Web Development
st.markdown("#### Web Development")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>HTML5</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>CSS3</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Streamlit</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>React</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Bootstrap</p>", unsafe_allow_html=True)

# Data Science & Tools
st.markdown("#### Data Science & Tools")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Git</p>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>GitHub</p>", unsafe_allow_html=True)

with col3:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Pandas</p>", unsafe_allow_html=True)

with col4:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>NumPy</p>", unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="80">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center;'>Jupyter</p>", unsafe_allow_html=True)

st.markdown("---")
st.caption(" Skill levels are self-assessed based on project experience and proficiency")

st.markdown("---")
st.markdown("### Featured Projects")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.container(border=True):
        st.image("https://via.placeholder.com/400x250.png?text=Project+1+Screenshot", use_container_width=True)

        st.markdown("#### Project Title 1")
        st.write("Brief description of your project. Explain what it does, the problem it solves, and key features implemented.")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)")
        with tech_col2:
            st.markdown("![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)")
        with tech_col3:
            st.markdown("![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)")

        st.caption(" Completed: October 2024")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Feature 1 - Description")
            st.write("• Feature 2 - Description")
            st.write("• Feature 3 - Description")

            st.markdown("**Challenges & Solutions:**")
            st.write("Describe a technical challenge you faced and how you solved it.")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/project1)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-demo-link.com)")

with proj_col2:
    with st.container(border=True):
        st.image("https://via.placeholder.com/400x250.png?text=Project+2+Screenshot", use_container_width=True)

        st.markdown("#### Project Title 2")
        st.write("Brief description of your second project. Highlight what makes this project unique or interesting.")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)")
        with tech_col2:
            st.markdown("![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)")
        with tech_col3:
            st.markdown("![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)")

        st.caption(" Completed: September 2024")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Feature 1 - Description")
            st.write("• Feature 2 - Description")
            st.write("• Feature 3 - Description")

            st.markdown("**Challenges & Solutions:**")
            st.write("Describe a technical challenge you faced and how you solved it.")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/project2)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-demo-link.com)")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.container(border=True):
        st.image("https://via.placeholder.com/400x250.png?text=Project+3+Screenshot", use_container_width=True)

        st.markdown("#### Project Title 3")
        st.write("Brief description of your third project. Mention any awards or recognition if applicable.")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)")
        with tech_col2:
            st.markdown("![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)")
        with tech_col3:
            st.markdown("![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)")

        st.caption(" Completed: August 2024")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Feature 1 - Description")
            st.write("• Feature 2 - Description")
            st.write("• Feature 3 - Description")

            st.markdown("**Challenges & Solutions:**")
            st.write("Describe a technical challenge you faced and how you solved it.")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/project3)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-demo-link.com)")

with proj_col2:
    with st.container(border=True):
        st.image("https://via.placeholder.com/400x250.png?text=Project+4+Screenshot", use_container_width=True)

        st.markdown("#### Project Title 4")
        st.write("Brief description of your fourth project. Explain the impact or results achieved.")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=java&logoColor=white)")
        with tech_col2:
            st.markdown("![Spring](https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=spring&logoColor=white)")
        with tech_col3:
            st.markdown("![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)")

        st.caption("📅 Completed: July 2024")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Feature 1 - Description")
            st.write("• Feature 2 - Description")
            st.write("• Feature 3 - Description")

            st.markdown("**Challenges & Solutions:**")
            st.write("Describe a technical challenge you faced and how you solved it.")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/project4)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-demo-link.com)")

st.markdown("---")

