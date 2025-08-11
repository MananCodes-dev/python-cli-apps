import requests

API_KEy = "YOUR_API_KEY" #Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEy,
        'units': 'metric' # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data["cod"] != 200:
        print("City not found.")
        return 
    
    weather = data['weather'][0]['description'].capitalize()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    print(f"\n📍 City: {city}")
    print(f"🌤️ Weather: {weather}")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")

while True:
    city = input("Enter a city name (or 'exit' to quit): ")
    if city.lower() == 'exit':
        print("Exiting the weather app. Goodbye!")
        break
    get_weather(city)