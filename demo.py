import cv2
from PIL import Image
import pytesseract

# Specify the Tesseract executable path if it's not in PATH (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to clean up the image
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Optionally, apply dilation/erosion to enhance text edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    return processed_image

def extract_text(image_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)

    # Save preprocessed image temporarily for Tesseract
    temp_image_path = "temp_processed_image.png"
    cv2.imwrite(temp_image_path, processed_image)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(Image.open(temp_image_path), lang="eng", config="--psm 6")
    return text

# Input image path
image_path = "1.png"  # Replace with your image file

# Extract text
# text = extract_text(image_path)
# print("Extracted Text:")
# print(text)
