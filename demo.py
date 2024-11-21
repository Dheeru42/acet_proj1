from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Update this path to where Tesseract-OCR is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    img = Image.open(image_path)
    # Convert image to grayscale
    img = img.convert("L")
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    # Apply a filter to remove noise
    img = img.filter(ImageFilter.MedianFilter())
    return img

def image_to_text(image_path):
    """Extract text from an image."""
    try:
        # Preprocess the image
        preprocessed_img = preprocess_image(image_path)
        
        # Perform OCR
        text = pytesseract.image_to_string(preprocessed_img)
        return text
    except Exception as e:
        return f"Error: {e}"

# Example usage
image_path = "1.png"  # Replace with your image path
result_text = image_to_text(image_path)
print("Extracted Text:\n", result_text)
