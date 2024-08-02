import fitz  # PyMuPDF
import re

# Function to extract registration number from a PDF
def extract_registration_number(pdf_path):
    doc = fitz.open(pdf_path)
    registration_number = None
    
    # Compile the regular expression pattern
    pattern = re.compile(r'[0-9]{2}[A-Z0-9]{10}[A-Z]{3}')
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        # Search for the pattern
        match = pattern.search(text)
        
        if match:
            registration_number = match.group()
            break
    
    doc.close()
    return registration_number

# Example usage:
pdf_file = r'C:/Users/Sreelu/Downloads/gst.pdf'
found_registration_number = extract_registration_number(pdf_file)

if found_registration_number:
    print(f"Registration Number found: {found_registration_number}")
else:
    print("No Registration Number found in the PDF.")


