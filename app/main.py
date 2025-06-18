import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": "Paris"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        city = data["location"]["name"]
        country = data["location"]["country"]
        updated = data["current"]["last_updated"]
        temp = data["current"]["temp_c"]
        text = data["current"]["condition"]["text"]
        result = f"{city}/{country} {updated} Weather: {temp} Celsius, {text}"
        print(result)

if __name__ == "__main__":
    get_weather()
