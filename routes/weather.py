from fastapi import APIRouter, HTTPException
from weather_api import get_weather

router = APIRouter()

@router.get("/{latitude}/{longitude}")
def get_weather_from_coords(latitude: float, longitude: float):
    weather_data= get_weather(latitude, longitude)
    return weather_data