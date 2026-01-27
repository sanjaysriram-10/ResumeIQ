from resumeiq.models.resume_parser import parse_resume
from resumeiq.models.ats_analyzer import ats_score
from resumeiq.models.role_classifier import classify_role
from resumeiq.models.resume_suggester import generate_resume_suggestions


def analyze_candidate_resume(file, target_role=None):
    resume_text = parse_resume(file)

    # ATS score
    ats = ats_score(resume_text)

    # AI-detected best-fit role
    best_role, best_role_confidence = classify_role(resume_text)

    # Role fit percentage
    if target_role:
        # Evaluate how well resume fits the USER-selected role
        _, role_fit = classify_role(resume_text)
    else:
        role_fit = best_role_confidence

    # Resume improvement suggestions
    recommendations = generate_resume_suggestions(
        resume_text,
        target_role if target_role else best_role
    )

    return {
        "ats_score": ats,
        "best_fit_role": best_role,               # AI decision
        "role_fit_percentage": round(role_fit, 2),
        "recommendations": recommendations
    }