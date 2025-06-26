# 🤖 Job Matching Chatbot

**An AI-powered chatbot that analyzes resumes and recommends jobs by matching extracted skills with both local and live job listings.**

---

## 📘 Table of Contents

- [Overview](#overview)  
- [Tech Stack](#tech-stack)  
- [Prerequisites](#prerequisites)  
- [Features](#features)  
- [Setup Instructions](#setup-instructions)  
- [How to Run](#how-to-run)  
- [💬 Sample Interaction](#sample-interaction)  
- [Evaluation Results](#evaluation-results)  
- [Future Improvements](#future-improvements)

---

## 🧠 Overview

Job Matching Chatbot helps users discover suitable job opportunities by analyzing their resumes using NLP. It recommends relevant jobs from a local dataset as well as live job listings fetched via the JSearch API.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python (NLP, API Integration)  
- **Resume Parsing:** PyMuPDF  
- **Job Matching:** Scikit-learn, FlashText  
- **Live Jobs API:** [JSearch API](https://rapidapi.com/)  
- **Hosting:** Streamlit Cloud

---

## 📋 Prerequisites

- Python 3.10+
- RapidAPI key (JSearch API)
- GitHub account
- Streamlit Cloud account (for deployment)

---

## ✨ Features

- 📄 Upload PDF Resume
- 🧠 Extract Skills from Resume using NLP
- 🔍 Match Resume with Local Job Descriptions using TF-IDF
- 🌐 Live Job Recommendations using API
- 🔐 API Key secured via `secrets.toml`
- 💡 Clean, interactive UI with Streamlit

---

## ⚙️ Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/job-matching-chatbot.git
   cd job-matching-chatbot
