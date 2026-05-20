#!/usr/bin/env python3
"""
GUI Interface for Math Buddy AI
User-friendly Tkinter interface with camera and file upload
Enhanced with better error handling
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import os
from camera_module import CameraCapture
from ocr_processor import MathOCR
from math_solver import MathSolver

class MathBuddyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Buddy AI - Offline Math Solver")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        # Initialize modules
        self.camera = CameraCapture()
        self.ocr = MathOCR()
        self.solver = MathSolver()
        
        self.current_image = None
        self.current_equation = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame,
            text="🧮 Math Buddy AI - Offline Math Solver",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Image and controls
        left_panel = tk.Frame(main_frame, bg="white", relief=tk.RIDGE, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Image preview label
        img_label = tk.Label(left_panel, text="Image Preview", font=("Arial", 12, "bold"), bg="white")
        img_label.pack(pady=10)
        
        self.image_display = tk.Label(left_panel, bg="#ecf0f1", width=40, height=20)
        self.image_display.pack(padx=10, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(left_panel, bg="white")
        button_frame.pack(padx=10, pady=10, fill=tk.X)
        
        camera_btn = tk.Button(
            button_frame,
            text="📸 Capture from Camera",
            command=self.capture_camera,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        camera_btn.pack(side=tk.LEFT, padx=5)
        
        upload_btn = tk.Button(
            button_frame,
            text="📁 Upload Image",
            command=self.upload_image,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        upload_btn.pack(side=tk.LEFT, padx=5)
        
        # Right panel - Results and solver
        right_panel = tk.Frame(main_frame, bg="white", relief=tk.RIDGE, bd=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Help info frame
        help_frame = tk.Frame(right_panel, bg="#e8f4f8", relief=tk.SUNKEN, bd=1)
        help_frame.pack(padx=10, pady=5, fill=tk.X)
        
        help_label = tk.Label(
            help_frame,
            text="💡 Tip: You can type words like 'two x plus three equals seven' or use math format like '2*x + 3 = 7'",
            font=("Arial", 9),
            bg="#e8f4f8",
            fg="#2c3e50",
            wraplength=400,
            justify=tk.LEFT
        )
        help_label.pack(padx=5, pady=5)
        
        # Recognized equation
        eq_label = tk.Label(right_panel, text="📋 Recognized Equation", font=("Arial", 12, "bold"), bg="white")
        eq_label.pack(pady=10)
        
        self.equation_text = tk.Entry(right_panel, font=("Arial", 12), width=40)
        self.equation_text.pack(padx=10, pady=5, fill=tk.X)
        
        # Solve button
        solve_btn = tk.Button(
            right_panel,
            text="🧮 Solve Problem",
            command=self.solve_problem,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        solve_btn.pack(pady=10)
        
        # Solution display
        sol_label = tk.Label(right_panel, text="✍️ Solution Steps", font=("Arial", 12, "bold"), bg="white")
        sol_label.pack(pady=10)
        
        self.solution_text = scrolledtext.ScrolledText(
            right_panel,
            font=("Courier", 10),
            height=25,
            width=50,
            bg="#ecf0f1"
        )
        self.solution_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    def capture_camera(self):
        """Capture image from camera"""
        try:
            self.current_image = self.camera.capture()
            if self.current_image:
                self.display_image(self.current_image)
                self.extract_equation()
                messagebox.showinfo("Success", "Image captured successfully!")
        except Exception as e:
            messagebox.showerror("Camera Error", f"Error: {str(e)}")
    
    def upload_image(self):
        """Upload image from file"""
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
            )
            if file_path:
                self.current_image = Image.open(file_path)
                self.display_image(self.current_image)
                self.extract_equation()
                messagebox.showinfo("Success", "Image uploaded successfully!")
        except Exception as e:
            messagebox.showerror("Upload Error", f"Error: {str(e)}")
    
    def display_image(self, image):
        """Display image in preview"""
        try:
            # Resize image for display
            img_copy = image.copy()
            img_copy.thumbnail((400, 300), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img_copy)
            self.image_display.config(image=photo)
            self.image_display.image = photo
        except Exception as e:
            messagebox.showerror("Display Error", f"Error: {str(e)}")
    
    def extract_equation(self):
        """Extract equation from image using OCR"""
        try:
            if self.current_image:
                equation = self.ocr.extract_equation(self.current_image)
                self.current_equation = equation
                self.equation_text.delete(0, tk.END)
                self.equation_text.insert(0, equation)
                messagebox.showinfo("OCR Result", f"Equation extracted:\n{equation}")
        except Exception as e:
            messagebox.showerror("OCR Error", f"Error extracting equation: {str(e)}")
    
    def solve_problem(self):
        """Solve the mathematical problem"""
        try:
            equation = self.equation_text.get()
            if not equation:
                messagebox.showwarning("Input Required", "Please enter or capture an equation")
                return
            
            # Clear previous solution
            self.solution_text.delete(1.0, tk.END)
            
            # Solve the problem
            solution = self.solver.solve_and_explain(equation)
            
            # Display solution
            self.solution_text.insert(tk.END, solution)
            messagebox.showinfo("Success", "Problem solved successfully!")
        except Exception as e:
            messagebox.showerror("Solver Error", f"Error solving problem: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathBuddyGUI(root)
    root.mainloop()
