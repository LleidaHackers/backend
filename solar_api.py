import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_SOLAR_API_KEY")
BASE_URL = "https://solar.googleapis.com/v1/buildingInsights:findClosest"

def calcular_solar_roi(lat: float, lon: float, area_disponible_m2: float) -> dict:
    # Llamar a la Google Solar API
    params = {
        "location.latitude": lat,
        "location.longitude": lon,
        "key": API_KEY
    }

    response = httpx.get(BASE_URL, params=params)
    if response.status_code != 200:
        return {"error": f"API error: {response.status_code}", "details": response.text}

    data = response.json()
    solar = data.get("solarPotential", {})
    if not solar:
        return {"error": "No solar data found for the provided coordinates."}

    # Extraer radiación
    radiacion_anual_kwh_m2 = float(solar["maxSolarIrradiance"] * 365 * 24 / 1000)  # Convertir W/m2 a kWh/m2

    # Parámetros
    eficiencia = 0.18  # 18%
    precio_kwh = 0.20  # €/kWh
    coste_kWp = 1000   # €/kWp
    m2_por_kWp = 5.5   # m2 necesarios por kWp

    # Cálculos
    energia_generada = radiacion_anual_kwh_m2 * area_disponible_m2 * eficiencia
    ahorro_anual = energia_generada * precio_kwh

    potencia_instalada_kWp = area_disponible_m2 / m2_por_kWp
    coste_instalacion = potencia_instalada_kWp * coste_kWp

    retorno_anios = round(coste_instalacion / ahorro_anual, 2) if ahorro_anual > 0 else None

    return {
        "coordenadas": (lat, lon),
        "superficie_m2": area_disponible_m2,
        "energia_estimada_kWh": round(energia_generada, 2),
        "ahorro_anual_estimado_€": round(ahorro_anual, 2),
        "coste_instalacion_estimado_€": round(coste_instalacion, 2),
        "retorno_estimado_en_anios": retorno_anios
    }
