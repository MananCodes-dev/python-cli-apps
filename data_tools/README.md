# 📊 Data Tools

Command-line tools for data collection, processing, and analysis built with Python.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Web Scraping](https://img.shields.io/badge/Feature-Web%20Scraping-green.svg)](#)
[![CLI](https://img.shields.io/badge/Interface-Command%20Line-yellow.svg)](#)

---

## 🚀 Quick Start

```bash
# Navigate to data_tools directory
cd python-cli-apps/data_tools

# Install dependencies
pip install requests beautifulsoup4

# Run the news scraper
python news_scraper.py
```

---

## 🛠 Available Tools

| Tool | Status | Description | Key Features |
|------|--------|-------------|--------------|
| **[News Scraper](#-news-headlines-scraper)** | ✅ Active | Web scraping tool for headlines and data | Multi-site scraping, CSV export, practice-safe |
| **CSV Analyzer** | 🚧 Coming Soon | Statistical analysis of CSV files | Summary stats, data quality |
| **Data Visualizer** | 🚧 Coming Soon | Chart creation from datasets | Multiple chart types, export |
| **Excel Processor** | 🚧 Coming Soon | Excel file manipulation | Multi-sheet processing |

---

## 🕷️ News Headlines Scraper

**Day 21** of 100 Python CLI Tools Challenge - A comprehensive web scraper for collecting headlines and data from multiple sources.

### 🌟 Features
- **Multi-Source Scraping** - Quotes, news headlines, and books data
- **Practice-Safe Sites** - Uses scraping-friendly websites for learning
- **CSV Export** - Saves all data in structured CSV format
- **Interactive Menu** - Easy-to-use command-line interface
- **Respectful Scraping** - Built-in delays and proper headers
- **Error Handling** - Graceful failure with informative messages
- **Data Summary** - Comprehensive overview of scraped content

### 🎯 Supported Sources
- **Quotes to Scrape** (`quotes.toscrape.com`) - Inspirational quotes with authors and tags
- **Hacker News** (`news.ycombinator.com`) - Latest tech news and discussions
- **Books to Scrape** (`books.toscrape.com`) - Book titles, prices, and ratings

### 🚀 Usage

#### Interactive Mode
```bash
python news_scraper.py
```

The scraper will present you with options:
1. **Run full scrape** (recommended) - Scrapes all sources
2. **Scrape quotes only** - Focus on inspirational quotes
3. **Scrape Hacker News only** - Get latest tech headlines
4. **Scrape books only** - Collect book data
5. **Show current data** - Display summary of scraped content
6. **Exit** - Close the application

#### Sample Output
```
🕷️  Welcome to News Headlines Scraper!
🚀 Starting comprehensive web scraping...

🕷️  Scraping quotes for practice...
✅ Successfully scraped 10 quotes!

🕷️  Scraping Hacker News headlines...
✅ Successfully scraped 15 news headlines!

🕷️  Scraping books data...
✅ Successfully scraped 12 books!

✅ Data saved to data_tools/scraped_data.csv
📊 Total records: 37

============================================================
📋 SCRAPING SUMMARY
============================================================
📚 Quote: 10 items
📚 News: 15 items
📚 Book: 12 items
🔢 Total Items: 37
⏰ Last Updated: 2025-01-19 14:30:25
```

### 📊 Data Structure

The scraper creates a CSV file with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `type` | Content type | quote, news, book |
| `title` | Main content/headline | "The way to get started is to quit talking..." |
| `author` | Source/author | Albert Schweitzer, Hacker News Community |
| `content` | Additional info | Tags, price, category |
| `url` | Source URL | https://news.ycombinator.com |
| `scraped_at` | Timestamp | 2025-01-19 14:30:25 |

### 🔧 Technical Features

#### Smart Request Handling
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

#### Respectful Scraping
- **Rate Limiting** - Built-in delays between requests
- **Session Management** - Efficient connection reuse
- **Error Handling** - Graceful failure recovery
- **Practice Sites** - Uses scraping-friendly educational sites

#### Data Processing
- **BeautifulSoup Parsing** - Reliable HTML parsing
- **CSV Export** - Structured data output
- **Timestamp Tracking** - When data was collected
- **Type Categorization** - Organized by content type

---

## 📋 Requirements

```bash
# Core dependencies
requests>=2.28.0          # HTTP requests for web scraping
beautifulsoup4>=4.11.0    # HTML/XML parsing
```

### Installation
```bash
# Install required packages
pip install requests beautifulsoup4

# Or install all project dependencies
pip install -r requirements.txt
```

---

## 💻 Advanced Usage

### Programmatic Usage
```python
from news_scraper import NewsHeadlinesScraper

# Create scraper instance
scraper = NewsHeadlinesScraper()

# Scrape specific source
scraper.scrape_hacker_news()

# Save to custom filename
scraper.save_to_csv('my_headlines.csv')

# Display results
scraper.display_summary()
```

### Custom Output Location
```python
# Scraper automatically creates data_tools directory
# Files saved to: data_tools/scraped_data.csv
```

---

## 🎓 Learning Objectives

This tool demonstrates:

- **Web Scraping Fundamentals** - HTTP requests, HTML parsing
- **Data Extraction** - CSS selectors, element traversal  
- **Error Handling** - Try-catch blocks, graceful failures
- **File I/O Operations** - CSV writing, directory creation
- **Object-Oriented Programming** - Class design, method organization
- **User Experience Design** - Interactive menus, clear feedback
- **Ethical Scraping** - Respectful delays, appropriate sites

---

## 🔒 Ethical Considerations

### ✅ What This Scraper Does Right
- **Uses practice sites** designed for scraping education
- **Includes delays** between requests to be respectful
- **Proper headers** to identify the scraper
- **Limited requests** to avoid overwhelming servers
- **Educational purpose** - built for learning

### ⚠️ Important Notes
- Only scrapes sites that allow scraping
- Includes rate limiting and respectful delays
- Uses educational/practice websites
- Not for commercial data harvesting
- Always check `robots.txt` before scraping new sites

---

## 🚧 Upcoming Tools

### In Development
- **CSV Analyzer** - Statistical analysis and data profiling
- **Data Visualizer** - Chart generation from scraped data
- **Excel Processor** - Handle spreadsheet data
- **JSON Parser** - Process API responses and JSON files
- **Data Cleaner** - Clean and preprocess datasets

### Future Enhancements for News Scraper
- **RSS Feed Support** - Subscribe to news feeds
- **Keyword Filtering** - Filter content by topics
- **Duplicate Detection** - Remove repeated headlines
- **Sentiment Analysis** - Analyze headline sentiment
- **Export Formats** - JSON, Excel, database support
- **Scheduling** - Automated periodic scraping

---

## 🧪 Testing & Validation

### Manual Testing Checklist
- [ ] All three sources scrape successfully
- [ ] CSV file is created with proper structure
- [ ] Error handling works with network issues
- [ ] Interactive menu responds correctly
- [ ] Data summary displays accurate counts

### Sample Test Commands
```bash
# Test individual sources
python -c "from news_scraper import NewsHeadlinesScraper; s=NewsHeadlinesScraper(); s.scrape_quotes_site()"

# Test CSV output
python -c "from news_scraper import NewsHeadlinesScraper; s=NewsHeadlinesScraper(); s.scrape_quotes_site(); s.save_to_csv('test.csv')"
```

---

## 🤝 Contributing

Want to add more data tools or improve the scraper?

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-data-tool`)
3. **Add** your tool following the existing structure
4. **Test** thoroughly with various inputs
5. **Update** this README with your tool
6. **Submit** a pull request

### Ideas for New Tools
- **API Data Collector** - Fetch data from REST APIs
- **Database Connector** - Connect to SQL databases  
- **Text Analyzer** - NLP processing of scraped content
- **Image Scraper** - Collect and process images
- **Social Media Monitor** - Track mentions and hashtags (ethically)

---

## 📊 Performance & Limits

### Current Performance
- **Scraping Speed** - ~2-3 seconds per site with delays
- **Data Volume** - Handles 50+ items per session comfortably
- **Memory Usage** - Minimal, processes data in memory
- **File Size** - CSV output typically <1MB for standard scraping

### Scalability Considerations
- Built-in rate limiting prevents server overload
- Session management for efficient connections
- Error recovery for network interruptions
- Modular design allows easy extension

---

## 🏆 Use Cases

### Educational
- **Learning web scraping** concepts and techniques
- **Understanding HTML structure** and CSS selectors
- **Practicing data collection** and CSV handling
- **Studying ethical scraping** practices

### Professional
- **Prototyping data collection** workflows
- **Market research** preparation (with proper permissions)
- **Content monitoring** for competitors
- **Data pipeline** development and testing

### Personal
- **News aggregation** from multiple sources  
- **Research data collection** for projects
- **Learning about web technologies** and APIs
- **Building portfolio** of data tools

---

## 👨‍💻 About the Developer

Created by **Manan** as **Day 21** of the 100 Python CLI Tools Challenge, focusing on web scraping fundamentals and ethical data collection practices.

### Connect & Follow
- **GitHub**: [@MananCodes-dev](https://github.com/MananCodes-dev)
- **Twitter**: [@UnfilteredManan](https://twitter.com/UnfilteredManan)  
- **Project**: [Python CLI Apps Collection](https://github.com/MananCodes-dev/python-cli-apps)

---

## 🎯 Next Steps

1. **Try the scraper** - Run it and explore the data
2. **Examine the CSV** - See how data is structured
3. **Modify sources** - Add new scraping targets (ethically)
4. **Build analytics** - Analyze the scraped data
5. **Share feedback** - Help improve the tool

---

*🕷️ Ready to start scraping? Run the tool and begin collecting data responsibly!*

**Happy scraping and data analysis!** 🚀📊
