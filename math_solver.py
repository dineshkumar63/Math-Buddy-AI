#!/usr/bin/env python3
"""
Enhanced Math Solver Module for Math Buddy AI
Integrates all solver types: Basic, Word Problems, and Advanced
"""

from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import re
from word_problem_solver import WordProblemSolver
from advanced_math_solver import AdvancedMathSolver

class EnhancedMathSolver:
    def __init__(self):
        """Initialize enhanced math solver with all sub-solvers"""
        self.word_solver = WordProblemSolver()
        self.advanced_solver = AdvancedMathSolver()
        self.symbols_cache = {}
    
    def identify_problem_type(self, equation_str: str) -> str:
        """Identify if it's a word problem, advanced problem, or basic equation"""
        text_lower = equation_str.lower()
        
        # Word Problems indicators
        word_problem_keywords = [
            'problem', 'travel', 'speed', 'distance', 'hours', 'days', 'work', 'complete',
            'age', 'years', 'older', 'younger', 'cost', 'price', 'profit', 'loss',
            'percent', 'markup', 'discount', 'ratio', 'proportion', 'together'
        ]
        
        if any(keyword in text_lower for keyword in word_problem_keywords):
            return 'word_problem'
        
        # Advanced problem indicators
        advanced_keywords = [
            'derivative', 'differentiate', 'integral', 'integrate', 'limit', 'lim',
            'circle', 'rectangle', 'triangle', 'sphere', 'cylinder', 'cone',
            'statistics', 'mean', 'median', 'mode', 'matrix', 'determinant'
        ]
        
        if any(keyword in text_lower for keyword in advanced_keywords):
            return 'advanced'
        
        # Check if it's a word format equation
        if self.is_word_format_equation(equation_str):
            return 'word_equation'
        
        return 'basic'
    
    def is_word_format_equation(self, text: str) -> bool:
        """Check if equation is in word format (e.g., 'two x plus three equals seven')"""
        word_numbers = [
            'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen', 'twenty'
        ]
        
        word_operators = [
            'plus', 'minus', 'times', 'divided by', 'equals', 'is', 'equal to',
            'squared', 'cubed', 'square root', 'power'
        ]
        
        text_lower = text.lower()
        has_word_numbers = any(word in text_lower for word in word_numbers)
        has_word_operators = any(op in text_lower for op in word_operators)
        has_no_symbols = '=' not in text or '+' not in text
        
        return has_word_numbers or (has_word_operators and has_no_symbols)
    
    def convert_word_to_math(self, text: str) -> str:
        """Convert word format equation to mathematical format"""
        text = text.lower().strip()
        
        # Number words to digits
        word_to_num = {
            'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
            'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13',
            'fourteen': '14', 'fifteen': '15', 'sixteen': '16', 'seventeen': '17',
            'eighteen': '18', 'nineteen': '19', 'twenty': '20', 'thirty': '30',
            'forty': '40', 'fifty': '50', 'sixty': '60', 'seventy': '70',
            'eighty': '80', 'ninety': '90', 'hundred': '*100', 'thousand': '*1000'
        }
        
        # Replace word numbers
        for word, num in word_to_num.items():
            text = re.sub(r'\b' + word + r'\b', num, text)
        
        # Operator replacements
        text = re.sub(r'\bplus\b', '+', text)
        text = re.sub(r'\bminus\b', '-', text)
        text = re.sub(r'\btimes\b', '*', text)
        text = re.sub(r'\bdivided\s+by\b', '/', text)
        text = re.sub(r'\bequals?\b', '=', text)
        text = re.sub(r'\bis\b', '=', text)
        text = re.sub(r'\bequal\s+to\b', '=', text)
        text = re.sub(r'\bsquared\b', '**2', text)
        text = re.sub(r'\bcubed\b', '**3', text)
        text = re.sub(r'\bsquare\s+root\s+of\b', 'sqrt', text)
        text = re.sub(r'\bto\s+the\s+power\s+of\b', '**', text)
        
        # Add multiplication between number and variable
        text = re.sub(r'(\d)\s+([a-zA-Z])', r'\1*\2', text)
        
        # Clean up spaces
        text = re.sub(r'\s+', '', text)
        
        return text
    
    def solve_and_explain(self, equation_str: str) -> str:
        """Main solve method - routes to appropriate solver"""
        try:
            # Identify problem type
            problem_type = self.identify_problem_type(equation_str)
            
            if problem_type == 'word_problem':
                return self.word_solver.solve(equation_str)
            
            elif problem_type == 'advanced':
                return self.advanced_solver.solve(equation_str)
            
            elif problem_type == 'word_equation':
                # Convert word format to math format and solve
                math_equation = self.convert_word_to_math(equation_str)
                return self.solve_basic_equation(math_equation)
            
            else:
                return self.solve_basic_equation(equation_str)
        
        except Exception as e:
            return f"❌ Error solving problem: {str(e)}\n\nPlease check your input format."
    
    def solve_basic_equation(self, equation_str: str) -> str:
        """Solve basic mathematical equations"""
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
    
    def clean_equation_string(self, equation_str: str) -> str:
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
            
            # Add multiplication between variable and bracket
            equation_str = re.sub(r'([a-zA-Z])(\()', r'\1*\2', equation_str)
            
            return equation_str
        except:
            return equation_str
    
    def simplify_expression(self, expr_str: str) -> str:
        """Simplify mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            simplified = simplify(expr)
            return str(simplified)
        except:
            return "Error simplifying expression"
    
    def expand_expression(self, expr_str: str) -> str:
        """Expand mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            expanded = expand(expr)
            return str(expanded)
        except:
            return "Error expanding expression"
    
    def factor_expression(self, expr_str: str) -> str:
        """Factor mathematical expression"""
        try:
            expr = parse_expr(expr_str)
            factored = factor(expr)
            return str(factored)
        except:
            return "Error factoring expression"


if __name__ == "__main__":
    # Test solver
    solver = EnhancedMathSolver()
    
    # Test cases
    test_equations = [
        "2*x + 3 = 7",
        "two x plus three equals seven",
        "x**2 + 2*x + 1 = 0",
        "A car travels at 60 km/h for 3 hours. What distance?",
        "A can do work in 10 days, B in 15 days. How long together?",
        "derivative of x**2",
        "circle radius=5",
    ]
    
    for eq in test_equations:
        print(f"\n{'='*60}")
        print(f"Problem: {eq}")
        print('='*60)
        result = solver.solve_and_explain(eq)
        print(result)
