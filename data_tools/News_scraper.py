# News Headlines Scraper - Day 21 Web Scraping
# A beginner-friendly web scraper for collecting news headlines

import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
import os

class NewsHeadlinesScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.scraped_data = []
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def scrape_quotes_site(self):
        """Scrape quotes from quotes.toscrape.com - perfect for learning!"""
        print("🕷️  Scraping quotes for practice...")
        
        try:
            url = "http://quotes.toscrape.com"
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes[:10]:  # Get first 10 quotes
                quote_text = quote.find('span', class_='text').get_text()
                author = quote.find('small', class_='author').get_text()
                tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                
                self.scraped_data.append({
                    'type': 'quote',
                    'title': quote_text[:100] + '...' if len(quote_text) > 100 else quote_text,
                    'author': author,
                    'content': ', '.join(tags),
                    'url': url,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                
            print(f"✅ Successfully scraped {len([d for d in self.scraped_data if d['type'] == 'quote'])} quotes!")
            return True
            
        except Exception as e:
            print(f"❌ Error scraping quotes: {str(e)}")
            return False
    
    def scrape_hacker_news(self):
        """Scrape Hacker News headlines - real tech news!"""
        print("🕷️  Scraping Hacker News headlines...")
        
        try:
            url = "https://news.ycombinator.com"
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            stories = soup.find_all('span', class_='titleline')
            
            for i, story in enumerate(stories[:15], 1):  # Get first 15 stories
                link = story.find('a')
                if link:
                    title = link.get_text()
                    story_url = link.get('href', '')
                    
                    # Handle relative URLs
                    if story_url.startswith('item?'):
                        story_url = f"https://news.ycombinator.com/{story_url}"
                    
                    self.scraped_data.append({
                        'type': 'news',
                        'title': title,
                        'author': 'Hacker News Community',
                        'content': f"Tech story #{i}",
                        'url': story_url,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                
                time.sleep(0.5)  # Be respectful - add small delay
                
            print(f"✅ Successfully scraped {len([d for d in self.scraped_data if d['type'] == 'news'])} news headlines!")
            return True
            
        except Exception as e:
            print(f"❌ Error scraping Hacker News: {str(e)}")
            return False
    
    def scrape_books_site(self):
        """Scrape books from books.toscrape.com - great for practice!"""
        print("🕷️  Scraping books data...")
        
        try:
            url = "http://books.toscrape.com"
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            books = soup.find_all('article', class_='product_pod')
            
            for book in books[:12]:  # Get first 12 books
                title_element = book.find('h3').find('a')
                title = title_element.get('title')
                price = book.find('p', class_='price_color').get_text()
                rating = book.find('p', class_='star-rating')['class'][1]
                
                self.scraped_data.append({
                    'type': 'book',
                    'title': title,
                    'author': f'Rating: {rating}',
                    'content': price,
                    'url': url,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                
            print(f"✅ Successfully scraped {len([d for d in self.scraped_data if d['type'] == 'book'])} books!")
            return True
            
        except Exception as e:
            print(f"❌ Error scraping books: {str(e)}")
            return False
    
    def save_to_csv(self, filename='scraped_data.csv'):
        """Save all scraped data to CSV file"""
        if not self.scraped_data:
            print("❌ No data to save!")
            return False
        
        try:
            # Create data_tools directory if it doesn't exist
            os.makedirs('data_tools', exist_ok=True)
            filepath = os.path.join('data_tools', filename)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['type', 'title', 'author', 'content', 'url', 'scraped_at']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for data in self.scraped_data:
                    writer.writerow(data)
            
            print(f"✅ Data saved to {filepath}")
            print(f"📊 Total records: {len(self.scraped_data)}")
            return True
            
        except Exception as e:
            print(f"❌ Error saving to CSV: {str(e)}")
            return False
    
    def display_summary(self):
        """Display a summary of scraped data"""
        if not self.scraped_data:
            print("No data scraped yet!")
            return
        
        print("\n" + "="*60)
        print("📋 SCRAPING SUMMARY")
        print("="*60)
        
        # Count by type
        type_counts = {}
        for item in self.scraped_data:
            item_type = item.get('type', 'unknown')
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        for item_type, count in type_counts.items():
            print(f"📚 {item_type.title()}: {count} items")
        
        print(f"🔢 Total Items: {len(self.scraped_data)}")
        print(f"⏰ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Show sample data
        print("\n📝 Sample Data:")
        for i, item in enumerate(self.scraped_data[:3], 1):
            print(f"{i}. [{item['type']}] {item['title'][:50]}{'...' if len(item['title']) > 50 else ''}")
        
        print("="*60)
    
    def run_full_scrape(self):
        """Run complete scraping process"""
        print("🚀 Starting comprehensive web scraping...")
        print("⚠️  Note: This scraper uses practice sites that allow scraping")
        
        success_count = 0
        
        # Scrape multiple sources
        if self.scrape_quotes_site():
            success_count += 1
        
        time.sleep(2)  # Respectful delay between sites
        
        if self.scrape_hacker_news():
            success_count += 1
        
        time.sleep(2)
        
        if self.scrape_books_site():
            success_count += 1
        
        # Save results
        if self.scraped_data:
            self.save_to_csv()
            self.display_summary()
        
        print(f"\n🎯 Scraping completed! {success_count}/3 sources successful.")
        return success_count > 0

def main():
    """Main function to run the scraper"""
    scraper = NewsHeadlinesScraper()
    
    print("🕷️  Welcome to News Headlines Scraper!")
    print("Choose an option:")
    print("1. Run full scrape (recommended)")
    print("2. Scrape quotes only")
    print("3. Scrape Hacker News only")
    print("4. Scrape books only")
    print("5. Show current data")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            scraper.run_full_scrape()
        elif choice == '2':
            scraper.scrape_quotes_site()
            scraper.save_to_csv()
        elif choice == '3':
            scraper.scrape_hacker_news()
            scraper.save_to_csv()
        elif choice == '4':
            scraper.scrape_books_site()
            scraper.save_to_csv()
        elif choice == '5':
            scraper.display_summary()
        elif choice == '6':
            print("Thanks for using the scraper! 👋")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
