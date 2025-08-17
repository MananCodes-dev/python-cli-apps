# 🐍 Python CLI Applications Collection

A comprehensive collection of command-line tools built with Python, covering utilities, games, productivity tools, and AI-powered applications. Perfect for learning Python development, exploring APIs, and building practical CLI tools.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/MananCodes-dev/python-cli-apps)](https://github.com/MananCodes-dev/python-cli-apps/stargazers)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/MananCodes-dev/python-cli-apps.git
cd python-cli-apps

# Install common dependencies
pip install -r requirements.txt

# Run any application
python <app-name>.py
```

---

## 📦 Applications Overview

### 💰 Financial Tools
| App | Description | Key Features |
|-----|-------------|--------------|
| **[Currency Converter](./currency_converter.py)** | Real-time currency conversion | 160+ currencies, ExchangeRate API |

### 📝 Productivity Tools
| App | Description | Key Features |
|-----|-------------|--------------|
| **[Notes App](./notes_app.py)** | Simple note-taking tool | Add, view, delete notes |
| **[Text Analyzer](./simple_text_analyzer.py)** | AI-powered text analysis | Sentiment analysis, statistics |
| **[Typing Speed Test](./typing_speed_test.py)** | Measure typing performance | WPM calculation, accuracy tracking |

### 🔧 Utility Tools
| App | Description | Key Features |
|-----|-------------|--------------|
| **[Number System Converter](./number_converter.py)** | Convert between number systems | Binary, Decimal, Hexadecimal |
| **[Password Strength Checker](./password_strength_checker.py)** | Evaluate password security | Strength scoring, recommendations |
| **[URL Shortener](./url_shortener.py)** | Shorten long URLs | TinyURL integration |

### 🌐 Web & Media Tools
| App | Description | Key Features |
|-----|-------------|--------------|
| **[Weather App](./weather_app.py)** | Real-time weather data | OpenWeatherMap API integration |
| **[YouTube Downloader](./youtube_downloader.py)** | Download YouTube videos | Multiple resolutions, pytube library |

---

## 🛠 Tech Stack

### Core Technologies
- **Python 3.6+** - Primary programming language
- **Command Line Interface** - User interaction
- **RESTful APIs** - External data integration

### Key Libraries
- `requests` - HTTP requests for APIs
- `textblob` - Natural language processing
- `pytube` - YouTube video downloading
- `nltk` - Advanced text processing

### APIs Used
- **ExchangeRate API** - Currency conversion rates
- **OpenWeatherMap API** - Weather data
- **TinyURL API** - URL shortening service

---

## 📋 Installation Guide

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Internet connection (for API-dependent tools)

### Step-by-Step Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/MananCodes-dev/python-cli-apps.git
   cd python-cli-apps
   ```

2. **Install Dependencies**
   ```bash
   # Install common packages
   pip install requests textblob pytube

   # For AI text analyzer (one-time setup)
   python -m textblob.download_corpora
   ```

3. **API Configuration** (if needed)
   - Weather App: Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Replace `YOUR_API_KEY` in respective files

---

## 🎯 Featured Applications

### 🤖 AI Text Analyzer
> **Day 20** of 100 Python CLI Tools Challenge - First AI-Powered Tool!

**Highlights:**
- Real sentiment analysis using machine learning
- Processes emotions in text (positive/negative/neutral)
- Built-in error handling and fallback methods
- Educational tool for understanding NLP concepts

```bash
python simple_text_analyzer.py "I love programming!"
# Output: Sentiment: Positive 😊 | Score: 0.85
```

### 💱 Currency Converter
Real-time exchange rates for 160+ currencies with graceful error handling.

```bash
python currency_converter.py
# Interactive mode with live exchange rates
```

### 🔐 Password Strength Checker
Comprehensive password analysis with detailed feedback.

```bash
python password_strength_checker.py
# Analyzes: length, complexity, character types
```

---

## 🚀 Usage Examples

### Basic Usage Pattern
```bash
# Most apps follow this pattern:
python <app_name>.py

# Some support command-line arguments:
python simple_text_analyzer.py "Your text here"
```

### Interactive Mode
Most applications provide an interactive CLI interface:
```
$ python notes_app.py
Welcome to Python Notes App!
1. Add Note
2. View Notes
3. Delete All Notes
4. Exit
Choose option: 
```

---

## 🔧 Development

### Project Structure
```
python-cli-apps/
├── README.md
├── requirements.txt
├── utilities/
│   ├── currency_converter.py
│   ├── notes_app.py
│   ├── simple_text_analyzer.py
│   └── ...
└── docs/
    └── individual_app_docs/
```

### Adding New Applications
1. Follow the existing naming convention
2. Include proper error handling
3. Add comprehensive docstrings
4. Update this README with your app details
5. Create individual documentation if complex

---

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
pip install <missing-module>
```

**TextBlob/NLTK errors:**
```bash
python -m textblob.download_corpora
```

**API-related errors:**
- Verify your API keys are correctly configured
- Check your internet connection
- Ensure API rate limits aren't exceeded

### Getting Help
- Check individual app documentation
- Open an issue on GitHub
- Review the troubleshooting sections in app-specific docs

---

## 🎓 Learning Path

This collection serves as a progression through Python development:

1. **Beginner** (Notes App, Password Checker)
2. **Intermediate** (API integration, Number Converter)
3. **Advanced** (AI integration, Media processing)

Each application builds upon previous concepts while introducing new technologies and patterns.

---

## 🌟 Use Cases

### Educational
- Learn Python CLI development
- Understand API integration
- Explore AI/ML concepts
- Practice file handling and data processing

### Professional
- Productivity enhancement tools
- Development utilities
- Automation scripts
- Portfolio demonstration

### Personal
- Daily utility tools
- Text analysis for content creation
- Media downloading and processing
- Financial calculations

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow existing code style and structure
- Include proper documentation
- Add error handling and input validation
- Test your code thoroughly
- Update README if adding new features

---

## 📈 Roadmap

### Planned Features
- [ ] **GUI versions** of popular CLI tools
- [ ] **Database integration** for data persistence
- [ ] **Advanced AI features** (language detection, summarization)
- [ ] **Batch processing** capabilities
- [ ] **Configuration files** for user preferences
- [ ] **Plugin system** for extensibility

### Version History
- **v1.0** - Initial collection of basic CLI tools
- **v1.1** - Added AI-powered text analyzer
- **v1.2** - Enhanced error handling across all apps
- **Current** - Comprehensive documentation and structure

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 About the Developer

**Manan** - Aspiring AI/ML and Game Developer
- 🎯 **Mission:** 4-year journey to master AI/ML and Game Development
- 📅 **Challenge:** 100 Python CLI Tools in 100 Days
- 🚀 **Progress:** Building and sharing daily coding projects

### Connect with Me
- **GitHub:** [@MananCodes-dev](https://github.com/MananCodes-dev)
- **Twitter:** [@UnfilteredManan](https://twitter.com/UnfilteredManan)
- **Project:** [100 Python CLI Tools Challenge](https://github.com/MananCodes-dev/python-cli-apps)

---

## 🏆 Achievements

- ✅ **First AI Integration** - Built AI-powered text analyzer
- ✅ **API Master** - Integrated multiple external APIs
- ✅ **Error Handling Pro** - Comprehensive error management
- ✅ **Documentation Expert** - Detailed project documentation
- ✅ **Community Builder** - Open source contribution

---

## ⭐ Support

If you find this project helpful:
- Give it a ⭐ on GitHub
- Share it with fellow developers
- Contribute to make it better
- Follow for more exciting projects!

---

*Built with ❤️ and a passion for learning Python development*

**Day 20+** of my journey to master programming. Every day brings new challenges and growth! 🚀
