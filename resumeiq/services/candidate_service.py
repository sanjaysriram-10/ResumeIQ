from resumeiq.models.resume_parser import parse_resume
from resumeiq.models.ats_analyzer import ats_score
from resumeiq.models.role_classifier import classify_role
from resumeiq.data.roles import ROLE_SKILLS


def analyze_candidate(resume_file, target_role=None):
    """
    Analyze a candidate resume and return:
    - ATS score
    - Best-fit role
    - Role fit percentage (0–100)
    - Resume improvement recommendations
    """

    # Parse resume (do not block any file)
    resume_text = parse_resume(resume_file) or ""
    resume_lower = resume_text.lower()

    # ATS score
    ats = ats_score(resume_text)

    # Infer best-fit role from resume
    best_role, role_fit_confidence = classify_role(resume_text)

    # Case 1: Candidate selected a target role
    if target_role and target_role in ROLE_SKILLS:
        required_skills = ROLE_SKILLS[target_role]

        # Count UNIQUE matched skills only
        matched_skills = {
            skill for skill in required_skills
            if skill.lower() in resume_lower
        }

        missing_skills = [
            skill for skill in required_skills
            if skill.lower() not in resume_lower
        ]

        role_fit_percentage = (
            round((len(matched_skills) / len(required_skills)) * 100, 2)
            if required_skills else 0.0
        )

        # Safety cap
        role_fit_percentage = min(role_fit_percentage, 100.0)

        recommendations = [
            f"Add experience, projects, or certifications related to {skill}"
            for skill in missing_skills
        ]

        if not recommendations:
            recommendations = [
                "Your resume aligns well with this role. "
                "Consider strengthening recent projects and measurable impacts."
            ]

        return {
            "ats_score": ats,
            "best_fit_role": target_role,
            "role_fit_percentage": role_fit_percentage,
            "recommendations": recommendations
        }

    # Case 2: No target role selected
    return {
        "ats_score": ats,
        "best_fit_role": best_role,
        # role_fit_confidence is ALREADY a percentage (0–100)
        "role_fit_percentage": role_fit_confidence,
        "recommendations": [
            f"Your resume aligns most closely with a {best_role} role.",
            "Improve role-specific skills and quantify achievements "
            "to increase your overall fit."
        ]
    }