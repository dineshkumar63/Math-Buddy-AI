#!/usr/bin/env python3
"""
Math Buddy AI - Flask Backend Server
Local server for Android app and desktop clients
All processing happens locally - NO CLOUD!
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from solvers.question_classifier import classify_question
from solvers.profit_loss_solver import ProfitLossSolver
from solvers.time_work_solver import TimeWorkSolver
from solvers.number_system_solver import NumberSystemSolver
from solvers.percentage_solver import PercentageSolver
from solvers.speed_distance_solver import SpeedDistanceSolver
from solvers.ratio_proportion_solver import RatioProportionSolver
from solvers.algebra_solver import AlgebraSolver
from solvers.geometry_solver import GeometrySolver
from tips.tips_database import TipsDatabase
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize solvers
solvers = {
    'profit_loss': ProfitLossSolver(),
    'time_work': TimeWorkSolver(),
    'number_system': NumberSystemSolver(),
    'percentage': PercentageSolver(),
    'speed_distance': SpeedDistanceSolver(),
    'ratio_proportion': RatioProportionSolver(),
    'algebra': AlgebraSolver(),
    'geometry': GeometrySolver()
}

# Initialize tips database
tips_db = TipsDatabase()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if server is running"""
    return jsonify({
        'status': 'online',
        'message': '🟢 Math Buddy AI Backend is running!',
        'version': '1.0.0'
    }), 200

@app.route('/api/solve', methods=['POST'])
def solve_question():
    """
    Main endpoint to solve questions
    Expected JSON:
    {
        'question': 'question text or equation',
        'question_type': 'optional - auto-detected if not provided'
    }
    """
    try:
        data = request.json
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        logger.info(f"Received question: {question}")
        
        # Classify question type if not provided
        question_type = data.get('question_type', None)
        if not question_type:
            question_type = classify_question(question)
        
        logger.info(f"Question type: {question_type}")
        
        # Get appropriate solver
        solver = solvers.get(question_type, solvers['algebra'])
        
        # Solve the question
        solution = solver.solve(question)
        
        # Get quick tips
        tips = tips_db.get_tips(question_type)
        
        # Get method
        method = solver.get_method()
        
        return jsonify({
            'status': 'success',
            'question': question,
            'question_type': question_type,
            'solution': solution,
            'tips': tips,
            'method': method
        }), 200
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/api/classify', methods=['POST'])
def classify():
    """Classify question type"""
    try:
        data = request.json
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        question_type = classify_question(question)
        
        return jsonify({
            'status': 'success',
            'question_type': question_type,
            'description': get_question_description(question_type)
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tips/<question_type>', methods=['GET'])
def get_tips(question_type):
    """Get quick tips for a question type"""
    try:
        tips = tips_db.get_tips(question_type)
        
        return jsonify({
            'status': 'success',
            'question_type': question_type,
            'tips': tips
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/question-types', methods=['GET'])
def get_question_types():
    """Get all supported question types"""
    return jsonify({
        'status': 'success',
        'question_types': [
            {
                'type': 'profit_loss',
                'name': 'Profit & Loss',
                'description': 'Solve profit, loss, discount, and markup problems'
            },
            {
                'type': 'time_work',
                'name': 'Time & Work',
                'description': 'Solve work completion, pipe & cistern problems'
            },
            {
                'type': 'number_system',
                'name': 'Number System',
                'description': 'Solve LCM, GCD, prime, divisibility problems'
            },
            {
                'type': 'percentage',
                'name': 'Percentage',
                'description': 'Calculate percentages and related problems'
            },
            {
                'type': 'speed_distance',
                'name': 'Speed, Distance & Time',
                'description': 'Solve train, boat, and relative speed problems'
            },
            {
                'type': 'ratio_proportion',
                'name': 'Ratio & Proportion',
                'description': 'Solve mixture and ratio-related problems'
            },
            {
                'type': 'algebra',
                'name': 'Algebra',
                'description': 'Solve equations and algebraic expressions'
            },
            {
                'type': 'geometry',
                'name': 'Geometry',
                'description': 'Calculate areas, perimeters, and geometric properties'
            }
        ]
    }), 200

def get_question_description(question_type):
    """Get description for question type"""
    descriptions = {
        'profit_loss': 'Profit & Loss problems',
        'time_work': 'Time & Work problems',
        'number_system': 'Number System problems',
        'percentage': 'Percentage problems',
        'speed_distance': 'Speed, Distance & Time problems',
        'ratio_proportion': 'Ratio & Proportion problems',
        'algebra': 'Algebra problems',
        'geometry': 'Geometry problems'
    }
    return descriptions.get(question_type, 'Unknown type')

@app.route('/', methods=['GET'])
def index():
    """Welcome page"""
    return jsonify({
        'name': '🧮 Math Buddy AI',
        'version': '1.0.0',
        'type': 'Backend Server (Local)',
        'status': 'Running',
        'features': [
            '📷 Camera-based question recognition',
            '🧮 All competitive exam question types',
            '📊 Step-by-step solutions',
            '⚡ Quick solving tips',
            '💾 100% Offline',
            '🆓 Completely Free'
        ],
        'endpoints': {
            'health': 'GET /api/health',
            'solve': 'POST /api/solve',
            'classify': 'POST /api/classify',
            'tips': 'GET /api/tips/<question_type>',
            'question_types': 'GET /api/question-types'
        }
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🧮 Math Buddy AI - Backend Server")
    print("="*70)
    print("\n✅ Starting Flask server...")
    print("📍 Local URL: http://localhost:5000")
    print("📍 Network URL: http://YOUR_IP:5000")
    print("\n📱 For Android app, use your PC IP address (e.g., 192.168.1.100)")
    print("\n" + "="*70 + "\n")
    
    # Run on all interfaces so Android can connect
    app.run(host='0.0.0.0', port=5000, debug=True)
