#!/usr/bin/env python3
"""
Word Problem Solver for Math Buddy AI
Handles distance, speed, time, work, age, profit/loss problems
Uses NLP and pattern matching to extract and solve word problems
"""

from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import re
from typing import Dict, Tuple, List

class WordProblemSolver:
    def __init__(self):
        """Initialize word problem solver"""
        self.problem_types = {
            'distance': self.solve_distance_problem,
            'work': self.solve_work_problem,
            'age': self.solve_age_problem,
            'profit': self.solve_profit_problem,
            'percentage': self.solve_percentage_problem,
            'ratio': self.solve_ratio_problem,
        }
    
    def identify_problem_type(self, text: str) -> str:
        """Identify the type of word problem"""
        text_lower = text.lower()
        
        # Distance/Speed/Time problems
        if any(word in text_lower for word in ['speed', 'km/h', 'mph', 'distance', 'travel', 'hours', 'minutes']):
            return 'distance'
        
        # Work problems
        if any(word in text_lower for word in ['work', 'complete', 'days', 'hours', 'together', 'can do']):
            if 'age' not in text_lower:
                return 'work'
        
        # Age problems
        if any(word in text_lower for word in ['age', 'years', 'older', 'younger', 'born']):
            return 'age'
        
        # Profit/Loss problems
        if any(word in text_lower for word in ['profit', 'loss', 'cost price', 'selling price', 'markup', 'discount']):
            return 'profit'
        
        # Percentage problems
        if any(word in text_lower for word in ['percent', '%', 'percentage', 'increased', 'decreased']):
            return 'percentage'
        
        # Ratio problems
        if any(word in text_lower for word in ['ratio', 'proportion', 'times']):
            return 'ratio'
        
        return 'general'
    
    def extract_numbers(self, text: str) -> List[float]:
        """Extract all numbers from text"""
        numbers = re.findall(r'\d+\.?\d*', text)
        return [float(n) for n in numbers]
    
    def solve_distance_problem(self, text: str) -> str:
        """Solve distance = speed × time problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "🚗 DISTANCE/SPEED/TIME PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            # Extract what we know
            solution += "📊 Given Information:\n"
            
            # Pattern: "A travels at X km/h for Y hours"
            if 'speed' in text_lower and 'time' in text_lower and 'distance' not in text_lower:
                if len(numbers) >= 2:
                    speed, time_hours = numbers[0], numbers[1]
                    distance = speed * time_hours
                    solution += f"  • Speed: {speed} km/h\n"
                    solution += f"  • Time: {time_hours} hours\n\n"
                    solution += "📐 Formula: Distance = Speed × Time\n\n"
                    solution += f"Distance = {speed} × {time_hours}\n"
                    solution += f"Distance = {distance} km\n\n"
                    solution += f"✅ ANSWER: {distance} km\n"
                    return solution
            
            # Pattern: "A travels X km at Y km/h, how many hours?"
            if 'distance' in text_lower and 'speed' in text_lower and 'time' not in text_lower:
                if len(numbers) >= 2:
                    distance, speed = numbers[0], numbers[1]
                    time_hours = distance / speed
                    solution += f"  • Distance: {distance} km\n"
                    solution += f"  • Speed: {speed} km/h\n\n"
                    solution += "📐 Formula: Time = Distance ÷ Speed\n\n"
                    solution += f"Time = {distance} ÷ {speed}\n"
                    solution += f"Time = {time_hours:.2f} hours\n\n"
                    solution += f"✅ ANSWER: {time_hours:.2f} hours\n"
                    return solution
            
            # Pattern: "A travels for X hours, covering Y km. Speed?"
            if 'time' in text_lower and 'distance' in text_lower and 'speed' not in text_lower:
                if len(numbers) >= 2:
                    time_hours, distance = numbers[0], numbers[1]
                    speed = distance / time_hours
                    solution += f"  • Time: {time_hours} hours\n"
                    solution += f"  • Distance: {distance} km\n\n"
                    solution += "📐 Formula: Speed = Distance ÷ Time\n\n"
                    solution += f"Speed = {distance} ÷ {time_hours}\n"
                    solution += f"Speed = {speed:.2f} km/h\n\n"
                    solution += f"✅ ANSWER: {speed:.2f} km/h\n"
                    return solution
            
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve_work_problem(self, text: str) -> str:
        """Solve work rate problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "👷 WORK RATE PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            # Pattern: "A can do work in X days, B in Y days, together?"
            if 'together' in text_lower and len(numbers) >= 2:
                days_a, days_b = numbers[0], numbers[1]
                solution += f"Given Information:\n"
                solution += f"  • A completes work in: {days_a} days\n"
                solution += f"  • B completes work in: {days_b} days\n\n"
                
                solution += "📐 Solution:\n"
                solution += f"Work rate of A per day = 1/{days_a}\n"
                solution += f"Work rate of B per day = 1/{days_b}\n\n"
                
                rate_together = (1/days_a) + (1/days_b)
                time_together = 1 / rate_together
                
                solution += f"Combined rate = 1/{days_a} + 1/{days_b}\n"
                solution += f"Combined rate = {rate_together:.4f}\n\n"
                solution += f"Time to complete together = 1 ÷ {rate_together:.4f}\n"
                solution += f"Time to complete together = {time_together:.2f} days\n\n"
                solution += f"✅ ANSWER: {time_together:.2f} days\n"
                return solution
        
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve_age_problem(self, text: str) -> str:
        """Solve age problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "👨 AGE PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            # Pattern: "A is X years older than B. A is Y times B's age. Find ages."
            if len(numbers) >= 2:
                diff = numbers[0]
                
                if 'times' in text_lower:
                    ratio = numbers[1]
                    # Let B's age = x, then A's age = x + diff
                    # A = ratio * B
                    # x + diff = ratio * x
                    x = diff / (ratio - 1)
                    age_b = x
                    age_a = age_b + diff
                    
                    solution += f"Given:\n"
                    solution += f"  • Difference in age: {diff} years\n"
                    solution += f"  • A is {ratio} times B's age\n\n"
                    solution += f"Let B's age = x\n"
                    solution += f"Then A's age = x + {diff}\n\n"
                    solution += f"Equation: x + {diff} = {ratio}x\n"
                    solution += f"{diff} = {ratio}x - x\n"
                    solution += f"{diff} = {ratio - 1}x\n"
                    solution += f"x = {diff} ÷ {ratio - 1}\n"
                    solution += f"x = {x:.1f}\n\n"
                    solution += f"✅ ANSWER:\n"
                    solution += f"  • B's age: {age_b:.1f} years\n"
                    solution += f"  • A's age: {age_a:.1f} years\n"
                    return solution
        
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve_profit_problem(self, text: str) -> str:
        """Solve profit/loss problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "💰 PROFIT/LOSS PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            if 'cost' in text_lower and 'markup' in text_lower and len(numbers) >= 2:
                cost_price = numbers[0]
                markup_percent = numbers[1]
                
                solution += f"Given:\n"
                solution += f"  • Cost Price: ${cost_price}\n"
                solution += f"  • Markup: {markup_percent}%\n\n"
                
                markup_amount = (markup_percent / 100) * cost_price
                selling_price = cost_price + markup_amount
                
                solution += f"📐 Solution:\n"
                solution += f"Markup Amount = (Markup% / 100) × Cost Price\n"
                solution += f"Markup Amount = ({markup_percent} / 100) × {cost_price}\n"
                solution += f"Markup Amount = ${markup_amount}\n\n"
                solution += f"Selling Price = Cost Price + Markup\n"
                solution += f"Selling Price = ${cost_price} + ${markup_amount}\n"
                solution += f"Selling Price = ${selling_price}\n\n"
                solution += f"✅ ANSWER: ${selling_price}\n"
                return solution
        
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve_percentage_problem(self, text: str) -> str:
        """Solve percentage problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "📊 PERCENTAGE PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            if len(numbers) >= 2:
                total = numbers[0]
                percent = numbers[1]
                
                solution += f"Given:\n"
                solution += f"  • Total: {total}\n"
                solution += f"  • Percentage: {percent}%\n\n"
                
                result = (percent / 100) * total
                
                solution += f"📐 Solution:\n"
                solution += f"Result = (Percentage / 100) × Total\n"
                solution += f"Result = ({percent} / 100) × {total}\n"
                solution += f"Result = {result}\n\n"
                solution += f"✅ ANSWER: {result}\n"
                return solution
        
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve_ratio_problem(self, text: str) -> str:
        """Solve ratio and proportion problems"""
        solution = "\n" + "="*60 + "\n"
        solution += "⚖️ RATIO PROBLEM\n"
        solution += "="*60 + "\n\n"
        
        try:
            text_lower = text.lower()
            numbers = self.extract_numbers(text)
            solution += f"Problem: {text}\n\n"
            
            if len(numbers) >= 3:
                a, b, c = numbers[0], numbers[1], numbers[2]
                # a:b = c:x
                x = (b * c) / a
                
                solution += f"Given Ratio: {a}:{b} = {c}:x\n\n"
                solution += f"📐 Solution:\n"
                solution += f"x = (b × c) / a\n"
                solution += f"x = ({b} × {c}) / {a}\n"
                solution += f"x = {b * c} / {a}\n"
                solution += f"x = {x}\n\n"
                solution += f"✅ ANSWER: {a}:{b} = {c}:{x}\n"
                return solution
        
        except Exception as e:
            solution += f"❌ Error: {str(e)}\n"
        
        return solution
    
    def solve(self, text: str) -> str:
        """Main method to solve word problems"""
        problem_type = self.identify_problem_type(text)
        
        if problem_type in self.problem_types:
            return self.problem_types[problem_type](text)
        
        return f"❌ Could not identify problem type.\nSupported types: distance, work, age, profit, percentage, ratio"


if __name__ == "__main__":
    solver = WordProblemSolver()
    
    # Test problems
    test_problems = [
        "A car travels at 60 km/h for 3 hours. What distance does it cover?",
        "A train travels 300 km in 5 hours. What is its speed?",
        "A can complete work in 10 days. B can complete it in 15 days. How long together?",
        "John is 5 years older than Mary. If John is 2 times Mary's age, find their ages.",
        "Cost price is 100. Markup is 20%. What is selling price?",
        "Find 25% of 200.",
        "If 3:5 = 12:x, find x."
    ]
    
    for problem in test_problems:
        print(solver.solve(problem))
