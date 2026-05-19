#!/usr/bin/env python3
"""
OCR Processor for Math Buddy AI
Extracts mathematical equations from images using Tesseract OCR
"""

import pytesseract
from PIL import Image
import re
import numpy as np
import cv2

class MathOCR:
    def __init__(self):
        """Initialize OCR processor"""
        self.tesseract_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789+-*/.()=x^y'
    
    def extract_equation(self, image):
        """Extract mathematical equation from image"""
        try:
            # Preprocess image
            processed = self.preprocess_for_ocr(image)
            
            # Extract text using Tesseract
            text = pytesseract.image_to_string(
                processed,
                config=self.tesseract_config
            )
            
            # Clean up the text
            equation = self.clean_equation(text)
            
            print(f"📋 Extracted equation: {equation}")
            return equation
        
        except pytesseract.TesseractNotFoundError:
            print("❌ Tesseract not installed. Please install it:")
            print("   Windows: https://github.com/UB-Mannheim/tesseract/wiki")
            print("   Mac: brew install tesseract")
            print("   Linux: sudo apt-get install tesseract-ocr")
            raise
        
        except Exception as e:
            print(f"❌ OCR Error: {str(e)}")
            return ""
    
    def preprocess_for_ocr(self, image):
        """Preprocess image for better OCR accuracy"""
        try:
            # Convert PIL to OpenCV
            cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Convert to grayscale
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            
            # Increase contrast
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            contrast = clahe.apply(gray)
            
            # Apply thresholding
            _, thresh = cv2.threshold(contrast, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Denoise
            denoised = cv2.fastNlMeansDenoising(thresh, h=10)
            
            # Upscale for better OCR
            upscaled = cv2.resize(denoised, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            
            # Convert back to PIL
            processed = Image.fromarray(upscaled)
            
            return processed
        
        except Exception as e:
            print(f"❌ Preprocessing Error: {str(e)}")
            return image
    
    def clean_equation(self, text):
        """Clean and normalize extracted text"""
        try:
            # Remove extra whitespace
            text = text.strip()
            text = re.sub(r'\s+', '', text)
            
            # Replace common OCR errors
            replacements = {
                'O': '0',  # O to 0
                'l': '1',  # l to 1
                'I': '1',  # I to 1
                'S': '5',  # S to 5
                'Z': '2',  # Z to 2
            }
            
            for old, new in replacements.items():
                text = text.replace(old, new)
            
            # Handle common math symbols
            text = text.replace('×', '*')
            text = text.replace('÷', '/')
            text = text.replace('²', '**2')
            text = text.replace('³', '**3')
            text = text.replace('√', 'sqrt')
            
            # Ensure proper spacing around operators
            text = re.sub(r'([+\-*/=])', r' \1 ', text)
            text = re.sub(r'\s+', ' ', text)
            
            return text
        
        except Exception as e:
            print(f"❌ Cleaning Error: {str(e)}")
            return text

if __name__ == "__main__":
    # Test OCR
    ocr = MathOCR()
    
    # Create a simple test image
    from PIL import ImageDraw, ImageFont
    
    # Create image with text
    img = Image.new('RGB', (400, 100), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), "2x + 3 = 7", fill='black')
    
    # Extract
    equation = ocr.extract_equation(img)
    print(f"Extracted: {equation}")
