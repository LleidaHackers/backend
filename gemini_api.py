from google import genai
import os
import requests
from dotenv import load_dotenv
import json
from pymongo import MongoClient
# Abrir y leer el archivo JSON
with open("data/devices.json", "r") as file:
    total = json.load(file)
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

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["mydatabase"]
workflow_collection = db["mycollection_wf"]
module_collection = db["mycollection_dc"]
data_center_collection = db["mydatacenter_collection"]

modules_cleaned = []
for module in module_collection.find():
    raw_data = module.get("data", "")
    print(f"raw_data: {raw_data}")
    
    # Si raw_data es un string, intenta convertirlo a un diccionario
    if isinstance(raw_data, str):
        if raw_data.startswith("root="):
            raw_data = raw_data[len("root="):]
            
        try:
            # Intenta convertir la cadena a un diccionario usando ast.literal_eval
            parsed_data = ast.literal_eval(raw_data)
            if not isinstance(parsed_data, dict):
                parsed_data = {}  # Si no es un diccionario, asigna un diccionario vacío
        except Exception as e:
            parsed_data = {"error": "Invalid data format", "details": str(e)}
    else:
        # Si raw_data ya es un diccionario, no lo modificamos
        parsed_data = raw_data

    # Si parsed_data es un diccionario, procedemos a usar get()
    if isinstance(parsed_data, dict):
        nodes = parsed_data.get("nodes", [])
        edges = parsed_data.get("edges", [])
    else:
        nodes = []
        edges = []

    # Añadir los datos procesados a la lista de módulos
    modules_cleaned.append({
        "id": module.get("id"),
        "nodes": nodes,
        "edges": edges,
        # "type": module.get("type"),
    })

objective="I want the AI to return me the new module with the correct edges. We want to have more power than the user said and if it has not, just look for the module and the connections. Give me JUST A MODULE, no suggestions or petitions just a MODULE FROM TH ELIST TOTAL. YOu will give me the information for the terminal, so just give the JSON with the module and the connections. The module is a dictionary with the keys: id, nodes, edges. The nodes is a list of dictionaries with the keys: id, type, name, and the edges is a list of dictionaries with the keys: source, target. The id is a string, the type is a string, the name is a string, the source is a string and the target is a string. The module is a dictionary with the keys: id, nodes, edges. GIVE JUST A SOLUTION"


current = modules_cleaned  # puedes renombrarlo así para claridad

# Armar el prompt como texto plano
prompt = f"""
{context}

Objective:
{objective}

Input Data:
- Total Modules:
{json.dumps(total, indent=2)}

- Current Modules:
{json.dumps(current, indent=2)}

Please analyze the data and return a modified module list that:
- Ensures more power than originally requested
- Adjusts the module connections if needed
- Returns a valid structure of nodes and edges
"""

# Enviar al modelo
def generate_response():
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response