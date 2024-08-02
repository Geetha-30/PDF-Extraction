import fitz  # PyMuPDF
import re

# Function to extract Udyam registration number from a PDF
def extract_udyam_registration_number(pdf_path):
    doc = fitz.open(pdf_path)
    udyam_registration_number = None
   
    # Compile the regular expression pattern
    pattern = re.compile(r'UDYAM-[A-Z]{2}-[0-9]{2}-[0-9]{6}')
   
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
       
        # Search for the pattern
        match = pattern.search(text)
       
        if match:
            udyam_registration_number = match.group()
            break
   
    doc.close()
    return udyam_registration_number

# Example usage:
pdf_file = r'C:\Users\Sreelu\Downloads\sa8000.pdf'
found_udyam_number = extract_udyam_registration_number(pdf_file)

if found_udyam_number:
    print(f"Udyam Registration Number found: {found_udyam_number}")
else:
    print("No Udyam Registration Number found in the PDF.")