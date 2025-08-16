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
