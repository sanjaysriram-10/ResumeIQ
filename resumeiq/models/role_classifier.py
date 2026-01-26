ROLE_KEYWORDS = {
    "Backend Developer": {
        "core": ["flask", "django", "rest", "api", "backend"],
        "common": ["python", "sql"]
    },
    "Data Analyst": {
        "core": ["pandas", "numpy", "excel", "power bi", "tableau"],
        "common": ["python", "sql"]
    },
    "Machine Learning Engineer": {
        "core": ["machine learning", "model", "scikit", "tensorflow", "pytorch"],
        "common": ["python"]
    },
    "Full Stack Developer": {
        "core": ["javascript", "react", "node", "frontend", "html", "css"],
        "common": ["python", "sql"]
    }
}


def classify_role(resume_text):
    text = resume_text.lower()
    scores = {}

    for role, skill_groups in ROLE_KEYWORDS.items():
        core_skills = skill_groups["core"]
        common_skills = skill_groups["common"]

        core_matches = {
            skill for skill in core_skills if skill in text
        }
        common_matches = {
            skill for skill in common_skills if skill in text
        }

        score = (
            len(core_matches) * 2 +    # core skills matter more
            len(common_matches) * 0.5  # common skills matter less
        )

        max_score = len(core_skills) * 2 + len(common_skills) * 0.5
        normalized = score / max_score if max_score else 0

        scores[role] = normalized

    best_role = max(scores, key=scores.get)
    confidence = round(scores[best_role] * 100, 2)

    return best_role, confidence