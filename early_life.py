import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

st.header("Early Life")

# Add CSS for scrollable column
st.markdown("""
    <style>
    /* Fit page content to viewport */
    section.main {
        padding-top: 1rem !important;
        padding-bottom: 0 !important;
    }
    
    div.stColumn:first-child div[data-testid="stVerticalBlock"] {
        max-height: calc(100vh - 200px) !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        padding-right: 10px;
    }
    
    /* Make containers compact and flexbox-like */
    div.stColumn:first-child div[data-testid="stLayoutWrapper"] {
        max-width: 250px !important;
        margin: 0 auto !important;
    }
    
    div.stColumn:first-child div[data-testid="stLayoutWrapper"] div[data-testid="stVerticalBlock"] {
        max-height: none !important;
        overflow: visible !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    
    div.stColumn:first-child div[data-testid="stVerticalBlock"]::-webkit-scrollbar {
        width: 8px;
    }
    
    div.stColumn:first-child div[data-testid="stVerticalBlock"]::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    div.stColumn:first-child div[data-testid="stVerticalBlock"]::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }
    
    div.stColumn:first-child div[data-testid="stVerticalBlock"]::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    
    /* Make card containers full width with padding */
    div.stColumn:first-child div[data-testid="stElementContainer"] {
        width: 100% !important;
        padding: 1rem !important;
        box-sizing: border-box !important;
    }
    
    /* Center content inside each card */
    div.stColumn:first-child div[data-testid="stElementContainer"] > div {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
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
            st.image("resource/grandmama.jpg", width=200)
            st.write("Matriarch of the family")
            st.caption("Generation: 1st")

        with st.container(border=True):
            st.image("resource/pops.jpg", width=200)
            st.write("Patriarch of the family")

        with st.container(border=True):
            st.image("resource/dad.jpg", width=200)
            st.write("My father")

        with st.container(border=True):
            st.image("resource/mom.jpg", width=200)
            st.write("My mother")

        with st.container(border=True):
            st.image("resource/me.jpg", width=200)
            st.write("Me")

        with st.container(border=True):
            st.image("resource/eldest.jpg", width=200)
            st.write("First sibling")

        with st.container(border=True):
            st.image("resource/middle.jpg", width=200)
            st.write("Second sibling")

        with st.container(border=True):
            st.image("resource/youngest.jpg", width=200)
            st.write("Third sibling")

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

        config = Config(height=graph_height,
                        directed=True,
                        physics=False,
                        hierarchical=True,
                        )


        agraph(nodes=nodes, edges=edges, config=config)
