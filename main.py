#!/usr/bin/env python3
"""
Math Buddy AI - Main Application Entry Point
Offline AI-powered math solver with camera input and OCR
"""

import sys
import tkinter as tk
from gui_interface import MathBuddyGUI

def main():
    """Initialize and run the Math Buddy AI application"""
    print("🚀 Starting Math Buddy AI...")
    print("=" * 50)
    print("Math Buddy AI - Offline Math Solver")
    print("=" * 50)
    
    try:
        # Create root window
        root = tk.Tk()
        root.title("Math Buddy AI")
        root.geometry("1000x700")
        
        # Initialize GUI
        app = MathBuddyGUI(root)
        
        # Run application
        root.mainloop()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Please install all required dependencies:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
