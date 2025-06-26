import requests

def get_live_jobs(skill):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": skill, "page": "1", "num_pages": "1"}

    headers = {
        "X-RapidAPI-Key": "de6f9ef636msh1e1ad8ff49e213ep1f7c3cjsn704dae3fa2f6",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(f"API Response status: {response.status_code}")  # NEW
    print(f"Response JSON: {response.json()}")             # NEW

    if response.status_code == 200:
        jobs = response.json().get("data", [])
        return jobs
    else:
        return []
if all_jobs:
    for job in all_jobs:
        st.markdown(f"### {job['job_title']} at {job['employer_name']}")
        st.markdown(f"📍 {job.get('job_city', '')}, {job.get('job_country', '')}")
        st.markdown(f"🔗 [Apply Here]({job['job_apply_link']})")
        st.markdown("---")
else:
    st.info("No jobs found. Try changing the skills or check your API key.")

