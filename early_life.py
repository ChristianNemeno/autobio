import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

st.header("My Family Tree (Interactive)")

nodes = []
edges = []

# Create the nodes (people)
nodes.append( Node(id="Grandma", 
                   label="Grandma", 
                   size=25, 
                   shape="circularImage", 
                   image=get_base64_image("resource/grandmama.jpg")) )

nodes.append( Node(id="Mom", 
                   label="Mom", 
                   size=25,
                   shape="circularImage",
                   image=get_base64_image("resource/mom.jpg")) )

nodes.append( Node(id="Me", 
                   label="Me", 
                   size=25,
                   shape="circularImage",
                   image=get_base64_image("resource/me.jpg")) )

nodes.append( Node(id="Dad",
                   label="Dad",
                   size=25,
                   shape="circularImage",
                   image=get_base64_image("resource/dad.jpg")) )

# Create the edges (relationships)
edges.append( Edge(source="Grandma", target="Mom") )
edges.append( Edge(source="Mom", target="Me") )

# 1. Build the config
config = Config(width=500,
                height=500,
                directed=True, # Shows the direction of the relationship
                physics=False, 
                hierarchical=True, # This is the key!
                )

# 2. Render the graph
agraph(nodes=nodes, edges=edges, config=config)