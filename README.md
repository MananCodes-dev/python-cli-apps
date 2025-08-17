# 🐍 Python CLI Tools – 100 Project Challenge

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/CLI-Tools-brightgreen?style=for-the-badge)](https://github.com/MananCodes-dev/python-cli-apps)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MananCodes-dev/python-cli-apps?style=for-the-badge)](https://github.com/MananCodes-dev/python-cli-apps/stargazers)

**A comprehensive collection of Python CLI applications built during my 100-day coding journey**

[🚀 Get Started](#-quick-start) • [📋 Project List](#-complete-project-index) • [🤝 Contributing](#-contributing) • [📬 Contact](#-connect-with-me)

</div>

---

## 🎯 About This Challenge

Welcome to my **100 Days of CLI Tools Challenge**! This repository chronicles my journey of building **100+ Python command-line applications** while mastering:

- 🐍 **Advanced Python Programming**
- 🤖 **AI/ML Fundamentals** 
- 🎮 **Game Development Concepts**
- 🔧 **Software Architecture & Design Patterns**

Every day, I create a new CLI tool, document the learning process, and share it publicly. From simple utilities to complex interpreters, each project builds upon the last.

### 📊 Current Progress
```
🎯 Goal: 100 CLI Tools
✅ Completed: 16+ Projects
🔥 Current Streak: 19+ Days
📈 Categories: 5 Different Types
🧮 Special: Custom Programming Language (MiniCalcLang)
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/MananCodes-dev/python-cli-apps.git
cd python-cli-apps

# Install dependencies (if any project requires them)
pip install -r requirements.txt

# Make scripts executable (Linux/Mac)
chmod +x */*.py

# Run any tool directly
python utilities/password_generator.py
```

### Quick Demo
```bash
# Try the password generator
python utilities/password_generator.py --length 16 --include-symbols

# Play a dice game
python games/dice_game.py

# Use the calculator
python calculators/mini_calculator.py
```

---

## 📂 Project Categories

<details open>
<summary><h3>🧮 Calculators & Math Tools</h3></summary>

| Project | Description | Key Features |
|---------|-------------|--------------|
| [Mini Calculator](./calculators/mini_calculator.py) | Basic arithmetic operations | Addition, subtraction, multiplication, division |
| [Unit Converter](./calculators/converter.py) | Convert between different units | Length, weight, temperature conversions |
| [Scientific Calculator](./calculators/scientific_calc.py) | Advanced mathematical operations | Trigonometry, logarithms, constants |

</details>

<details open>
<summary><h3>🎮 Games & Interactive Apps</h3></summary>

| Project | Description | Key Features |
|---------|-------------|--------------|
| [Dice Game](./games/dice_game.py) | Classic dice rolling game | Multiple players, scoring system |
| [Rock Paper Scissors](./games/rock_paper_scissors.py) | Traditional RPS game | Best of 3, score tracking |
| [Number Guessing Game](./games/number_guess.py) | Guess the random number | Difficulty levels, hint system |
| [Quiz Application](./games/quiz_app.py) | Interactive quiz with scoring | Multiple categories, timer |

</details>

<details open>
<summary><h3>⚡ Utilities & Productivity Tools</h3></summary>

| Project | Description | Key Features |
|---------|-------------|--------------|
| [Password Generator](./utilities/password_generator.py) | Secure password creation | Customizable length, character sets |
| [URL Shortener](./utilities/url_shortener.py) | Shorten long URLs | Custom aliases, click tracking |
| [YouTube Downloader](./utilities/youtube_downloader.py) | Download videos from YouTube | Multiple formats, quality selection |
| [Currency Converter](./utilities/currency_converter.py) | Real-time currency conversion | Live exchange rates, history |
| [File Organizer](./utilities/file_organizer.py) | Organize files by type/date | Batch operations, undo functionality |
| [QR Code Generator](./utilities/qr_generator.py) | Generate QR codes | Custom sizes, error correction |

</details>

<details open>
<summary><h3>💰 Tracking & Data Management</h3></summary>

| Project | Description | Key Features |
|---------|-------------|--------------|
| [Expense Tracker](./trackers/expense_tracker.py) | Track daily expenses | Categories, monthly reports, CSV export |
| [Task Manager](./trackers/task_manager.py) | Simple to-do list manager | Priority levels, due dates |
| [Habit Tracker](./trackers/habit_tracker.py) | Track daily habits | Streak counting, progress visualization |

</details>

<details open>
<summary><h3>🧑‍🔬 Language Development & Advanced</h3></summary>

| Project | Description | Key Features |
|---------|-------------|--------------|
| [**MiniCalcLang**](./language/) | My custom programming language! | Lexer, parser, interpreter, variables |
| [Tokenizer](./language/tokenizer.py) | Text tokenization utility | Multiple algorithms, custom patterns |
| [Expression Parser](./language/parser.py) | Mathematical expression parser | Recursive descent, operator precedence |

</details>

---

## 🛠️ Tech Stack & Libraries

### Core Technologies
- **Python 3.7+** - Main programming language
- **Standard Library** - os, sys, argparse, json, csv, sqlite3
- **External Libraries** - requests, pytube, qrcode, colorama

### Development Tools
- **IDE**: Visual Studio Code
- **Version Control**: Git & GitHub
- **Documentation**: Markdown
- **Planning**: Notion workspace

### Key Programming Concepts Demonstrated
- **CLI Argument Parsing** - Using argparse for user-friendly interfaces
- **File I/O Operations** - Reading, writing, and processing various file formats
- **API Integration** - Working with REST APIs and web services
- **Data Structures** - Lists, dictionaries, sets, and custom classes
- **Error Handling** - Robust exception handling and user feedback
- **Regex Processing** - Pattern matching and text manipulation
- **Object-Oriented Programming** - Classes, inheritance, and encapsulation

---

## 📋 Complete Project Index

### 🗂️ By Difficulty Level

<details>
<summary><strong>🟢 Beginner (1-5 days)</strong></summary>

- Hello World CLI
- Simple Calculator
- Number Guessing Game
- Rock Paper Scissors
- Dice Rolling Game

</details>

<details>
<summary><strong>🟡 Intermediate (6-12 days)</strong></summary>

- Password Generator
- Unit Converter
- Expense Tracker
- Quiz Application
- File Organizer
- QR Code Generator

</details>

<details>
<summary><strong>🔴 Advanced (13+ days)</strong></summary>

- YouTube Downloader
- Currency Converter (API)
- URL Shortener
- MiniCalcLang Interpreter
- Data Analysis Tools

</details>

### 📊 Project Statistics
```
Total Projects: 16+
Lines of Code: 2000+
Categories: 5
Average Project Time: 2-4 hours
Documentation Coverage: 100%
```

---

## 🌟 Featured Project: MiniCalcLang

### 🧮 My Custom Programming Language

The crown jewel of this repository is **MiniCalcLang** - a fully functional interpreted programming language designed for mathematical calculations.

#### Features
- ✅ **Lexical Analysis** - Custom tokenizer for language syntax
- ✅ **Recursive Descent Parser** - Handles operator precedence
- ✅ **Variable Assignment** - Store and retrieve values
- ✅ **Mathematical Operations** - All basic arithmetic
- 🚧 **Functions** - Custom function definitions (coming soon)
- 🚧 **Control Flow** - If statements and loops (planned)

#### Example Code
```python
# MiniCalcLang syntax
x = 10
y = 20
result = x * y + 5
print(result)  # Output: 205
```

[**🔗 View MiniCalcLang Documentation**](./language/README.md)

---

## 🎯 Learning Roadmap

### Phase 1: Foundations ✅
- [x] Basic CLI structure and argument parsing
- [x] File handling and data persistence
- [x] User input validation and error handling
- [x] Simple games and interactive applications

### Phase 2: Intermediate Tools ✅
- [x] API integration and web scraping
- [x] Data processing and analysis
- [x] System utilities and automation
- [x] Beginning language development

### Phase 3: Advanced Projects 🔄
- [ ] Machine learning CLI applications
- [ ] Web scraping and automation tools
- [ ] Database integration and management
- [ ] Network programming utilities

### Phase 4: AI Integration 🔮
- [ ] Natural language processing tools
- [ ] Computer vision applications
- [ ] Chatbot and AI assistants
- [ ] Machine learning model trainers

---

## 🔧 Development Workflow

### Daily Process
1. **🌅 Morning Planning** - Choose project scope and requirements
2. **💻 Development** - Write, test, and debug the application
3. **📝 Documentation** - Create README and usage examples
4. **🧪 Testing** - Manual testing and edge case handling
5. **📤 Publishing** - Commit, push, and update project index
6. **📱 Sharing** - Post progress on social media

### Code Quality Standards
- **PEP 8** - Python style guide compliance
- **Documentation** - Comprehensive README for each project
- **Error Handling** - Graceful failure and user feedback
- **User Experience** - Intuitive CLI interfaces
- **Modularity** - Clean, reusable code structure

---

## 🤝 Contributing

I welcome contributions, suggestions, and feedback! Here's how you can help:

### Ways to Contribute
- 🐛 **Report Bugs** - Found an issue? Open a GitHub issue
- 💡 **Suggest Features** - Ideas for new CLI tools or improvements
- 📖 **Improve Documentation** - Help make instructions clearer
- 🔧 **Code Contributions** - Submit pull requests for enhancements
- ⭐ **Star the Repository** - Show your support!

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-tool`)
3. Follow the existing code style and structure
4. Add documentation for new tools
5. Test your changes thoroughly
6. Submit a pull request with a clear description

---

## 📚 Learning Resources

### Python CLI Development
- [Click Documentation](https://click.palletsprojects.com/) - Advanced CLI framework
- [argparse Tutorial](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments) - Built-in argument parsing
- [Rich Library](https://github.com/willmcgugan/rich) - Beautiful terminal output

### Inspiration & Ideas
- [Build your own X](https://github.com/danistefanovic/build-your-own-x) - Project ideas
- [The Missing Semester](https://missing.csail.mit.edu/) - Command line tools
- [Python CLI Applications](https://realpython.com/command-line-interfaces-python-argparse/) - Real Python guide

---

## 📈 Project Analytics

### Development Timeline
```
Week 1: Basic utilities and games (5 projects)
Week 2: File processing and API integration (4 projects)  
Week 3: Advanced tools and language development (7+ projects)
Current: Expanding MiniCalcLang and AI integration planning
```

### Most Popular Tools (by complexity)
1. **MiniCalcLang** - Custom programming language
2. **YouTube Downloader** - Media utility with API integration
3. **Expense Tracker** - Data persistence and reporting
4. **Password Generator** - Security and cryptography
5. **Currency Converter** - Real-time API integration

---

## 🎉 Milestones & Achievements

- ✅ **Day 1**: First CLI tool completed
- ✅ **Day 5**: 5 tools milestone reached
- ✅ **Day 10**: First API-integrated tool
- ✅ **Day 15**: 15 tools milestone + custom language started
- ✅ **Day 18**: MiniCalcLang interpreter working
- 🎯 **Day 30**: Target for 30 tools (v1.0 release)
- 🎯 **Day 50**: AI-powered tools introduction
- 🎯 **Day 100**: Complete challenge with advanced projects

---

## 📬 Connect with Me

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/UnfilteredManan)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MananCodes-dev)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)

**Let's connect and learn together!**

</div>

### Follow My Journey
- 🐦 **Twitter**: [@UnfilteredManan](https://x.com/UnfilteredManan) - Daily updates and insights
- 💬 **Discord**: `manan_codes` - Direct messages and community
- 📧 **GitHub Issues** - Technical discussions and feedback

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You're free to:
- ✅ Use the code in your own projects
- ✅ Modify and distribute the tools
- ✅ Use for commercial purposes
- ✅ Learn from and build upon the examples

---

## 🙏 Acknowledgments

Special thanks to:
- **Python Community** - For amazing libraries and documentation
- **GitHub** - For providing an excellent platform for learning in public
- **Fellow Developers** - For inspiration and feedback
- **Open Source Contributors** - For the tools that make this possible

---

<div align="center">


**⭐ If you find this repository helpful, please consider giving it a star!**

*Built with ❤️, ☕, and lots of Python*

---

<sub>Last updated: August 2025 | Repository maintained by [@MananCodes-dev](https://github.com/MananCodes-dev)</sub>

</div>
