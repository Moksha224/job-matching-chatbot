from flashtext import KeywordProcessor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILL_LIST = ["Python", "SQL", "Excel", "Data Analysis", "Machine Learning", "Pandas", "Numpy", "Deep Learning"]

def extract_skills(text):
    kp = KeywordProcessor()
    kp.add_keywords_from_list(SKILL_LIST)
    return kp.extract_keywords(text)

def match_jobs(resume_text, job_descriptions):
    all_texts = [resume_text] + job_descriptions
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(all_texts)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return similarity.argsort()[0][::-1]

def highlight_matches(text, keywords):
    for kw in keywords:
        text = text.replace(kw, f"**{kw}**")
    return text
