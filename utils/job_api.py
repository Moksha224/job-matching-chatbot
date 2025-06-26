import requests

def get_live_jobs(skill):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": skill, "page": "1", "num_pages": "1"}

    headers = {
        "X-RapidAPI-Key": "de6f9ef636msh1e1ad8ff49e213ep1f7c3cjsn704dae3fa2f6",   # ← Replace with your real key
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jobs = response.json().get("data", [])
    
    return jobs
