KEYWORDS = [
    "python",
    "java",
    "sql",
    "flask",
    "django",
    "machine learning",
    "data analysis",
    "api",
    "aws",
    "docker"
]

def ats_score(resume_text):
    text = resume_text.lower()
    matched = sum(1 for skill in KEYWORDS if skill in text)
    score = (matched / len(KEYWORDS)) * 100
    return round(score, 2)