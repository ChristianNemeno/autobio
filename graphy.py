import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Page:",
    ["Autobiography","Portfolio"]
)

if page == "Autobiography":
    st.write("Auto")
elif page == "Portfolio":
    st.write("Portfolio")
