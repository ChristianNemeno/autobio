import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Header Nav App",
    page_icon="🧭",
    layout="wide"
)



# pages
pages = [
    st.Page("preface.py", title="Homee", icon=":material/login:"),
    st.Page("page2.py", title="Projects", icon=":material/login:"),
    st.Page("page3.py", title="About me", icon=":material/login:")

]

pg = st.navigation(pages, position = "top")
pg.run()


