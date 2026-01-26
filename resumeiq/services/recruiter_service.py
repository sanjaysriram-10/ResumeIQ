import os
from resumeiq.models.semantic_matcher import semantic_match
from resumeiq.models.role_classifier import classify_role
from resumeiq.models.resume_parser import parse_resume


def normalize_similarity(score):
    """
    Normalize semantic similarity (0–1) into recruiter-friendly percentage
    """
    if score <= 0.3:
        return round(score * 100)
    elif score <= 0.6:
        return round(40 + (score - 0.3) * 100)
    else:
        return min(95, round(70 + (score - 0.6) * 125))


def analyze_resumes(resume_files, jd_text):
    results = []

    for file in resume_files:
        resume_text = parse_resume(file)
        best_role, _ = classify_role(resume_text)

        raw_score = semantic_match(resume_text, jd_text)
        match_percentage = normalize_similarity(raw_score)

        results.append({
            "name": file.filename.replace(".pdf", "").replace(".txt", ""),
            "best_role": best_role,
            "match_percentage": match_percentage,
            "resume_url": f"/static/uploads/{file.filename}"
        })

    return results