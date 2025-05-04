from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import parseModule  # Asegúrate de que `parseModule` esté accesible
import ast
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from Connection import Connection

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
    
    parsedObjects = []  
    for module in modules_cleaned:
        for node in module.get("nodes", []):
            parsedObjects.append(parseModule(node))
        for edge in module.get("edges", []):
            source = edge.get("source")
            target = edge.get("target")
            for obj in parsedObjects:
                if obj.id == source and target not in obj.connectedOut:
                    obj.connectedOut.append((target ,))
                elif obj.id == target and source not in obj.connectedIn:
                    obj.connectedIn.append(source)
    return parsedObjects


@router.get("/build/{id}")
def get_parsed_by_id(id: str):
    module = workflow_collection.find_one({"id": id})
    if module:
        raw_data = module.get("data", "")
        if isinstance(raw_data, str):
            # Intentamos quitar el prefijo "root=" si está presente
            if raw_data.startswith("root="):
                raw_data = raw_data[len("root="):]
            
            try:
                parsed_data = ast.literal_eval(raw_data)
            except Exception as e:
                return JSONResponse(
                    content={"error": "Invalid data format", "details": str(e)},
                    status_code=500
                )
        else:
            parsed_data = raw_data
        parsedObjects = []
        for node in parsed_data.get("nodes", []):
            parsedObjects.append(parseModule(node))
        for edge in parsed_data.get("edges", []):
            source = edge.get("source")
            target = edge.get("target")
            for obj in parsedObjects:
                if obj.id == source and target not in obj.connectedOut:
                    resource = edge.get("data").get("label")
                    obj.conn_outputs.append(Connection(resource, target))
                elif obj.id == target and source not in obj.connectedIn:
                    resource = edge.get("data").get("label")
                    obj.conn_inputs.append(Connection(resource, source))
        return parsedObjects


