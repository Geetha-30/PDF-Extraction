import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text

def extract_certificate_number_id(text):
    # Regular expression pattern for CERTIFICATE NUMBER followed by an ID
    pattern = re.compile(r'CERTIFICATE\s+NUMBER\s*:\s*(\w+)', re.IGNORECASE)

    match = re.search(pattern, text)
    if match:
        certificate_id = match.group(1)
        return certificate_id
    else:
        return ""

def validate_id(id_string):
    # Example pattern to validate ID (you can adjust as per your requirement)
    pattern_to_match = r'^QMS-MMXXII-\d{2}-\d{5}$'

    if re.match(pattern_to_match, id_string):
        return True
    else:
        return False

# Path to the PDF file
pdf_path = 'C:/Users/Sreelu/Downloads/iso.pdf'

# Extract text from PDF
pdf_text = extract_text_from_pdf(pdf_path)
print("Extracted Text:")
print(pdf_text)  # Debug: Print extracted text

# Extract CERTIFICATE NUMBER ID
certificate_id = extract_certificate_number_id(pdf_text)
print(f"Extracted Certificate ID: {certificate_id}")  # Debug: Print extracted certificate ID

# Validate the extracted ID and print if valid
if certificate_id and validate_id(certificate_id):
    print(certificate_id)
else:
    print("No valid CERTIFICATE NUMBER found.")