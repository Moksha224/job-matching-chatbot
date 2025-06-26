from utils.job_api import get_live_jobs
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
    st.text(resume_text[:1000])  # Show only first part

    skills = extract_skills(resume_text)
    st.subheader("🧠 Extracted Skills")
    st.write(skills)

    # 🔸 Local Job Matching (offline from jobs.json)
    try:
        with open("data/jobs.json") as f:
            job_data = json.load(f)

        job_descriptions = [job["description"] for job in job_data]
        matched_indices = match_jobs(resume_text, job_descriptions)

        st.subheader("🎯 Top Matching Jobs (from dataset)")
        for i in matched_indices[:3]:
            job = job_data[i]
            st.markdown(f"### {job['title']}")
            st.markdown(highlight_matches(job["description"], skills))

    except FileNotFoundError:
        st.warning("jobs.json not found. Skipping local match.")

    # 🔹 Live Job Matching from API
    st.subheader("🌐 Live Job Recommendations")

    if skills:
        all_jobs = []
        for skill in skills:
            try:
                jobs = get_live_jobs(skill)
                all_jobs.extend(jobs[:2])  # Top 2 jobs per skill
            except Exception as e:
                st.error(f"Error fetching jobs for '{skill}': {e}")

        if all_jobs:
            for job in all_jobs:
                st.markdown(f"### {job['job_title']} at {job['employer_name']}")
                st.markdown(f"📍 {job.get('job_city', '')}, {job.get('job_country', '')}")
                st.markdown(f"🔗 [Apply Here]({job['job_apply_link']})")
                st.markdown("---")
        else:
            st.info("No live jobs found. Try changing skills or check API key.")
