def generate_resume_suggestions(resume_text, target_role=None):
    text = resume_text.lower()
    suggestions = []

    # Section checks
    if "project" not in text:
        suggestions.append("Add a Projects section with real-world problem statements and outcomes.")

    if "experience" not in text and "intern" not in text:
        suggestions.append("Include an Experience or Internship section to showcase practical exposure.")

    if "education" not in text:
        suggestions.append("Add an Education section with degree, institution, and graduation year.")

    # Action verb quality
    weak_verbs = ["worked on", "helped", "responsible for"]
    if any(verb in text for verb in weak_verbs):
        suggestions.append(
            "Use stronger action verbs like 'developed', 'implemented', 'optimized', or 'designed'."
        )

    # Tools & deployment
    tools = ["docker", "aws", "gcp", "azure", "github"]
    if not any(tool in text for tool in tools):
        suggestions.append(
            "Mention tools or platforms used (GitHub, Docker, AWS, etc.) to strengthen technical credibility."
        )

    # Role-specific advice
    if target_role:
        if target_role.lower() == "backend developer" and "api" not in text:
            suggestions.append("Mention REST API or backend service development experience.")
        if target_role.lower() == "data analyst" and "dashboard" not in text:
            suggestions.append("Add details about dashboards, reports, or data visualization tools used.")
        if target_role.lower() == "machine learning engineer" and "model" not in text:
            suggestions.append("Highlight ML models, datasets, and evaluation metrics you've worked with.")

    if not suggestions:
        suggestions.append("Your resume looks well-structured. Consider tailoring it more to the target role.")

    return suggestions