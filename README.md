<<<<<<< HEAD
# Automated Resume Relevance Check System

## Overview
A Streamlit web app designed for placement teams to evaluate resumes against job descriptions.  
The system automatically scores resumes based on **hard skill matching** and **semantic understanding** using AI/LLMs, highlights missing skills, and provides a suitability verdict.

---

## Features
- Upload multiple resumes (PDF/DOCX)
- Upload Job Descriptions and Skills
- Extract text from resumes and JDs
- **Hard Match**: Exact and fuzzy keyword/skill matching
- **Semantic Match**: Contextual comparison using AI embeddings
- Generate a **Relevance Score (0–100)** and verdict (High / Medium / Low)
- Highlight missing skills, projects, or certifications
- Download results as CSV
- Web-based dashboard for placement team use

---

## Tech Stack
- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **Libraries**:
  - `pandas` – Data handling
  - `pdfplumber` / `python-docx` – Extract text from PDF/DOCX
  - `openai` – LLM embeddings for semantic matching
  - `numpy` – Numerical computations
  - `fuzzywuzzy` – Fuzzy keyword matching
- **Deployment**: Streamlit Cloud

---

## Files
- `resume_dashboard.py` — Main Streamlit application
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

---

## How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/aleiah1skss/resume-screening-dashboard.git
cd resume-screening-dashboard

2.Create a virtual environment (optional but recommended)
python -m venv hackathon_env
source hackathon_env/Scripts/activate   # Windows
# OR
source hackathon_env/bin/activate       # Mac/Linux

3.Install dependencies
pip install -r requirements.txt

4.Run the app
streamlit run resume_dashboard.py

## How to Use

° Enter the Job Description and Skills (comma separated).
° Upload resumes (PDF or DOCX).
° View results table showing:
   Matched Skills
   Missing Skills
   Hard Score
   Semantic Score
   Final Score
   Verdict (High/Medium/Low)
° Download results as CSV for record keeping.

🔗Demo / Live App
[https://resume-screening-dashboard.streamlit.app/](https://resume-screening-dashboard.streamlit.app/)

## Future Improvements

Add requirements and responsibilities matching for better scoring.
Add company-specific weightage for skills.
Improve visualization with charts for skill gaps.
Extend support to resume templates in multiple formats

## Author
Aliya Nishath (Cipher)
partcipating as solo
College : COORG INSTITUTE OF TECHNOLOGY
Cybersecurity Trainee & Internship Aspirant
Email: aalianishath1005@gmail.com
Phn no.: 8496001161
passout year : 2027



 
=======
# resume-screening-dashboard
Streamlit web app for automated resume–job description matching (Hackathon project)
>>>>>>> 25f95c872e30763be3d3fd54d3bfd993add85f41
