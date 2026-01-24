import re
def parse_jd(jd_text: str) -> str:
    """
    Clean and normalize Job Description text
    for semantic matching.
    """
    if not jd_text:
        return ""
    jd_text = jd_text.lower()
    jd_text = re.sub(r"\s+", " ", jd_text)
    jd_text = re.sub(r"[^a-z0-9\s]", "", jd_text)
    return jd_text.strip()