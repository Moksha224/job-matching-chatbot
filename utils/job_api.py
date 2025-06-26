import requests
import streamlit as st

def get_live_jobs(skill):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": skill, "page": "1", "num_pages": "1"}

    headers = {
        "X-RapidAPI-Key": st.secrets["RAPIDAPI_KEY"],  # ✅ Use secret
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        return []
