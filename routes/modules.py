from fastapi import APIRouter
from pathlib import Path
import json
from pymongo import MongoClient
from pydantic import RootModel
from typing import Any  # en vez de from typing import Any
import ast
from fastapi.responses import JSONResponse
from bson.json_util import dumps
router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
module_collection = db["mycollection_dc"]
data_center_collection = db["mydatacenter_collection"]

class ModuleData(RootModel[Any]):
    pass


@router.get("/")
def get_available_modules():
    json_path = Path("data/devices.json")  # ajusta la ruta si está en otro sitio
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data




@router.get("/all")
def get_modules():
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
    return modules_cleaned

@router.post("/{id}")
def save_module(id: str, data: ModuleData):
    # Aquí puedes guardar el módulo en la base de datos
    # Por simplicidad, lo guardamos en una colección de MongoDB
    module_collection.update_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}

@router.get("/{id}")
def get_module(id: str):
    module = module_collection.find_one({"id": id})
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

        return JSONResponse(content=parsed_data)

    return JSONResponse(content={"error": "Module not found"}, status_code=404)

@router.delete("/{id}")
def delete_module(id: str):
    result = module_collection.delete_one({"id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Module deleted"}
    else:
        return {"status": "error", "message": "Module not found"}

"""

@router.get("/workflow")
def get_workflow():
    workflow = list(workflow_collection.find())
    return {"status": "success", "workflow": str(workflow)}


@router.post("/workflow")
def save_workflow(id: str, data: ModuleData):
    # Aquí puedes guardar el módulo en la base de datos
    # Por simplicidad, lo guardamos en una colección de MongoDB
    workflow_collection.update_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}
@router.delete("/workflow/{id}")
def delete_workflow(id: str):
    result = workflow_collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Workflow deleted"}
    else:
        return {"status": "error", "message": "Workflow not found"}
    
@router.get("/workflow/{id}")
def get_workflow_by_id(id: str):
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

        return JSONResponse(content=parsed_data)

    return JSONResponse(content={"error": "Module not found"}, status_code=404)


@router.get("/wall")
def get_all_workflows():
    modules_cleaned = []

    for module in workflow_collection.find():
        raw_data = module.get("data", "")
        parsed_data = {}

        if isinstance(raw_data, str) and raw_data.startswith("root="):
            raw_data = raw_data[len("root="):]

            try:
                parsed_data = ast.literal_eval(raw_data)
            except Exception as e:
                parsed_data = {"error": "Invalid data format", "details": str(e)}
        else:
            parsed_data = raw_data  # already parsed or missing

        modules_cleaned.append({
            "id": module.get("id"),
            "nodes": parsed_data.get("nodes", []),
            "edges": parsed_data.get("edges", [])
        })

    return JSONResponse(modules_cleaned)


@router.post("/create-data-center")
def create_data_center(data: dict):
    data["status"] = "Active"
    data["totalBudget"] = data.get("budget", 0)
    space_x = data.get("space_x", 0)
    space_y = data.get("space_y", 0)

    data.update({
        "powerConsume": 0,
        "powerRequired": 0,
        "accomulatePower": 0,
        "occupedSurface": 0,
        "totalSurface": space_x * space_y,
        "waterUsage": 0,
        "distilledWaterUsage": 0,
        "chilledWaterUsage": 0,
        "waterProduction": 0,
        "freshWaterUsage": 0,
        "freshWaterProduction": 0,
        "distilledWaterProduction": 0,
        "chilledWaterProduction": 0,
        "internalNetworkUsage": 0,
        "internalNetworkProduction": 0,
        "externalNetworkProduction": 0,
        "soundLevel": 0,
        "procesProduction": 0,
        "dataStorageProduction": 0
    })
    result = data_center_collection.insert_one(data)
    return {"inserted_id": str(result.inserted_id)}

@router.post("/save-data-center/{id}")
def save_module(id: str, data: dict):
    from bson import ObjectId
    FIELDS = [
        "totalBudget", "budget", "powerConsume", "powerRequired", "accomulatePower", "occupedSurface",
        "totalSurface", "waterUsage", "distilledWaterUsage", "chilledWaterUsage",
        "waterProduction", "freshWaterUsage", "freshWaterProduction",
        "distilledWaterProduction", "chilledWaterProduction",
        "internalNetworkUsage", "internalNetworkProduction", "externalNetworkProduction",
        "soundLevel", "procesProduction", "dataStorageProduction"
    ]
    cleaned_data = {key: data.get(key, 0) for key in FIELDS}
    result = data_center_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": cleaned_data},
        upsert=False
    )
    if result.modified_count > 0:
        return {"status": "success", "id": id}
    else:
        return {"status": "error", "message": "Update failed or no changes made"}

# Nuevo endpoint para eliminar data centers por _id (ObjectId)
@router.delete("/delete-data-center/{id}")
def delete_data_center(id: str):
    from bson import ObjectId
    result = data_center_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Data center deleted"}
    else:
        return {"status"    : "error", "message": "Data center not found"}

@router.get("/data-center")
def get_data_center():
    data_center = list(data_center_collection.find())
    return JSONResponse(content=json.loads(dumps(data_center)))

from bson import ObjectId
from bson.errors import InvalidId

@router.get("/data-center/{id}")
def get_data_center_id(id: str):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return JSONResponse(content={"error": "Invalid ID format"}, status_code=400)

    module = data_center_collection.find_one({"_id": object_id})
    if module:
        return JSONResponse(content=json.loads(dumps(module)))
    
    return JSONResponse(content={"error": "Module not found"}, status_code=404)
"""