import requests

def get_live_jobs(skill):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": skill, "page": "1", "num_pages": "1"}

    headers = {
        "X-RapidAPI-Key": "your_api_key_here",   # ← Replace with your real key
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jobs = response.json().get("data", [])
    
    return jobs
