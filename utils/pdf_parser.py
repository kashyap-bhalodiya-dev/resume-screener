import PyPDF2

# PyPDF is used to read PDF files and extract text

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or "" # avoid None issue
    
    return text