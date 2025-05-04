from fastapi import APIRouter, Depends
from weather_api import get_weather

router = APIRouter()

@router.get("/{latitude}/{longitude}")
def get_info(latitude: float, longitude: float):
    weather_data= get_weather(latitude, longitude)
    filtered_data = {
        "temperature_c": weather_data["current_weather"]["temperature_c"],
        "humidity": weather_data["current_weather"]["humidity"],
        "wind_kph": weather_data["current_weather"]["wind_kph"],
    }

    return filtered_data