# 💱 Currency Converter (CLI)

A Python command-line tool that converts between any two currencies in real-time using the [ExchangeRate API](https://www.exchangerate-api.com/).

---

## 🚀 Features
- Real-time exchange rates
- Supports 160+ currencies
- Easy CLI interface
- Handles invalid inputs gracefully

---

## 🛠 Tech Stack
- **Language:** Python 3.x 🐍
- **Libraries:** `requests`
- **API:** [ExchangeRate API](https://www.exchangerate-api.com/)

---

## 📦 Installation
```bash
git clone https://github.com/MananCodes-dev/python-cli-apps.git
cd python-cli-apps
```

# 🗒 Python Notes App

Simple CLI note-taking tool using file handling in Python.  
Notes are stored in `notes.txt` and can be viewed or deleted later.

## Features:
- Add text notes
- View saved notes
- Delete all notes

## How to Run
```
python notes_app.py
```
# 🔢 Python Number System Converter

CLI tool to convert between Binary, Decimal, and Hexadecimal numbers.

## Features:
- Binary ↔ Decimal
- Decimal ↔ Binary
- Decimal ↔ Hex
- Hex ↔ Decimal
- Input validation included

## How to Run:
```
python number_converter.py
```
# 🔐 Python Password Strength Checker

This Python CLI tool checks the strength of a password using:
- Length
- Uppercase + lowercase
- Digits
- Special characters

## Output:
- Weak / Medium / Strong

## Run it:
````

python password_strength_checker.py

````
# 📝 Simple Text Analyzer

**Day 20** of 100 Python CLI Tools Challenge | My First AI-Powered Tool! 🤖

A beginner-friendly text analysis tool that uses artificial intelligence to understand and analyze text. This is my first step into the world of AI and machine learning!

## ✨ What It Does

- **🎭 Sentiment Analysis**: Detects if text is positive, negative, or neutral
- **📊 Text Statistics**: Counts words, sentences, and characters
- **🧠 AI-Powered**: Uses machine learning (TextBlob) for real sentiment detection
- **⚡ Easy to Use**: Simple command-line interface
- **🛡️ Error Handling**: Won't crash if something goes wrong

## 🚀 Quick Start

### Installation
```bash
# Install required library
pip install textblob

# Download AI models (one-time setup)
python -m textblob.download_corpora
```

### Usage
```bash
# Analyze text directly
python simple_text_analyzer.py "I love programming!"

# Interactive mode
python simple_text_analyzer.py
```

## 📖 Examples

### Positive Text
```bash
$ python simple_text_analyzer.py "I'm so excited about learning AI!"

📝 Simple Text Analyzer - Day 20
========================================
🤖 TextBlob found! Setting up...
✅ NLTK data ready!

Analyzing: 'I'm so excited about learning AI!'

📊 RESULTS:
Sentiment: Positive 😊
Score: 0.85 (Range: -1 to 1)
Words: 7
Sentences: 1
Average words per sentence: 7.0

✅ Day 20 complete!
```

### Negative Text
```bash
$ python simple_text_analyzer.py "This is the worst day ever"

📊 RESULTS:
Sentiment: Negative 😔
Score: -0.95 (Range: -1 to 1)
Words: 6
Sentences: 1
```

### Neutral Text
```bash
$ python simple_text_analyzer.py "The sky is blue today"

📊 RESULTS:
Sentiment: Neutral 😐
Score: 0.00 (Range: -1 to 1)
Words: 5
Sentences: 1
```

## 🧠 How It Works

1. **Text Input**: Gets text from command line or user input
2. **AI Analysis**: Uses TextBlob's machine learning models to analyze sentiment
3. **Processing**: Counts words and sentences using natural language processing
4. **Output**: Shows results in a user-friendly format

### The AI Behind It
- **TextBlob**: A Python library that uses trained machine learning models
- **Sentiment Analysis**: Assigns polarity scores from -1 (negative) to +1 (positive)
- **Tokenization**: Splits text into meaningful units (words, sentences)

## 🔧 Technical Details

### Dependencies
- `textblob`: For sentiment analysis and text processing
- `nltk`: Natural Language Toolkit (used by TextBlob)

### Features
- **Automatic Setup**: Downloads required AI models automatically
- **Fallback Methods**: Uses simple counting if AI fails
- **Cross-Platform**: Works on Windows, Mac, and Linux
- **No External APIs**: Everything runs locally

## 🐛 Troubleshooting

### "MissingCorpusError"
```bash
# Run this command to download AI models:
python -m textblob.download_corpora
```

### "TextBlob not found"
```bash
# Install TextBlob:
pip install textblob
```

### Still Having Issues?
The tool includes backup methods that work without external dependencies!

## 📈 What I Learned

Building this tool taught me:

- **AI Integration**: How to use machine learning libraries in Python
- **Natural Language Processing**: Understanding how computers analyze text
- **Error Handling**: Making programs robust and user-friendly
- **Library Management**: Installing and configuring external packages
- **Sentiment Analysis**: How AI determines emotions in text

## 🔮 Future Improvements

Ideas for making this tool even better:

- [ ] **Language Detection**: Identify what language the text is in
- [ ] **Keyword Extraction**: Find the most important words
- [ ] **Text Summarization**: Create short summaries of long text
- [ ] **Emotion Detection**: Detect specific emotions (joy, anger, fear, etc.)
- [ ] **File Support**: Analyze entire documents
- [ ] **Export Results**: Save results to CSV or JSON files
- [ ] **Batch Processing**: Analyze multiple texts at once

## 🎯 Why This Matters

This simple tool represents a major milestone:

- **First AI Integration**: My first experience with machine learning
- **Real-World Application**: Sentiment analysis is used by companies everywhere
- **Foundation Building**: Prepares me for more advanced AI projects
- **Problem Solving**: Shows I can integrate complex libraries successfully

## 🌟 Use Cases

This tool could be used for:

- **Social Media Monitoring**: Analyze customer feedback
- **Content Creation**: Check if your writing sounds positive
- **Learning**: Understand how AI analyzes text
- **Business**: Analyze survey responses or reviews
- **Personal**: Check the tone of emails before sending

## 🏆 Achievement Unlocked

✅ **AI Developer**: Built my first AI-powered application  
✅ **NLP Explorer**: Used natural language processing  
✅ **Problem Solver**: Handled complex library integration  
✅ **Documentation Master**: Wrote comprehensive documentation  

## 🔗 Connect & Follow

- **GitHub**: [@MananCodes-dev](https://github.com/MananCodes-dev)
- **Twitter**: [@UnfilteredManan](https://twitter.com/UnfilteredManan)
- **Challenge**: [100 Python CLI Tools](https://github.com/MananCodes-dev/python-cli-apps)

---

**Day 20** of my 4-year journey to master AI/ML and Game Development. Every day I'm building something new and sharing my progress publicly. Follow along for daily coding updates! 🚀

*Built with ❤️ and curiosity about artificial intelligence*
# ⌨️ Typing Speed Test CLI App

A Python CLI app that measures typing speed and accuracy.

## Features:
- Random sentence selection
- WPM calculation
- Accuracy measurement
- Replayable

## Run it:
```
python typing_speed_test.py
```
# 🔗 URL Shortener (CLI)

A Python command-line tool that shortens long URLs using the [TinyURL API](https://tinyurl.com/).

---

## 🚀 Features
- Shorten any valid URL instantly
- Simple CLI interface
- No API key required
- Works with any website link

---

## 🛠 Tech Stack
- **Language:** Python 3.x 🐍
- **Libraries:** `requests`
- **API:** [TinyURL API](https://tinyurl.com/)

---

## 📦 Installation
```
git clone https://github.com/MananCodes-dev/python-cli-apps.git
cd python-cli-apps/utilities
```
## How to Run
```
python url_shortener.py
```
Enter the URL to shorten (or 'exit' to quit): https://www.example.com/this-is-a-very-long-url-with-parameters?id=12345
🔗 Short URL: https://tinyurl.com/abc123

# 🌦 Real-Time Weather App (CLI)

Python CLI app that fetches and displays real-time weather data using the OpenWeatherMap API.

## Features:
- Get temperature, condition, and humidity
- Search by city name
- Celsius units by default

## Setup:
1. Get a free API key from OpenWeatherMap
2. Replace `YOUR_API_KEY` in `weather_app.py`

## Run:
```bash
python weather_app.py
```

# 🎥 YouTube Video Downloader (CLI)

A Python command-line tool to download YouTube videos in different resolutions (360p, 720p, 1080p).  
Built with the **pytube** library.

---

## 🚀 Features
- Download any YouTube video by URL  
- Choose resolution (360p, 720p, 1080p)  
- Save video locally with original title  
- Error handling for invalid URLs or unavailable streams  
- Optional: Download audio-only version (future update)

---

## 🛠 Tech Stack
- **Language:** Python 3.x 🐍  
- **Libraries:** `pytube`

---

## 📦 Installation
Install dependencies first:
```
pip install pytube
```
