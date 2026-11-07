from smolagents import tool
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

@tool
def read_pdf(file_path:str) -> str:
    """ 
    Extract all text content from a given PDF file path.
    
    Args:
        file_path: The local path to the PDF file.
    
    Returns:
        The extracted text content from the PDF as a string,
    """
    import fitz
    
    try:
        doc = fitz.open(file_path)
        text = ""
        
        for page in doc:
            text += page.get_text()
        return text if text.strip() else "PDF is empty"
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
    
@tool
def image_to_text(image_path: str) -> str:
    """
    Extracts text from a given image file using OCR.

    Args:
        image_path: A string representing the local path to the image file (e.g., 'invoice.png','invoice.jpg','invoice.jpeg').

    Returns:
        A string containing the extracted text found within the image.
    """
    try:
        img = Image.open(image_path)
        
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text.strip() if extracted_text.strip() else "No readable text found in the image."
    except Exception as e :
        return f"Error processing image: {str(e)}"
    