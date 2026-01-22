ATS_KEYWORDS = [
    "python", "java", "sql", "flask", "django", "api",
    "machine learning", "data analysis", "aws",
    "git", "docker", "html", "css", "javascript"
]

def ats_score(resume_text):
    text = resume_text.lower()
    matched = sum(1 for k in ATS_KEYWORDS if k in text)
    return round((matched / len(ATS_KEYWORDS)) * 100, 2)
