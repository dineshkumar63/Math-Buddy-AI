#!/usr/bin/env python3
"""
Setup script for Math Buddy AI
Installs all required dependencies
"""

import os
import sys
import subprocess
import platform

def print_header():
    """Print setup header"""
    print("\n" + "="*60)
    print("🧮 Math Buddy AI - Setup Wizard")
    print("="*60 + "\n")

def install_python_packages():
    """Install required Python packages"""
    print("📦 Installing Python packages...\n")
    
    packages = [
        "sympy",
        "opencv-python",
        "pytesseract",
        "pillow",
        "numpy"
    ]
    
    for package in packages:
        print(f"  Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"  ✅ {package} installed successfully\n")
        except subprocess.CalledProcessError:
            print(f"  ❌ Failed to install {package}\n")
            return False
    
    return True

def install_tesseract():
    """Guide user to install Tesseract OCR"""
    print("\n" + "="*60)
    print("📋 Tesseract OCR Installation Required")
    print("="*60 + "\n")
    
    system = platform.system()
    
    if system == "Windows":
        print("Windows Installation:")
        print("1. Download installer from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Run the installer (accept default path)")
        print("3. After installation, Python will find it automatically")
        print("\n   If Tesseract is in a custom location, update ocr_processor.py:")
        print("   pytesseract.pytesseract.pytesseract_cmd = r'C:\\path\\to\\tesseract.exe'\n")
    
    elif system == "Darwin":  # macOS
        print("macOS Installation:")
        print("1. Install Homebrew if not already installed")
        print("2. Run: brew install tesseract")
        print("3. Verify: tesseract --version\n")
    
    elif system == "Linux":
        print("Linux Installation (Ubuntu/Debian):")
        print("1. Run: sudo apt-get update")
        print("2. Run: sudo apt-get install tesseract-ocr")
        print("3. Verify: tesseract --version\n")
    
    input("Press Enter after installing Tesseract...")

def verify_installation():
    """Verify all dependencies are installed"""
    print("\n" + "="*60)
    print("✓ Verifying Installation")
    print("="*60 + "\n")
    
    modules = {
        "sympy": "SymPy (Symbolic Math)",
        "cv2": "OpenCV (Computer Vision)",
        "pytesseract": "Tesseract OCR",
        "PIL": "Pillow (Image Processing)",
        "numpy": "NumPy (Numerical Computing)"
    }
    
    all_ok = True
    
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"✅ {name}: OK")
        except ImportError:
            print(f"❌ {name}: NOT FOUND")
            all_ok = False
    
    return all_ok

def main():
    """Main setup function"""
    print_header()
    
    # Install Python packages
    if not install_python_packages():
        print("\n❌ Failed to install some packages")
        sys.exit(1)
    
    # Install Tesseract
    install_tesseract()
    
    # Verify installation
    if verify_installation():
        print("\n" + "="*60)
        print("✅ Installation Complete!")
        print("="*60)
        print("\nTo start Math Buddy AI, run:")
        print("  python main.py\n")
    else:
        print("\n" + "="*60)
        print("⚠️  Some components are missing")
        print("="*60)
        print("\nPlease install the missing components and try again.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
