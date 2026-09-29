import os
from pypdf import PdfReader


def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text


def extract_skills(text, skills):
    found_skills = []
    for skill in skills:
        if skill in text:
            found_skills.append(skill)
    return found_skills


def compare_skills(resume_skills, job_skills):
    matched_skills = []
    missing_skills = []
    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    return matched_skills, missing_skills


def calculate_match_score(matched_skills, job_skills):
    if not job_skills:
        return 0.0
    return (len(matched_skills) / len(job_skills)) * 100


# ---- Main script ----

resume_path = "CV_NABHAN.pdf"

if not os.path.exists(resume_path):
    print(f"ERROR: '{resume_path}' was not found in this folder:")
    print(os.getcwd())
    print("Files currently in this folder:")
    for f in os.listdir("."):
        print(" -", f)
    exit()

reader = PdfReader(resume_path)

text = ""
for page in reader.pages:
    text = text + page.extract_text()

cleaned_text = clean_text(text)

skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "power bi",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "git",
    "docker"
]

found_skills = extract_skills(cleaned_text, skills)
print("Skills found:", found_skills)

job_description = """
We are looking for an AI/ML Developer with experience in Python,
SQL, Machine Learning, Pandas, Power BI, Docker and Git.
Knowledge of NLP and deep learning is an advantage.
"""

cleaned_job = clean_text(job_description)
job_skills = extract_skills(cleaned_job, skills)
print("Job skills:", job_skills)

matched_skills, missing_skills = compare_skills(found_skills, job_skills)
print("Matched skills:", matched_skills)
print("Missing skills:", missing_skills)

match_score = calculate_match_score(matched_skills, job_skills)
print("Match score:", round(match_score, 2), "%")