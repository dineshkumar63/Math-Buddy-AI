#!/usr/bin/env python3
"""
Camera Module for Math Buddy AI
Handles webcam capture and image preprocessing
"""

import cv2
import numpy as np
from PIL import Image
import io

class CameraCapture:
    def __init__(self, camera_index=0):
        """Initialize camera capture"""
        self.camera_index = camera_index
        self.cap = None
    
    def capture(self):
        """Capture image from webcam"""
        try:
            # Open camera
            self.cap = cv2.VideoCapture(self.camera_index)
            
            if not self.cap.isOpened():
                raise Exception("Cannot open camera")
            
            # Set camera properties
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            
            print("📸 Camera opened. Press SPACE to capture, Q to quit")
            
            while True:
                ret, frame = self.cap.read()
                
                if not ret:
                    raise Exception("Failed to read frame")
                
                # Display frame
                cv2.imshow('Math Buddy AI - Camera Capture (Press SPACE to capture, Q to quit)', frame)
                
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord(' '):
                    # Capture image
                    cv2.destroyAllWindows()
                    self.cap.release()
                    
                    # Convert BGR to RGB
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    # Convert to PIL Image
                    pil_image = Image.fromarray(rgb_frame)
                    
                    print("✅ Image captured successfully")
                    return pil_image
                
                elif key == ord('q'):
                    cv2.destroyAllWindows()
                    self.cap.release()
                    print("❌ Camera capture cancelled")
                    return None
        
        except Exception as e:
            print(f"❌ Camera Error: {str(e)}")
            if self.cap:
                self.cap.release()
            cv2.destroyAllWindows()
            raise
    
    def preprocess_image(self, image):
        """Preprocess image for better OCR"""
        try:
            # Convert PIL to OpenCV format
            cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Convert to grayscale
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            
            # Apply thresholding
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            
            # Denoise
            denoised = cv2.fastNlMeansDenoising(thresh)
            
            # Convert back to PIL
            processed = Image.fromarray(denoised)
            
            return processed
        
        except Exception as e:
            print(f"❌ Preprocessing Error: {str(e)}")
            return image

if __name__ == "__main__":
    camera = CameraCapture()
    image = camera.capture()
    if image:
        print("✅ Capture successful")
