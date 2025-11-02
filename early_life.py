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
    /* Tab content container - constrain height but allow internal scrolling */
    .stTabs [data-baseweb="tab-panel"] {
        max-height: calc(100vh - 15rem) !important;
        overflow: visible !important;
    }

    /* Horizontal block (columns container) - fixed height with margin for footer */
    [data-testid="stHorizontalBlock"] {
        max-height: calc(100vh - 20rem) !important;
        margin-bottom: 5rem !important;
        padding-bottom: 2rem !important;
    }

    /* Each column scrolls independently */
    [data-testid="stColumn"] {
        max-height: calc(100vh - 20rem) !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        padding-right: 0.5rem !important;
    }

    /* Custom scrollbar styling */
    [data-testid="stColumn"]::-webkit-scrollbar {
        width: 8px;
    }

    [data-testid="stColumn"]::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }

    [data-testid="stColumn"]::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }

    [data-testid="stColumn"]::-webkit-scrollbar-thumb:hover {
        background: #555;
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

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("##### Family Members")

        with st.container(border=True):
            st.image("resource/grandmama.jpg", width=120)
            st.write("**Grandma**")

        with st.container(border=True):
            st.image("resource/pops.jpg", width=120)
            st.write("**Grandpa**")

        with st.container(border=True):
            st.image("resource/dad.jpg", width=120)
            st.write("**Dad**")

        with st.container(border=True):
            st.image("resource/mom.jpg", width=120)
            st.write("**Mom**")
            st.write("My mother")

        with st.container(border=True):
            st.image("resource/me.jpg", width=120)
            st.write("**Me**")

        with st.container(border=True):
            st.image("resource/eldest.jpg", width=120)
            st.write("**Eldest**")

        with st.container(border=True):
            st.image("resource/middle.jpg", width=120)
            st.write("**Middle**")

        with st.container(border=True):
            st.image("resource/youngest.jpg", width=120)
            st.write("**Youngest**")

    with col2:
        st.markdown("##### Interactive Family Graph")

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

        # Create the edges (relationships)
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


with tab2:
    st.subheader("Born in Leyte")

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.container(border=True):
            st.metric("City", "Ormoc")
            st.metric("Province", "Leyte")
            st.metric("Born", "September 4, 2003")

    with col2:
        with st.container(border=True):
            st.header("My Birthplace: Ormoc")
            df = pd.DataFrame(
                {"lat": [11.004049], "lon": [124.614853]}
            )
            st.map(df, zoom=14, use_container_width=True)


with tab3:
    st.subheader("My Education Journey")

    # Three columns for education levels
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### Elementary")
            st.markdown("---")

            st.image("resource/vscs.png", width=200)
            st.write("**Villaba South Central School**")
            st.caption("Years: 2009-2016")
            st.caption("Location: Leyte")
            st.metric("Status", "Completed", "100%")

    with col2:
        with st.container(border=True):
            st.markdown("### High School")
            st.markdown("---")
            st.image("resource/pit.png", width=200)
            st.write("**Palompon Institute of Technology**")
            st.caption("Years: 2017-2022")
            st.caption("Location: Leyte")
            st.metric("Status", "Completed", "100%")

    with col3:
        with st.container(border=True):
            st.markdown("### College")
            st.markdown("---")
            st.image("resource/cit.png", width=200)
            st.write("**Cebu Institute of Technology**")
            st.caption("Years: 2023-Present")
            st.caption("Course: Computer Science")
            st.metric("Status", "In Progress", "75%")

    st.markdown("---")
    st.markdown("##### 📊 Overall Education Progress")

    with st.container(border=True):
        st.progress(0.75, text="Educational Journey: 75% Complete")

        prog_col1, prog_col2, prog_col3 = st.columns(3)

        with prog_col1:
            st.metric("Years in School", "16", "+3 years")

        with prog_col2:
            st.metric("Current Level", "College", "Year 3")

        with prog_col3:
            st.metric("Expected Graduation", "2025", "1 year remaining")
