from fastapi import APIRouter
from pathlib import Path
import json
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
datcenter_collection = db["mycollection_dc"]

@router.get("/modules")
def get_available_modules():
    json_path = Path("data/devices.json")  # ajusta la ruta si está en otro sitio
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@router.post("/save/{id}")
def save_module(id: int, data: str):
    # Aquí puedes guardar el módulo en la base de datos
    # Por simplicidad, lo guardamos en una colección de MongoDB
    o = u
    datcenter_collection.insert_one({"id": id, "data": o.__dict__()})
    return {"status": "success", "id": id}

@router.get("/get/{id}")
def get_module(id: int):
    module = datcenter_collection.find_one({"id": id})
    if module:
        return {"status": "success", "module": str(module)}
    else:
        return {"status": "error", "message": "Module not found"}
    
@router.get("/all")
def get_all_modules():
    modules = list(datcenter_collection.find())
    return {"status": "success", "modules": str(modules)}

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
def save_workflow(data: str):
    # Aquí puedes guardar el flujo de trabajo en la base de datos
    o = utils
    workflow_collection.insert_one({"data": o.__dict__()})
    return {"status": "success", "data": data}
@router.delete("/workflow/{id}")
def delete_workflow(id: int):
    result = workflow_collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Workflow deleted"}
    else:
        return {"status": "error", "message": "Workflow not found"}
@router.get("/workflow/{id}")
def get_workflow_by_id(id: int):
    workflow = workflow_collection.find_one({"_id": id})
    if workflow:
        return {"status": "success", "workflow": str(workflow)}
    else:
        return {"status": "error", "message": "Workflow not found"}
@router.get("/wall")
def get_all_workflows():
    workflows = list(workflow_collection.find())
    return {"status": "success", "workflows": str(workflows)}
