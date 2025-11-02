import streamlit as st
import pandas as pd
import numpy as np
from streamlit_agraph import agraph, Node, Edge, Config
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

st.divider()
st.markdown("""
    <style>
    /* Add bottom padding to prevent footer overlap */
    .stTabs [data-baseweb="tab-panel"] {
        padding-bottom: 4rem !important;
    }
    
    /* Center all markdown text in first column */
    [data-testid="stColumn"]:first-child [data-testid="stMarkdown"] {
        text-align: center !important;
    }
    
    /* Center the layout wrapper containers that hold images */
    [data-testid="stColumn"]:first-child [data-testid="stLayoutWrapper"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* Center vertical blocks inside layout wrappers */
    [data-testid="stColumn"]:first-child [data-testid="stLayoutWrapper"] [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* Center element containers */
    [data-testid="stColumn"]:first-child [data-testid="stElementContainer"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* Center the stImage wrapper */
    [data-testid="stColumn"]:first-child .stImage {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* Center image container */
    [data-testid="stColumn"]:first-child [data-testid="stImageContainer"] {
        display: flex !important;
        justify-content: center !important;
        margin: 0 auto !important;
    }
    
    /* Add simple border to the graph canvas iframe */
    [data-testid="stCustomComponentV1"] {
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
    
    /* Make vis-network container responsive */
    .vis-network {
        width: 100% !important;
    }
    
    /* Make canvas fill container */
    .vis-network canvas {
        width: 100% !important;
        height: 100% !important;
    }
    
    /* Align metrics in tab2 to the left - Direct override */
    /* Remove centering from app.py for metrics */
    .stMetric,
    .stMetric * {
        text-align: left !important;
    }
    
    [data-testid="stMetric"] {
        align-items: flex-start !important;
    }
    
    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"] {
        justify-content: flex-start !important;
        align-items: flex-start !important;
    }
    
    /* Override emotion cache classes */
    .st-emotion-cache-1p09rwb,
    .st-emotion-cache-efbu8t,
    .st-emotion-cache-1q82h82,
    .st-emotion-cache-0,
    .st-emotion-cache-10klw3m {
        justify-content: flex-start !important;
        align-items: flex-start !important;
    }
    
    /* Override markdown centering inside metrics */
    [data-testid="stMetric"] [data-testid="stMarkdownContainer"],
    [data-testid="stMetric"] [data-testid="stMarkdownContainer"] p {
        text-align: left !important;
        justify-content: flex-start !important;
    }
    
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    
    /* Center images in tab3 education section */
    .stTabs [data-baseweb="tab-panel"] [data-testid="stVerticalBlock"] {
        text-align: center !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] .stImage {
        display: inline-block !important;   
        text-align: center !important;
    }
    
    /* Fixed height for family member containers in Tab 1 */
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] > div[data-testid="stVerticalBlock"] > div[data-testid="stLayoutWrapper"] {
        min-height: 280px !important;
    }
    
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] > div[data-testid="stVerticalBlock"] > div[data-testid="stLayoutWrapper"] > div[data-testid="stVerticalBlock"] {
        height: 280px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        padding: 1rem !important;
    }
    
    /* Left align metric content divs */
    [data-testid="stMetricLabel"] > div,
    [data-testid="stMetricValue"] > div {
        justify-content: flex-start !important;
        align-items: flex-start !important;
        text-align: left !important;
    }
        
    </style>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Family Tree", "Reside", "Education"])

with tab1:
    st.subheader("My Family Tree")

    st.markdown("---")
    st.markdown("##### Interactive Family Graph")

    with st.container(border=True):
        nodes = []
        edges = []

        nodes.append( Node(id="Grandma",
                           label="Grandma",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/grandmama.jpg")) )

        nodes.append( Node(id="Grandpa",
                           label="Grandpa",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/pops.jpg")) )

        nodes.append( Node(id="Dad",
                           label="Dad",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/dad.jpg")) )

        nodes.append( Node(id="Mom",
                           label="Mom",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/mom.jpg")) )

        nodes.append( Node(id="Me",
                           label="Me",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/me.jpg")) )

        nodes.append( Node(id="eldest",
                           label="Eldest",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/eldest.jpg")) )

        nodes.append( Node(id="middle",
                           label="Middle",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/middle.jpg")) )

        nodes.append( Node(id="erika",
                           label="Youngest",
                           size=35,
                           shape="circularImage",
                           image=get_base64_image("resource/youngest.jpg")) )

        edges.append( Edge(source="Grandma", target="Dad") )
        edges.append( Edge(source="Grandpa", target="Dad") )
        edges.append( Edge(source="Mom", target="erika") )
        edges.append( Edge(source="Mom", target="Dad") )
        edges.append( Edge(source="Mom", target="Me") )
        edges.append( Edge(source="Mom", target="eldest") )
        edges.append( Edge(source="Mom", target="middle") )

        graph_height = 550
        graph_width = 1000

        config = Config(width=graph_width,
                        height=graph_height,
                        directed=True,
                        physics=False,
                        hierarchical=True,
                        )

        agraph(nodes=nodes, edges=edges, config=config)

    st.markdown("---")
    st.markdown("##### Family Members")

    st.markdown("###### First Generation")
    gen1_col1, gen1_col2 = st.columns(2)

    with gen1_col1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/grandmama.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Grandma**")
            st.write("Matriarch of the family")
            st.caption("Generation: 1st")

    with gen1_col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/pops.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Grandpa**")
            st.write("Patriarch of the family")
            st.caption("Generation: 1st")

    st.markdown("###### Second Generation")
    gen2_col1, gen2_col2 = st.columns(2)

    with gen2_col1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/dad.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Dad**")
            st.write("My father")
            st.caption("Generation: 2nd")

    with gen2_col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/mom.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Mom**")
            st.write("My mother")
            st.caption("Generation: 2nd")

    st.markdown("###### Third Generation")
    gen3_col1, gen3_col2, gen3_col3, gen3_col4 = st.columns(4)

    with gen3_col1:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/me.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Me**")
            st.write("Myself")
            st.caption("Generation: 3rd")

    with gen3_col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/eldest.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Eldest**")
            st.write("First sibling")
            st.caption("Generation: 3rd")

    with gen3_col3:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/middle.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Middle**")
            st.write("Second sibling")
            st.caption("Generation: 3rd")

    with gen3_col4:
        with st.container(border=True):
            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/youngest.jpg").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Youngest**")
            st.write("Third sibling")
            st.caption("Generation: 3rd")



with tab2:
    st.subheader("A Profile: Born in Leyte")

    col1, col2 = st.columns([1, 2])

    with col1:
        with st.container(border=True):
            st.markdown("#### Key Info")
            st.metric("City", "Ormoc")
            st.metric("Province", "Leyte")
            st.metric("Born", "September 4, 2003")

        with st.container(border=True):
            st.markdown("#### About My Hometown")
            st.write("Ormoc City is a vibrant coastal city in Leyte, known for its rich culture and beautiful landscapes.")
            st.caption("Population: ~230,000 residents")
            st.caption("Known for: Pineapple production & scenic beaches")

    with col2:
        with st.container(border=True):
            st.markdown("#### My Birthplace: Ormoc")
            df = pd.DataFrame(
                {"lat": [11.004049], "lon": [124.614853]}
            )
            st.map(df, zoom=14, use_container_width=True)
            st.caption("Located in the heart of Leyte province")




with tab3:
    st.subheader("My Education Journey")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### Elementary")
            st.markdown("---")

            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/vscs.png").split(",")[1]),
                unsafe_allow_html=True
            )
            st.write("**Villaba South Central School**")
            st.caption("Years: 2009-2016")
            st.caption("Location: Villaba, Leyte")
            st.caption("Status: Completed")

    with col2:
        with st.container(border=True):
            st.markdown("### High School")
            st.markdown("---")

            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/pit.png").split(",")[1]),
                unsafe_allow_html=True
            )

            st.write("**Palompon Institute of Technology**")
            st.caption("Years: 2017-2022")
            st.caption("Location: Palompon, Leyte")
            st.caption("Status: Completed")

    with col3:
        with st.container(border=True):
            st.markdown("### College")
            st.markdown("---")

            st.markdown(
                """
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{}" width="120">
                </div>
                """.format(get_base64_image("resource/cit.png").split(",")[1]),
                unsafe_allow_html=True
            )

            st.write("**Cebu Institute of Technology**")
            st.caption("Years: 2023-Present")
            st.caption("Course: Computer Science")
            st.caption("Status: In Progress (Year 3)")

    st.markdown("---")
    st.markdown("##### Overall Education Progress")

    with st.container(border=True):
        st.progress(0.75, text="Educational Journey: 75% Complete")

        prog_col1, prog_col2, prog_col3 = st.columns(3)

        with prog_col1:
            st.metric("Years in School", "16 years")

        with prog_col2:
            st.metric("Current Level", "College Year 3")

        with prog_col3:
            st.metric("Expected Graduation", "2027")
