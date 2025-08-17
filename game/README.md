# 🎮 Python CLI Games Collection

Interactive command-line games built with Python, designed to entertain while demonstrating core programming concepts like random number generation, game logic, user input handling, and score tracking.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Games](https://img.shields.io/badge/Games-2-green.svg)](#games-overview)
[![CLI](https://img.shields.io/badge/Interface-CLI-yellow.svg)](#)

---

## 🚀 Quick Start

```bash
# Navigate to the games directory
cd python-cli-apps/game

# Run any game
python <game-name>.py

# Examples
python dice_game.py
python rock_paper_scissors.py
```

---

## 🎯 Games Overview

| Game | Difficulty | Concepts Demonstrated | Play Time |
|------|------------|----------------------|-----------|
| **[Dice Rolling Game](#-dice-rolling-game)** | Beginner | Random generation, loops, user input | 2-5 mins |
| **[Rock Paper Scissors](#-rock-paper-scissors)** | Beginner | Game logic, score tracking, conditionals | 5-10 mins |

---

## 🎲 Dice Rolling Game

A classic dice simulator that demonstrates fundamental Python concepts in an engaging way.

### 🌟 Features
- **Realistic Dice Simulation** - Uses Python's `random` module for true randomness
- **Continuous Play Loop** - Roll as many times as you want
- **Clean Interface** - Intuitive command-line experience
- **Instant Results** - Immediate feedback on each roll

### 🎯 Learning Objectives
- **Random Number Generation** - Understanding `random.randint()`
- **User Input Validation** - Handling user choices gracefully
- **Loop Control** - Implementing while loops for continuous gameplay
- **Basic CLI Design** - Creating user-friendly interfaces

### 🚀 How to Play
```bash
python dice_game.py
```

**Gameplay:**
1. Run the program
2. Press Enter to roll the dice
3. See your random result (1-6)
4. Choose to roll again or exit

### 💡 Code Highlights
- Utilizes `random.randint(1, 6)` for authentic dice behavior
- Implements input validation for smooth user experience
- Demonstrates clean code structure and readability

---

## ✊🖐✌️ Rock Paper Scissors

The timeless hand game reimagined for the command line, featuring intelligent computer opponents and comprehensive score tracking.

### 🌟 Features
- **Player vs Computer** - Challenge the AI opponent
- **Live Scoreboard** - Real-time win/loss/tie tracking
- **Smart AI Logic** - Computer makes random strategic choices
- **Round-based Gameplay** - Play single rounds or extended sessions
- **Input Validation** - Handles invalid inputs gracefully
- **Game Statistics** - Track your performance over time

### 🎯 Learning Objectives
- **Conditional Logic** - Complex if/elif/else structures
- **Data Structures** - Score tracking with variables/dictionaries
- **Random Selection** - `random.choice()` for AI decisions
- **String Handling** - Input processing and comparison
- **Game State Management** - Maintaining game flow and user experience

### 🚀 How to Play
```bash
python rock_paper_scissors.py
```

**Gameplay:**
1. Choose your move: Rock (r), Paper (p), or Scissors (s)
2. Computer makes its choice automatically
3. See the results and updated scoreboard
4. Continue playing or quit anytime

### 🏆 Game Rules
- **Rock** beats Scissors
- **Scissors** beats Paper  
- **Paper** beats Rock
- Same choice = Tie

### 📊 Score Tracking
The game maintains a persistent scoreboard showing:
- **Wins** - Your victories
- **Losses** - Computer victories  
- **Ties** - Draw games
- **Win Rate** - Performance percentage

---

## 🛠 Technical Details

### Requirements
- **Python 3.6+** - Core language requirement
- **Standard Library Only** - No external dependencies needed
- **Cross-Platform** - Works on Windows, macOS, and Linux

### Core Libraries Used
```python
import random  # For dice rolls and computer choices
import os      # For screen clearing (optional enhancement)
import sys     # For clean exits
```

### Code Architecture
Both games follow clean, modular design principles:
- **Separation of Concerns** - Game logic separated from user interface
- **DRY Principle** - Reusable functions for common operations
- **Error Handling** - Graceful handling of invalid inputs
- **Readable Code** - Clear variable names and commenting

---

## 🎓 Educational Value

### Programming Concepts Covered
1. **Random Number Generation** - `random` module usage
2. **Control Flow** - Loops, conditionals, and program flow
3. **User Input Handling** - `input()` function and validation
4. **String Operations** - Comparison, formatting, and manipulation
5. **Function Design** - Modular programming approaches
6. **Game Logic Implementation** - Win/loss condition handling

### Skill Progression
- **Beginners** - Learn fundamental Python syntax and logic
- **Intermediate** - Understand program structure and user experience design
- **Advanced** - Study code organization and best practices

---

## 🚀 Usage Examples

### Dice Game Session
```bash
$ python dice_game.py
🎲 Welcome to Dice Rolling Game!
=============================
Press Enter to roll the dice (or 'q' to quit): 

🎲 You rolled: 4

Press Enter to roll again (or 'q' to quit): 

🎲 You rolled: 6

Great roll! Press Enter to continue (or 'q' to quit): q
Thanks for playing! 🎲
```

### Rock Paper Scissors Match
```bash
$ python rock_paper_scissors.py
✊🖐✌️ Rock Paper Scissors Game
==============================
Choose: (r)ock, (p)aper, (s)cissors, or (q)uit: r

You chose: Rock 🪨
Computer chose: Scissors ✂️
You win! Rock beats Scissors!

📊 SCOREBOARD:
Wins: 1 | Losses: 0 | Ties: 0
Win Rate: 100.0%

Choose: (r)ock, (p)aper, (s)cissors, or (q)uit: 
```

---

## 🔧 Development

### Running the Games
```bash
# Clone the parent repository
git clone https://github.com/MananCodes-dev/python-cli-apps.git
cd python-cli-apps/game

# Run individual games
python dice_game.py
python rock_paper_scissors.py
```

### Customization Ideas
- **Dice Game Enhancements:**
  - Multiple dice rolling
  - Different sided dice (d4, d8, d12, d20)
  - Roll statistics and history
  - Dice game variants (Yahtzee mechanics)

- **Rock Paper Scissors Improvements:**
  - Best of N rounds tournaments
  - Different AI difficulty levels
  - Rock Paper Scissors Lizard Spock variant
  - Multiplayer support
  - Visual ASCII art representations

### Code Quality
Both games demonstrate:
- ✅ **Clean Code** - Readable and well-structured
- ✅ **Error Handling** - Robust input validation
- ✅ **User Experience** - Intuitive and engaging interfaces
- ✅ **Documentation** - Clear comments and docstrings

---

## 🎯 Future Enhancements

### Planned Features
- [ ] **Save Game State** - Persistent high scores and statistics
- [ ] **GUI Versions** - Tkinter-based graphical interfaces
- [ ] **Multiplayer Support** - Network-based player vs player
- [ ] **Tournament Mode** - Bracketed competitions
- [ ] **Achievement System** - Unlockable rewards and milestones
- [ ] **Sound Effects** - Audio feedback for actions
- [ ] **Themes** - Different visual styles and color schemes

### Advanced Game Ideas
- [ ] **Blackjack** - Card game with betting mechanics
- [ ] **Tic Tac Toe** - Strategic board game with AI
- [ ] **Hangman** - Word guessing with categories
- [ ] **Number Guessing** - Adaptive difficulty levels
- [ ] **Quiz Game** - Trivia with multiple categories

---

## 🤝 Contributing

Want to add new games or improve existing ones? Contributions are welcome!

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/NewGame`)
3. **Add** your game following the existing structure
4. **Test** thoroughly across different scenarios
5. **Document** your code and update this README
6. **Submit** a Pull Request

### Contribution Guidelines
- Follow existing code style and structure
- Include comprehensive error handling
- Add clear documentation and examples
- Test edge cases and invalid inputs
- Update README with game description and features

---

## 📚 Learning Resources

### Python Concepts References
- **Random Module**: [Python Documentation](https://docs.python.org/3/library/random.html)
- **Input Handling**: [Real Python Tutorial](https://realpython.com/python-input-output/)
- **Control Flow**: [Python.org Guide](https://docs.python.org/3/tutorial/controlflow.html)
- **Game Development**: [Python Game Programming Patterns](https://gameprogrammingpatterns.com/)

### Next Steps
After mastering these games, consider exploring:
- **Pygame** - For 2D game development
- **Tkinter** - For GUI applications
- **Flask/Django** - For web-based games
- **AI/ML** - For intelligent game opponents

---

## 🏆 Achievements

Building these games demonstrates mastery of:
- ✅ **Core Python Syntax** - Variables, functions, loops, conditionals
- ✅ **User Interface Design** - CLI interaction patterns
- ✅ **Game Logic Implementation** - Rules, scoring, win conditions
- ✅ **Random Number Generation** - Probability and chance mechanics
- ✅ **Error Handling** - Robust input validation
- ✅ **Code Organization** - Clean, readable, maintainable structure

---

## 👨‍💻 About the Developer

Created by **Manan** as part of the **100 Python CLI Tools Challenge** - a journey to master Python development through practical, engaging projects.

### Connect
- **GitHub**: [@MananCodes-dev](https://github.com/MananCodes-dev)
- **Twitter**: [@UnfilteredManan](https://twitter.com/UnfilteredManan)
- **Project**: [Python CLI Apps Collection](https://github.com/MananCodes-dev/python-cli-apps)

---

## 📄 License

This project is part of the larger Python CLI Apps collection and follows the same MIT License terms.

---

*🎮 Built for fun, designed for learning, and created to inspire others to explore the joy of programming through games!*

**Ready to play? Choose your game and let the fun begin!** 🚀
