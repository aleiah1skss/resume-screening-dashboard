import streamlit as st
import pandas as pd
from pdfplumber import PDF
from docx import Document

# -----------------------------
# Helper functions
# -----------------------------

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    with PDF(uploaded_file) as pdf:  # UploadedFile works directly
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Extract text from DOCX
def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)  # UploadedFile works directly
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)

# Hard match scoring
def hard_match_score(resume_text, jd_skills):
    jd_skill_list = [skill.strip().lower() for skill in jd_skills.split(",")]
    resume_words = resume_text.lower().split()
    
    matched = [skill for skill in jd_skill_list if skill in resume_words]
    missing = [skill for skill in jd_skill_list if skill not in resume_words]
    
    hard_score = (len(matched) / len(jd_skill_list)) * 100 if jd_skill_list else 0
    return hard_score, matched, missing

# Semantic match (dummy implementation)
def semantic_score_local(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    common = resume_words.intersection(jd_words)
    sem_score = (len(common) / len(jd_words)) * 100 if jd_words else 0
    return sem_score

# Final score
def final_score(hard, semantic):
    return round(0.5*hard + 0.5*semantic, 2)

# Verdict based on final score
def verdict(final_score):
    if final_score >= 75:
        return "High"
    elif final_score >= 50:
        return "Medium"
    else:
        return "Low"

# HTML for colored verdict
def verdict_html(val):
    if val == "High":
        color = "lightgreen"
    elif val == "Medium":
        color = "yellow"
    elif val == "Low":
        color = "lightcoral"
    else:
        color = "white"
    return f"<div style='background-color:{color}; text-align:center; font-weight:bold'>{val}</div>"

# -----------------------------
# Streamlit UI
# -----------------------------

st.title("Automated Resume Relevance Check System")

# Job Description input
jd_text = st.text_area("Enter Job Description")
jd_skills = st.text_input("Enter JD Skills (comma separated)")
jd_responsibilities = st.text_area("Enter Job Responsibilities (optional)")
jd_requirements = st.text_area("Enter Job Requirements (optional)")

# Multiple Resume Upload
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True
)

if uploaded_files and jd_text and jd_skills:
    # Initialize results list
    results = []

    for uploaded_file in uploaded_files:
        # Extract text
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.warning(f"Unsupported file type: {uploaded_file.name}")
            continue

        # Calculate scores
        hard, matched, missing = hard_match_score(resume_text, jd_skills)
        sem_score = semantic_score_local(resume_text, jd_text)
        final = final_score(hard, sem_score)
        fit = verdict(final)

        # Store result
        results.append({
            "Resume": uploaded_file.name,
            "Matched Skills": matched,
            "Missing Skills": missing,
            "Hard Score": round(hard, 2),
            "Semantic Score": round(sem_score, 2),
            "Final Score": round(final, 2),
            "Verdict": fit
        })

    # Convert results to DataFrame
    df = pd.DataFrame(results)

    # Join long lists into readable strings
    df['Matched Skills'] = df['Matched Skills'].apply(lambda x: ", ".join(x))
    df['Missing Skills'] = df['Missing Skills'].apply(lambda x: ", ".join(x))

    # Display results with colored verdict
    st.subheader("All Resume Results")
    for i in range(len(df)):
        st.write(f"**Resume:** {df.loc[i,'Resume']}")
        st.write(f"**Matched Skills:** {df.loc[i,'Matched Skills']}")
        st.write(f"**Missing Skills:** {df.loc[i,'Missing Skills']}")
        st.write(f"**Hard Score:** {df.loc[i,'Hard Score']}")
        st.write(f"**Semantic Score:** {df.loc[i,'Semantic Score']}")
        st.write(f"**Final Score:** {df.loc[i,'Final Score']}")
        st.markdown(verdict_html(df.loc[i,'Verdict']), unsafe_allow_html=True)
        st.markdown("---")

    # Optional: Download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="resume_results.csv",
        mime="text/csv"
    )

else:
    st.info("Please enter Job Description, JD Skills, and upload at least one resume to see results.")