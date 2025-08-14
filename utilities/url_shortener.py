import requests

URL = "https://tinyurl.com/api-create.php"

def shorten_url(long_url):
    response = requests.get(URL, params={"url": long_url})
    if response.status_code == 200:
        return response.text
    else:
        print("❌ Failed to shorten URL")
        return 
    
while True:
    long_url = input("\nEnter the URL to shorten or type 'exit' to quit: ")
    if long_url.lower() == 'exit':
        print("Exiting the URL shortener. Goodbye!")
        break
    
    short_url = shorten_url(long_url)
    if short_url:
        print(f"✅ Shortened URL: {short_url}")
    else:
        print("❌ Could not shorten the URL. Please try again.")
