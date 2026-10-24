import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

st.header("Add a Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value= 0, max_value= 50, value= 0)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post("http://localhost:8000/developer/", json=dev_data)
    st.json(response.json())

st.header("Add a Project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project Description")
proj_langs = st.text_input("Languages Used (Comma-separated)")
lead_dev_name = st.number_input("Lead Developer Name ")
lead_dev_exp = st.number_input("Lead Developer Experience (Years)", min_value = 0, max_value = 50, value = 0)

if st.button("Create Project"):
    dev_data = {"name": lead_dev_name, "experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "languages": proj_langs,
        "lead_developer": lead_dev_data
    }
    response = requests.post("http://localhost:8000/project/", json=proj_data)
    st.json(response.json())


st.header("Project Dashboard")

if st.button("Get Projects"):
    response = response.get("http://localhost:8000/projects")
    proj_data = response.json()['projects']

    if proj_data:
        proj_df = 


