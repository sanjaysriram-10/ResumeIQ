import PyPDF2

def parse_resume(file):
    text = ""

    if file.filename.lower().endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    else:
        text = file.read().decode("utf-8", errors="ignore")

    return text.strip()