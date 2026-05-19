# 🧮 Math Buddy AI - Offline Math Solver

An intelligent offline AI-powered math solver that recognizes competitive exam questions through camera input and provides step-by-step solutions.

## ✨ Features

- 📷 **Real-time Camera Input** - Capture math problems directly from your device
- 🔍 **Advanced OCR** - Recognize handwritten and printed mathematical equations
- 🧮 **Smart Solver** - Solve algebra, equations, factorization, and more
- 📊 **Step-by-Step Solutions** - Understand each step of the solution
- 💻 **100% Offline** - No internet required, all processing is local
- 🖥️ **User-Friendly GUI** - Simple and intuitive interface

## 🎯 Supported Math Operations

- Linear Equations: `2x + 3 = 7`
- Quadratic Equations: `x² + 2x + 1 = 0`
- Expression Simplification
- Polynomial Expansion
- Factorization
- Algebraic Operations
- And much more!

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Webcam (for camera input)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/dineshkumar63/Math-Buddy-AI.git
cd Math-Buddy-AI
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Tesseract OCR (Required)

**Windows:**
- Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
- Run installer and note the installation path
- Set environment variable or update path in `ocr_processor.py`

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### Step 5: Run the Application
```bash
python main.py
```

## 📖 Usage

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Capture or Upload an Image**
   - Click "📸 Capture Image" to use webcam
   - Or click "📁 Upload Image" to select from file

3. **Solve the Problem**
   - Click "🧮 Solve" button
   - View step-by-step solution

4. **Copy or Save Results**
   - Results are displayed in the GUI
   - You can copy and save solutions

## 📁 Project Structure

```
Math-Buddy-AI/
├── main.py                 # Application entry point
├── gui_interface.py        # GUI using Tkinter
├── camera_module.py        # Camera capture functionality
├── ocr_processor.py        # Math OCR using Tesseract
├── math_solver.py          # Math solver engine using SymPy
├── examples.py             # Example usage
├── setup.py                # Setup script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Core Components

### 1. **main.py**
Entry point that initializes and runs the GUI application.

### 2. **gui_interface.py**
Tkinter-based GUI with:
- Image preview panel
- Camera capture button
- File upload button
- Solve button
- Results display panel

### 3. **camera_module.py**
Handles:
- Webcam initialization
- Real-time frame capture
- Image preprocessing
- Noise reduction

### 4. **ocr_processor.py**
Features:
- Tesseract OCR integration
- Math-specific preprocessing
- LaTeX equation extraction
- Error handling

### 5. **math_solver.py**
Powered by SymPy:
- Equation solving
- Expression simplification
- Symbolic computation
- Step-by-step solution generation

## 💡 Example Workflow

```python
from math_solver import MathSolver

solver = MathSolver()

# Example 1: Linear Equation
result = solver.solve_and_explain("2*x + 3 = 7")
print(result)
# Output: x = 2 (with detailed steps)

# Example 2: Quadratic Equation
result = solver.solve_and_explain("x**2 + 2*x + 1 = 0")
print(result)
# Output: x = -1 (with detailed steps)

# Example 3: Simplification
result = solver.simplify_expression("(x + 1)**2")
print(result)
# Output: x² + 2x + 1
```

## 🛠️ Technology Stack

- **Python 3.8+**
- **Tkinter** - GUI Framework
- **SymPy** - Symbolic Mathematics
- **OpenCV** - Image Processing
- **Tesseract** - OCR Engine
- **Pillow** - Image Handling
- **NumPy** - Numerical Computing

## 📝 Supported Equation Types

### Basic Operations
- Addition, Subtraction, Multiplication, Division
- Exponents and Powers
- Square Roots and Radicals

### Algebraic Equations
- Linear equations (1st degree)
- Quadratic equations (2nd degree)
- Polynomial equations
- Rational equations

### Trigonometry (Extended)
- Trigonometric functions
- Trigonometric equations

## 🚨 Troubleshooting

### Issue: "Tesseract is not installed"
**Solution:** Follow the Tesseract installation steps above for your OS

### Issue: Camera not working
**Solution:** 
- Check if another app is using the webcam
- Grant camera permissions to Python
- Try restarting the application

### Issue: OCR accuracy is low
**Solution:**
- Ensure good lighting
- Hold the equation clearly in frame
- Use printed or clearly written equations

### Issue: Import errors
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙋 Support

For issues, questions, or suggestions:
- Open a GitHub Issue
- Contact: dineshkumar63

## 🎓 Educational Use

This tool is designed for:
- Competitive exam preparation
- Math homework assistance
- Learning mathematical concepts
- Improving problem-solving skills

## 🔮 Future Enhancements

- [ ] Support for more advanced mathematical operations
- [ ] Multi-language support
- [ ] Cloud backup for solutions
- [ ] Mobile app version
- [ ] Batch processing of multiple problems
- [ ] Integration with other educational platforms
- [ ] AI-powered explanation generation

---

**Made with ❤️ for Math Learners Everywhere**

Happy Solving! 🚀
