from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import parseModule  # Asegúrate de que `parseModule` esté accesible
import ast

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
datcenter_collection = db["mycollection_dc"]

router = APIRouter()

@router.get("/build")
def build_all_modules():
    all_data = list(datcenter_collection.find())
    built_modules = []

    for module in all_data:
        raw = module.get("data", "")
        if not raw.startswith("root="):
            continue
        
        try:
            parsed_data = ast.literal_eval(raw[len("root="):])
            nodes = parsed_data.get("nodes", [])

            for node in nodes:
                node_data = node.get("data", {})
                
                # Adaptar el dict al formato que espera parseModule (agregar 'cost' y 'type' si faltan)
                module_input = {
                    "name": node.get("id", "unknown"),
                    "type": node_data.get("type"),
                    "posX": node.get("position", {}).get("x", 0),
                    "posY": node.get("position", {}).get("y", 0),
                    "cost": str(node_data.get("power", node_data.get("demand", 0)))  # Asumimos que 'power' o 'demand' = cost
                }

                try:
                    built = parseModule(module_input)
                    built_modules.append(built)
                except Exception as e:
                    built_modules.append({"error": str(e), "input": module_input})

        except Exception as e:
            built_modules.append({"error": "Failed to parse module data", "details": str(e)})

    return JSONResponse([str(b) for b in built_modules])
