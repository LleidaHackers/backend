from fastapi import APIRouter
from gemini_api import generate_response
import json
import re

router = APIRouter()

@router.get("/")
def get_gemini():
    solution = generate_response()
    
    # Extraer texto del contenido generado
    try:
        text = solution.text  # Acceso directo si es un objeto de Gemini
    except AttributeError:
        text = solution.candidates[0].content.parts[0].text    # Extraer JSON entre ```json ... ```
    match = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not match:
        return {"error": "No JSON block found in response"}

    try:
        json_text = match.group(1)
        parsed = json.loads(json_text)
        return parsed
    except json.JSONDecodeError as e:
        return {"error": "Invalid JSON format", "details": str(e)}
