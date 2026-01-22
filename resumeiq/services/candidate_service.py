from resumeiq.models.resume_parser import parse_resume
from resumeiq.models.ats_analyzer import ats_score

SKILLS = [
    "python", "java", "sql", "flask", "django",
    "machine learning", "data analysis",
    "aws", "git", "docker", "html", "css", "javascript"
]

def analyze_candidate(resume_file):
    resume_text = parse_resume(resume_file)

    if not resume_text or len(resume_text.strip()) < 100:
        return {"error": "Uploaded file does not appear to be a valid resume"}

    ats = ats_score(resume_text)

    text_lower = resume_text.lower()
    extracted_skills = [s for s in SKILLS if s in text_lower]

    return {
        "ats_score": ats,
        "skills": extracted_skills,
        "resume_length": len(resume_text)
    }
