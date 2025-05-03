from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import parseModule  # Asegúrate de que `parseModule` esté accesible
import ast
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
module_collection = db["mycollection_dc"]

router = APIRouter()

@router.get("/build")
def build_all_modules():
    all_data = list(module_collection.find())
    print(all_data)
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


@router.get("/build_v2")
def build_sim():
    modules_cleaned = []

    for module in module_collection.find():
        raw_data = module.get("data", "")
        
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
    build_modules=[]
    for module in modules_cleaned:
        for node in module.get("nodes", []):
            o= parseModule(node)
            build_modules.append(o)
        
    return build_modules

        
