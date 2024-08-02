import fitz  # PyMuPDF
import re

# Function to extract referral ID from a PDF
def extract_referral_id(pdf_path):
    doc = fitz.open(pdf_path)
    referral_id = None
    
    # Compile the regular expression pattern
    pattern = re.compile(r'[A-Z]{2}/[0-9]{4}-[0-9]{2}/[A-Z]{4}/[A-Z]{3}')
    
    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        # Search for the pattern
        match = pattern.search(text)
        
        if match:
            referral_id = match.group()
            break
    
    doc.close()
    return referral_id

# Example usage:
pdf_file = r'C:/Users/Sreelu/Downloads/lou.pdf'
found_referral_id = extract_referral_id(pdf_file)

if found_referral_id:
    print(f"Referral ID found: {found_referral_id}")
else:
    print("No Referral ID found in the PDF.")


