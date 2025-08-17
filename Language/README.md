# 🧮 MiniCalcLang – A Custom Calculator Language

A simple interpreted language built in Python that can evaluate math expressions.  
This project marks the **beginning of my language design journey** as part of the *100 Python CLI Tools Challenge*.  

---

## 🚀 Features
- Supports basic arithmetic: `+`, `-`, `*`, `/`  
- Handles parentheses: `(10 - 3) * 2`  
- Interactive **REPL (Read-Eval-Print Loop)**  
- Tokenizer + Evaluator design (baby steps into interpreters)  

---

## 🛠 Tech Stack
- **Language:** Python 3.x 🐍  
- **Libraries:** `re` (regex for tokenizing)

---
# 🧮 MiniCalcLang V2 - Programming Language with Variables

A simple mathematical programming language built in Python that supports variables, expressions, and interactive commands. Created as part of my 100-day developer roadmap journey.

## ✨ Features

### Core Functionality
- **Mathematical Expressions**: Basic arithmetic operations (+, -, *, /, parentheses)
- **Variables**: Assign and use variables in calculations
- **Interactive REPL**: Read-Eval-Print Loop for real-time interaction
- **Command History**: Track your previous commands
- **Error Handling**: Helpful error messages for debugging

### Supported Operations
```
# Basic math
>>> 5 + 3
8

# Variable assignment
>>> x = 10
x = 10

# Using variables in expressions
>>> y = x + 5
y = 15

# Complex expressions
>>> result = (x + y) * 2
result = 50
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No additional libraries required!

### Installation
1. Clone or download the `minicalclang_v2.py` file
2. Save it to your project directory (recommended: `language/` folder)

### Running MiniCalcLang V2
```bash
python minicalclang_v2.py
```

## 📖 Usage Guide

### Basic Commands
```
>>> help          # Show all available commands
>>> vars          # Display all defined variables
>>> history       # Show recent command history
>>> clear         # Clear all variables
>>> quit          # Exit the program
```

### Variable Operations
```
# Simple assignment
>>> age = 25

# Using variables in calculations
>>> next_year = age + 1

# Complex expressions with variables
>>> area = length * width
>>> perimeter = 2 * (length + width)
```

### Mathematical Expressions
```
# Parentheses for order of operations
>>> result = (10 + 5) * 2
result = 30

# Decimal numbers
>>> pi = 3.14159
>>> circle_area = pi * radius * radius
```

## 🧪 Example Session
```
🔢 MiniCalcLang V2 - Now with Variables!
Type 'help' for commands, 'quit' to exit
----------------------------------------
>>> x = 5
x = 5
>>> y = 3
y = 3
>>> sum = x + y
sum = 8
>>> product = x * y
product = 15
>>> vars
Variables:
  x = 5
  y = 3
  sum = 8
  product = 15
>>> result = (sum + product) * 2
result = 46
>>> quit
Goodbye! 👋
```

## 🔧 Technical Details

### Architecture
- **Tokenizer**: Breaks input into manageable tokens
- **Parser**: Identifies assignments vs expressions
- **Evaluator**: Safely executes mathematical operations
- **Variable Store**: Maintains variable state across commands

### Variable Rules
- Variable names must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (`x` and `X` are different variables)
- Cannot use Python reserved keywords

### Supported Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `10 - 4` |
| `*` | Multiplication | `7 * 6` |
| `/` | Division | `15 / 3` |
| `()` | Parentheses | `(2 + 3) * 4` |
| `=` | Assignment | `x = 10` |

## 🐛 Error Handling

The language provides helpful error messages:
```
>>> 5 /
Error: Math error: unexpected EOF while parsing

>>> unknown_var + 5
Error: Undefined variable: unknown_var

>>> 123abc = 5
Error: Assignment error: Invalid variable name: 123abc
```

## 📁 Project Structure
```
language/
├── minicalclang_v2.py      # Main language implementation
└── README.md               # This file
```

## 🎯 Learning Objectives

This project demonstrates:
- **Language Design**: Creating syntax and grammar rules
- **Parsing**: Converting text input into executable operations
- **State Management**: Maintaining variables across commands
- **Error Handling**: Providing user-friendly feedback
- **REPL Development**: Interactive programming environments

## 🚀 Future Enhancements (V3 Ideas)
- [ ] Functions and procedures
- [ ] Conditional statements (if/else)
- [ ] Loops (for/while)
- [ ] String operations
- [ ] File I/O capabilities
- [ ] Better syntax highlighting

## 🤝 Contributing

This is a learning project, but suggestions are welcome! Areas for improvement:
- Additional mathematical functions (sin, cos, sqrt)
- Better error messages
- Performance optimizations
- Extended data types

## 📚 Resources Used

- **Learning References**: Python documentation, compiler design basics
- **Development Day**: Day 20 of 100-day developer roadmap
- **Focus Area**: Language development and variable systems

## 📝 Version History

- **V1**: Basic calculator with arithmetic operations
- **V2**: Added variables, history, and enhanced commands
- **Next**: Planning functions and control structures

## 👨‍💻 Author

Built as part of my journey to become a software developer. Day 20 focus: AI Integration and Language Enhancement.

---

**Try it out!** Start with simple math, then experiment with variables. The interactive nature makes it perfect for learning programming concepts.

*Happy calculating! 🔢*
