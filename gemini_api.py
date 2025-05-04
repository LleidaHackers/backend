from google import genai
import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

context = """Context for AI Gemini: Energy Data Center Designer App
Application: Simulation/design tool for modular energy facilities (like power plants) with generation, storage, distribution and optimization modules.

Features:
- Drag-and-drop interface with component blocks (solar, batteries, etc.)
- Real-time simulation of performance/failures
- Built for Siemens' industrial clients
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
