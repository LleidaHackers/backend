from fastapi import APIRouter
import json
from pymongo import MongoClient
from pydantic import RootModel
from typing import Any  # en vez de from typing import Any
import ast
from fastapi.responses import JSONResponse
router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
module_collection = db["mycollection_dc"]
data_center_collection = db["mydatacenter_collection"]
sat_collection = db["sat_collection"]

class ModuleData(RootModel[Any]):
    pass

@router.get("/")
def get_sat_solver(Data: ModuleData):
    """
    Endpoint to get SAT solver information.
    """
    pass

@router.get("/save/{id}")
def save_sat_solver(id: str, data: ModuleData):
    sat_collection.insert_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}

@router.get("/get/{id}")
def get_sat_solver(id: str):
    result = sat_collection.find_one({"id": id})
    
    if result:
        return {"status": "success", "data": result["data"], "id": id}
    else:
        return {"status": "not found", "message": f"ID {id} no encontrada"}
    