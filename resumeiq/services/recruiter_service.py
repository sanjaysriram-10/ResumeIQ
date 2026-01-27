from resumeiq.models.semantic_matcher import semantic_match
from resumeiq.models.role_classifier import classify_role
from resumeiq.models.resume_parser import parse_resume


def normalize_similarity(score):
    if score < 0.25:
        return round(score * 80)
    elif score < 0.45:
        return round(40 + (score - 0.25) * 120)
    elif score < 0.65:
        return round(65 + (score - 0.45) * 100)
    else:
        return min(95, round(85 + (score - 0.65) * 100))


def analyze_resumes(resume_items, jd_text):
    results = []

    for item in resume_items:
        file = item["file"]
        stored_name = item["stored_name"]
        original_name = item["original_name"]

        resume_text = parse_resume(file)
        best_role, _ = classify_role(resume_text)

        raw_score = semantic_match(resume_text, jd_text)
        match_percentage = normalize_similarity(raw_score)

        results.append({
            "name": original_name.rsplit(".", 1)[0],
            "best_role": best_role,
            "match_percentage": match_percentage,
            "resume_url": f"/static/uploads/{stored_name}"
        })

    return results