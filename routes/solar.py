from fastapi import APIRouter, Depends
from solar_api import calcular_solar_roi
router = APIRouter()

@router.get("/{lat}/{lon}/{surface}")
def get_solar_data(lat: float, lon: float, surface: float):
    """
    Endpoint to get solar data.
    """
    return calcular_solar_roi(lat,lon,surface)