#!/usr/bin/env python3
"""
Math Solver Module for Math Buddy AI
Powered by SymPy for symbolic mathematics
"""

from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import re

class MathSolver:
    def __init__(self):
        """Initialize math solver"""
        self.symbols_cache = {}
    
    def solve_and_explain(self, equation_str):
        """Solve equation and provide step-by-step explanation"""
        try:
            solution_text = "" + "="*60 + "\n"
            solution_text += "📊 SOLUTION STEPS\n"
            solution_text += "="*60 + "\n\n"
            
            # Clean the equation string
            equation_str = self.clean_equation_string(equation_str)
            solution_text += f"Original Equation: {equation_str}\n\n"
            
            # Parse the equation
            if '=' in equation_str:
                left, right = equation_str.split('=')
                equation = parse_expr(left) - parse_expr(right)
            else:
                equation = parse_expr(equation_str)
            
            # Extract variables
            variables = list(equation.free_symbols)
            
            if not variables:
                # No variables, just simplify
                simplified = simplify(equation)
                solution_text += f"Simplified: {simplified}\n"
                return solution_text
            
            # Main variable to solve for
            main_var = variables[0]
            
            solution_text += f"Variable to solve: {main_var}\n\n"
            
            # Solve the equation
            solutions = solve(equation, main_var)
            
            if not solutions:
                solution_text += "❌ No solution found!\n"
                return solution_text
            
            solution_text += f"✅ Solutions Found: {len(solutions)}\n"
            solution_text += "-" * 60 + "\n\n"
            
            # Display each solution
            for i, sol in enumerate(solutions, 1):
                solution_text += f"Solution {i}: {main_var} = {sol}\n"
                
                # Try to simplify
                try:
                    simplified = simplify(sol)
                    if simplified != sol:
                        solution_text += f"  Simplified: {simplified}\n"
                except:
                    pass
                
                # Try to get numeric value
                try:
                    numeric = float(sol.evalf())
                    solution_text += f"  Numeric Value: {numeric:.6f}\n"
                except:
                    pass
                
                solution_text += "\n"
            
            # Verification
            solution_text += "-" * 60 + "\n"
            solution_text += "✓ VERIFICATION:\n"
            solution_text += "-" * 60 + "\n\n"
            
            for i, sol in enumerate(solutions, 1):
                try:
                    # Substitute solution back into original equation
                    verification = equation.subs(main_var, sol)
                    verification_simplified = simplify(verification)
                    
                    if verification_simplified == 0:
                        solution_text += f"Solution {i}: ✓ VERIFIED (Equation = 0)\n"
                    else:
                        solution_text += f"Solution {i}: Result = {verification_simplified}\n"
                except:
                    pass
            
            solution_text += "\n" + "="*60 + "\n"
            
            return solution_text
        
        except Exception as e:
            return f"❌ Error solving equation: {str(e)}\n\nPlease check your equation format."
    
    def clean_equation_string(self, equation_str):
        """Clean and normalize equation string"""
        try:
            # Remove extra spaces
            equation_str = equation_str.strip()
            
            # Replace common symbols
            equation_str = equation_str.replace('×', '*')
            equation_str = equation_str.replace('÷', '/')
            equation_str = equation_str.replace('^', '**')
            equation_str = equation_str.replace('√', 'sqrt')
            equation_str = equation_str.replace('π', 'pi')
            equation_str = equation_str.replace('θ', 'theta')
            
            # Add multiplication between number and variable
            equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)
            
            # Add multiplication between variable and variable
            equation_str = re.sub(r'([a-zA-Z])(\()', r'\1*\2', equation_str)
            
            return equation_str
        except:
            return equation_str
    
    def simplify_expression(self, expr_str):
        """Simplify mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            simplified = simplify(expr)
            return str(simplified)
        except:
            return "Error simplifying expression"
    
    def expand_expression(self, expr_str):
        """Expand mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            expanded = expand(expr)
            return str(expanded)
        except:
            return "Error expanding expression"
    
    def factor_expression(self, expr_str):
        """Factor mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            factored = factor(expr)
            return str(factored)
        except:
            return "Error factoring expression"

if __name__ == "__main__":
    # Test solver
    solver = MathSolver()
    
    # Test cases
    test_equations = [
        "2*x + 3 = 7",
        "x**2 + 2*x + 1 = 0",
        "x**2 - 5*x + 6 = 0",
        "3*x - 2 = 10"
    ]
    
    for eq in test_equations:
        print(f"\n{'='*60}")
        print(f"Equation: {eq}")
        print('='*60)
        result = solver.solve_and_explain(eq)
        print(result)
