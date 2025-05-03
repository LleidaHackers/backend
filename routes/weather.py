from fastapi import APIRouter, HTTPException
from weather_api import get_weather

router = APIRouter()

@router.get("/weather/{latitude}/{longitude}")
def get_weather(latitude: float, longitude: float):
    return get_weather(latitude, longitude)