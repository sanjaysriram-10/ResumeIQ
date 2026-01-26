import re
import os
print(">>> name_extractor.py LOADED")

def extract_name(resume_text, filename=None):

    def extract_name(resume_text, filename=None):
        print(">>> extract_name CALLED")
        print(">>> filename:", filename)
        print(">>> text preview:", resume_text[:200])
        ...

    if looks_like_pdf_garbage(resume_text):
        return filename_to_name(filename)

    lines = resume_text.splitlines()[:10]
    text = " ".join(lines)

    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\+?\d[\d\s\-]{8,}', '', text)
    text = re.sub(r'[^A-Za-z\s]', ' ', text)

    words = text.split()

    for i in range(len(words) - 1):
        name = words[i] + " " + words[i + 1]
        if is_reasonable_name(name):
            return name.title()

        if i + 2 < len(words):
            name = words[i] + " " + words[i + 1] + " " + words[i + 2]
            if is_reasonable_name(name):
                return name.title()

    return filename_to_name(filename)


def filename_to_name(filename):
    if not filename:
        return "Candidate"
    base = os.path.splitext(filename)[0]

    base = re.sub(r'[_\-]', ' ', base)

    remove_words = [
        "resume", "cv", "profile", "updated",
        "final", "latest", "copy"
    ]

    words = base.split()
    clean_words = [
        w for w in words
        if w.lower() not in remove_words and w.isalpha()
    ]

    name_words = clean_words[:3]

    if len(name_words) >= 2:
        return " ".join(name_words).title()
    return "Candidate"


def is_reasonable_name(name):
    words = name.split()
    return 2 <= len(words) <= 3 and all(word.isalpha() for word in words)


def looks_like_pdf_garbage(text):
    bad_keywords = ["obj", "xref", "endobj", "stream", "pdf"]
    text_lower = text.lower()
    return sum(k in text_lower for k in bad_keywords) >= 2