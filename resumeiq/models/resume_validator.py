RESUME_KEYWORDS = [
    "education", "skills", "projects",
    "certifications"
]

def is_valid_resume(text):
    text = text.lower()
    matches = sum(1 for k in RESUME_KEYWORDS if k in text)
    return matches >= 2
