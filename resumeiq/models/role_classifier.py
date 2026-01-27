ROLE_SKILLS = {
    "Backend Developer": {
        "core": ["flask", "django", "rest api", "backend", "server"],
        "common": ["python", "sql"]
    },
    "Data Analyst": {
        "core": ["pandas", "numpy", "excel", "power bi", "tableau", "data analysis"],
        "common": ["python", "sql"]
    },
    "Machine Learning Engineer": {
        "core": ["machine learning", "model", "scikit", "tensorflow", "pytorch"],
        "common": ["python"]
    },
    "Full Stack Developer": {
        "core": ["javascript", "react", "node", "html", "css"],
        "common": ["python", "sql"]
    }
}


def classify_role(resume_text):
    text = resume_text.lower()
    role_scores = {}

    for role, skills in ROLE_SKILLS.items():
        core = skills["core"]
        common = skills["common"]

        core_hits = [s for s in core if s in text]
        common_hits = [s for s in common if s in text]

        # Reject roles with no core relevance
        if len(core_hits) == 0:
            role_scores[role] = 0
            continue

        #  Weighted scoring
        score = (len(core_hits) * 2) + (len(common_hits) * 0.5)

        # Normalize score
        max_score = (len(core) * 2) + (len(common) * 0.5)
        role_scores[role] = score / max_score

    #  If all scores are zero, fallback
    if all(score == 0 for score in role_scores.values()):
        return "General Software Role", 30

    best_role = max(role_scores, key=role_scores.get)
    confidence = round(role_scores[best_role] * 100, 2)

    return best_role, confidence