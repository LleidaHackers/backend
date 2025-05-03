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
datcenter_collection = db["mycollection_dc"]


class ModuleData(RootModel[Any]):
    pass


@router.get("/modules")
def get_available_modules():
    json_path = Path("data/devices.json")  # ajusta la ruta si está en otro sitio
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@router.post("/save/{id}")
def save_module(id: int, data: ModuleData):
    # Aquí puedes guardar el módulo en la base de datos
    # Por simplicidad, lo guardamos en una colección de MongoDB
    datcenter_collection.update_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}

@router.get("/get/{id}")
def get_module(id: int):
    module = datcenter_collection.find_one({"id": id})
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


@router.get("/all")
def get_all_modules():
    modules_cleaned = []

    for module in datcenter_collection.find():
        raw_data = module.get("data", "")
        parsed_data = {}

        if isinstance(raw_data, str) and raw_data.startswith("root="):
            raw_data = raw_data[len("root="):]

            try:
                # Si raw_data es un string, intentar convertirlo a un diccionario
                parsed_data = ast.literal_eval(raw_data)
                if not isinstance(parsed_data, dict):
                    parsed_data = {}  # Si no es un diccionario, lo ignoramos o gestionamos de otra forma
            except Exception as e:
                parsed_data = {"error": "Invalid data format", "details": str(e)}
        else:
            parsed_data = raw_data  # Ya está procesado o ausente

        # Asegúrate de que parsed_data sea un diccionario antes de intentar acceder con .get()
        modules_cleaned.append({
            "id": module.get("id"),
            "nodes": parsed_data.get("nodes", []),
            "edges": parsed_data.get("edges", [])
        })

    return JSONResponse(modules_cleaned)


@router.delete("/delete/{id}")
def delete_module(id: int):
    result = datcenter_collection.delete_one({"id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Module deleted"}
    else:
        return {"status": "error", "message": "Module not found"}

@router.get("/workflow")
def get_workflow():
    workflow = list(workflow_collection.find())
    return {"status": "success", "workflow": str(workflow)}


@router.post("/workflow")
def save_workflow(id: int, data: ModuleData):
    # Aquí puedes guardar el módulo en la base de datos
    # Por simplicidad, lo guardamos en una colección de MongoDB
    workflow_collection.update_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}
@router.delete("/workflow/{id}")
def delete_workflow(id: int):
    result = workflow_collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Workflow deleted"}
    else:
        return {"status": "error", "message": "Workflow not found"}
    
@router.get("/workflow/{id}")
def get_workflow_by_id(id: int):
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
    result = datcenter_collection.insert_one(data)
    return {"inserted_id": str(result.inserted_id)}

@router.get("/data-center")
def get_data_center():
    data_center = list(datcenter_collection.find())
    return JSONResponse(content=json.loads(dumps(data_center)))
