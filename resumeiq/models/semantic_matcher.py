from sklearn.metrics.pairwise import cosine_similarity
from resumeiq.models.embedding_loader import get_embedding


def semantic_match(resume_text: str, jd_text: str) -> float:
    """
    Compute semantic similarity between resume and job description.
    Returns a score between 0 and 1.
    """

    if not resume_text or not jd_text:
        return 0.0

    resume_embedding = get_embedding(resume_text)
    jd_embedding = get_embedding(jd_text)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(float(similarity), 4)