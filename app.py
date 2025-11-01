import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Assignment sa DAV",
    page_icon=":material/favorite:",
    layout="wide"
)



# pages
pages = [
    st.Page("preface.py", title="preface", icon=":material/account_circle:"),
    st.Page("page2.py", title="Projects", icon=":material/login:"),
    st.Page("page3.py", title="About me", icon=":material/login:")

]

pg = st.navigation(pages, position = "top")
pg.run()


