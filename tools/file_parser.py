import os
from pypdf import PdfReader
from docx import Document

UPLOAD_FOLDER = "uploads"

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text(file):
    """
    Detect file type and extract text.
    Returns extracted text or saved audio path.
    """

    file_extension = os.path.splitext(file.name)[1].lower()

    if file_extension == ".txt":
        return file.read().decode("utf-8")

    elif file_extension == ".pdf":
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text

    elif file_extension == ".docx":
        document = Document(file)
        text = "\n".join([para.text for para in document.paragraphs])
        return text

    elif file_extension in [".mp3", ".wav", ".m4a"]:
        save_path = os.path.join(UPLOAD_FOLDER, file.name)

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        return save_path

    else:
        raise ValueError("Unsupported file format.")