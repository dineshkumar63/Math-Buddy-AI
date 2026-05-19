#!/usr/bin/env python3
"""
Example usage of Math Buddy AI components
"""

from math_solver import MathSolver
from ocr_processor import MathOCR
from PIL import Image, ImageDraw, ImageFont

def example_solver():
    """Example: Solve various math equations"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Math Solver - Solving Equations")
    print("="*70 + "\n")
    
    solver = MathSolver()
    
    equations = [
        "2*x + 3 = 7",
        "x**2 + 2*x + 1 = 0",
        "x**2 - 5*x + 6 = 0",
        "3*x - 2 = 10",
        "x**2 = 16"
    ]
    
    for eq in equations:
        print(f"\nEquation: {eq}")
        print("-" * 70)
        result = solver.solve_and_explain(eq)
        print(result)

def example_simplify():
    """Example: Simplify expressions"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Simplify Expressions")
    print("="*70 + "\n")
    
    solver = MathSolver()
    
    expressions = [
        "2*x + 3*x",
        "(x + 1)**2",
        "(x**2 - 1)",
        "sin(x)**2 + cos(x)**2"
    ]
    
    for expr in expressions:
        simplified = solver.simplify_expression(expr)
        print(f"{expr} = {simplified}")

def example_expand():
    """Example: Expand expressions"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Expand Expressions")
    print("="*70 + "\n")
    
    solver = MathSolver()
    
    expressions = [
        "(x + 1)**2",
        "(x + 1)**3",
        "(x - 2)*(x + 3)",
        "(a + b)**2"
    ]
    
    for expr in expressions:
        expanded = solver.expand_expression(expr)
        print(f"{expr} = {expanded}")

def example_factor():
    """Example: Factor expressions"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Factor Expressions")
    print("="*70 + "\n")
    
    solver = MathSolver()
    
    expressions = [
        "x**2 + 2*x + 1",
        "x**2 - 1",
        "x**2 + 5*x + 6",
        "2*x**2 - 8"
    ]
    
    for expr in expressions:
        factored = solver.factor_expression(expr)
        print(f"{expr} = {factored}")

def example_ocr():
    """Example: OCR extraction"""
    print("\n" + "="*70)
    print("EXAMPLE 5: OCR - Extract Equations from Images")
    print("="*70 + "\n")
    
    ocr = MathOCR()
    
    # Create test image
    img = Image.new('RGB', (300, 100), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), "2x + 3 = 7", fill='black')
    
    print("Created test image with: '2x + 3 = 7'")
    print("Extracting equation using OCR...\n")
    
    try:
        equation = ocr.extract_equation(img)
        print(f"Extracted: {equation}")
    except Exception as e:
        print(f"Note: Tesseract not installed. This example requires Tesseract.")
        print(f"Error: {e}")

def main():
    """Run all examples"""
    print("\n" + "#"*70)
    print("# 🧮 Math Buddy AI - Example Usage")
    print("#"*70)
    
    try:
        example_solver()
        example_simplify()
        example_expand()
        example_factor()
        example_ocr()
        
        print("\n" + "#"*70)
        print("# ✅ All examples completed!")
        print("#"*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")

if __name__ == "__main__":
    main()
