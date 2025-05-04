import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(lat, lon):
    if not API_KEY:
        raise ValueError("No API Key encontrada en el entorno")

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("Error al consultar la API:", data["error"])
        return None

    # Extraer la información relevante
    location = data["location"]
    current = data["current"]
    condition = current["condition"]

    weather_info = {
        "location": {
            "name": location["name"],
            "region": location["region"],
            "country": location["country"],
            "lat": location["lat"],
            "lon": location["lon"],
            "timezone": location["tz_id"],
            "localtime": location["localtime"]
        },
        "current_weather": {
            "temperature_c": current["temp_c"],
            "feels_like_c": current["feelslike_c"],
            "humidity": current["humidity"],
            "wind_kph": current["wind_kph"],
            "wind_direction": current["wind_dir"],
            "pressure_mb": current["pressure_mb"],
            "uv_index": current["uv"],
            "condition": {
                "text": condition["text"],
                "icon_url": f"http:{condition['icon']}"
            }
        }
    }

    return weather_info
