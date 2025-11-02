import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

st.header("Early Life")

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
        
    </style>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Family Tree", "Memories", "Timeline"])

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
