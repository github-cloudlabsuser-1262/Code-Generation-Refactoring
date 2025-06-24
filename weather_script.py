import requests

API_KEY = "9c18ec09e647900bf5a7ee3f9d462ba1"  # Replace with your OpenWeatherMap API key
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    print(f"Weather in {CITY}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("Failed to fetch weather data.")