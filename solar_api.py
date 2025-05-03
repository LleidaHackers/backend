import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("GOOGLE_SOLAR_API_KEY")