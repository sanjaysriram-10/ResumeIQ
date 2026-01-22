from io import BytesIO

def parse_resume(file):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    if filename.endswith(".pdf"):
        from PyPDF2 import PdfReader
        reader = PdfReader(BytesIO(file.read()))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if filename.endswith(".docx"):
        from docx import Document
        doc = Document(BytesIO(file.read()))
        return "\n".join(p.text for p in doc.paragraphs)

    return ""
