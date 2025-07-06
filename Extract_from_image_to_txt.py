from PIL import Image
import pytesseract

def extract_text_from_images(image_path):
    # Open the image file from the given path
    image = Image.open(image_path)
    print("Image format/type:", type(image))  # Print the image type for debugging
    
    # Convert the image to RGB mode
    # This ensures compatibility since some formats (like AVIF) might not be directly supported by pytesseract
    image = image.convert('RGB')
    
    # Use pytesseract to perform OCR (Optical Character Recognition) on the image
    text = pytesseract.image_to_string(image)
    
    # Return the extracted text
    return text

if __name__ == "__main__":
    # Set the path to your image file here
    image_path = "/home/gh/Jailbreak4.jpg"
    
    # Call the function to extract text from the image
    extracted_text = extract_text_from_images(image_path)
    
    # Print the extracted text to the console
    print("Extracted text:")
    print(extracted_text)
