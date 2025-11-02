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
        st.image("resource/dxd.jpg", use_container_width=False)

        st.markdown("#### Animedia REST API")
        st.write("Using the built in auth in django, and the Django REST framework dependency, I explored how django backend works, other details , I used JWT for user sessions and tokens (IDK WHY When i couldve just used django built in auth)")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)")
        with tech_col2:
            st.markdown("![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)")
        with tech_col3:
            st.markdown("![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)")

        st.caption(" Completed: October 2024")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Basic GET api  - Fetches data in database for anime information")
            st.write("• Basic POST api - Can make an anime record")
            st.write("• Basic Update and Delete - Delete and update anime record")

            st.markdown("**Challenges & Solutions:**")
            st.write("I hated Python type inference")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ChristianNemeno/animedia_api.git)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://youtube.com/shorts/KJbwEah5gQE?si=GRmmT-Y2Ec4AFC5h)")

with proj_col2:
    with st.container(border=True):
        st.image("resource/karenderya.png", use_container_width=True)

        st.markdown("#### Karenderya site")
        st.write("A react + vite prototype for a eatery")

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
            st.write("• Static website - predefined everything")
            st.write("• Can search using filter tools")
            st.write("• Navigation  - used react router dom")

            st.markdown("**Challenges & Solutions:**")
            st.write("React hooks lol")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ChristianNemeno/karenderia_ordering_site.git)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://youtube.com/shorts/KJbwEah5gQE?si=GRmmT-Y2Ec4AFC5h)")

proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.container(border=True):
        st.image("resource/rem.png", use_container_width=True)

        st.markdown("#### What Remains")
        st.write("A visual novel from scratch built using Java core, and JavaFX for UI")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=openjdk&logoColor=white)")
        with tech_col2:
            st.markdown("![JavaFX](https://camo.githubusercontent.com/74b3f60f771039c9f1d0426fab375fbb3855168361c03e49845937a44cc582fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a61766166782d2532334646303030302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6a6176616678266c6f676f436f6c6f723d7768697465)")
        with tech_col3:
            st.markdown("![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)")

        st.caption(" Completed: May 2025")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Flexible Save System ")
            st.write("• Dialogue Log ")
            st.write("• Auto-Play Mode ")

            st.markdown("**Challenges & Solutions:**")
            st.write("Design patterns , event system and state pattern")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BenJosephEscolano/CSIT228Capstone.git)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://youtube.com/shorts/KJbwEah5gQE?si=GRmmT-Y2Ec4AFC5h)")

with proj_col2:
    with st.container(border=True):
        st.image("resource/tapcet.png", use_container_width=True)

        st.markdown("#### TAPCET")
        st.write("TAPCET is basically a quiz app clone, with the goal of serving aspiring college scholars, with sets of review questions for the upcoming seasonal CETs")

        st.markdown("**Tech Stack:**")
        tech_col1, tech_col2, tech_col3 = st.columns(3)
        with tech_col1:
            st.markdown("![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=java&logoColor=white)")
        with tech_col2:
            st.markdown("![Spring](https://img.shields.io/badge/Spring-6DB33F?style=flat&logo=spring&logoColor=white)")
        with tech_col3:
            st.markdown("![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)")

        st.caption(" Ongoing: November 2025")

        with st.expander("▸ View Details"):
            st.markdown("**Key Features:**")
            st.write("• Quiz progress - Description")
            st.write("• Quiz category - Description")
            st.write("• Rapid review random - Description")

            st.markdown("**Challenges & Solutions:**")
            st.write("As a beginnner in java spring boot, dependency injection was quite confusing at first, hench this will be the last time ill be touching Java spring")

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername/project4)")
            with btn_col2:
                st.markdown("[![Demo](https://img.shields.io/badge/Live_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://youtube.com/shorts/KJbwEah5gQE?si=GRmmT-Y2Ec4AFC5h)")

st.markdown("---")

