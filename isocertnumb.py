import fitz  # PyMuPDF
import re

# Function to extract certificate number from a PDF
def extract_certificate_number(pdf_path):
    doc = fitz.open(pdf_path)
    certificate_number = None
    
    # Compile the regular expression pattern
    pattern = re.compile(r'QMS-[IVXLCDM]+-[0-9]{2}-[0-9]{5}')
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        # Search for the pattern
        match = pattern.search(text)
        
        if match:
            certificate_number = match.group()
            break
    
    doc.close()
    return certificate_number

# Example usage:
pdf_file = r'C:/Users/Sreelu/Downloads/iso.pdf'
found_certificate_number = extract_certificate_number(pdf_file)

if found_certificate_number:
    print(f"Certificate Number found: {found_certificate_number}")
else:
    print("No Certificate Number found in the PDF.")


