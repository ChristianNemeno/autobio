import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

st.header("Early Life")

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["👨‍👩‍👧‍👦 Family Tree", "📸 Memories", "📅 Timeline"])

with tab1:
    st.subheader("My Family Tree")

    nodes = []
    edges = []

    # Create the nodes (people)
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

    # 1. Build the config
    config = Config(height=600,
                    directed=True, # Shows the direction of the relationship
                    physics=False,
                    hierarchical=True, # This is the key!
                    )

    # 2. Render the graph (full width)
    agraph(nodes=nodes, edges=edges, config=config)

with tab2:
    st.subheader("Childhood Memories")
    st.write("Coming soon: Photos and stories from my childhood...")
    # Add your childhood photos/memories here
    # Example: st.image("resource/childhood.jpg", caption="My first day at school")

with tab3:
    st.subheader("Life Timeline")
    st.write("Coming soon: Key milestones and events...")
    # Add your timeline content here
    # Example:
    # st.write("🎂 2003 - Born")
    # st.write("📚 2009 - Started elementary school")

