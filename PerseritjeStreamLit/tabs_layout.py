import streamlit as st

tab1, tab2, tab3, = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Content for Tab 1")
    st.write("This is the content of the first")