import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    if not API_KEY:
        return {"error": "API key missing. Please check your .env file."}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }
    elif response.status_code == 404:
        return {"error": f"City '{city}' not found."}
    elif response.status_code == 401:
        return {"error": "Invalid API Key. Please verify your OpenWeatherMap key."}
    else:
        return {"error": f"Unexpected error: {data}"}
