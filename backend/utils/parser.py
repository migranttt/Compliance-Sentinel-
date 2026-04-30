
import pdfplumber
from docx import Document

def parse_document(path):

    if path.endswith(".pdf"):
        return parse_pdf(path)

    if path.endswith(".docx"):
        return parse_docx(path)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def parse_pdf(path):

    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text

def parse_docx(path):

    doc = Document(path)

    return "\n".join([p.text for p in doc.paragraphs])
