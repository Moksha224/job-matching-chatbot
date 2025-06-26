import streamlit as st
import json
from utils.resume_parser import extract_text_from_pdf
from utils.matcher import extract_skills, match_jobs, highlight_matches

st.set_page_config(page_title="Job Matching Chatbot", layout="centered")

st.title("🤖 Job Matching Chatbot")
st.write("Upload your resume to find matching jobs based on your skills.")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📃 Extracted Resume Text")
    st.text(resume_text[:1000])  # Display first part only

    skills = extract_skills(resume_text)
    st.subheader("🧠 Extracted Skills")
    st.write(skills)

    with open("data/jobs.json") as f:
        job_data = json.load(f)

    job_descriptions = [job["description"] for job in job_data]
    matched_indices = match_jobs(resume_text, job_descriptions)

    st.subheader("🎯 Top Matching Jobs")
    for i in matched_indices[:3]:
        job = job_data[i]
        st.markdown(f"### {job['title']}")
        st.markdown(highlight_matches(job["description"], skills))
