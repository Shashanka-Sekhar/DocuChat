import re
from pypdf import PdfReader


def clean_text(text):

    # Remove repeated spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple newlines with one
    text = re.sub(r"\n{2,}", "\n", text)

    # Remove page numbers (line containing only digits)
    text = re.sub(r"\n\d+\n", "\n", text)

    # Remove excessive blank spaces
    text = text.strip()

    return text


def load_pdf(file_path):
    reader = PdfReader(file_path)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            full_text += text + "\n"

    return clean_text(full_text)