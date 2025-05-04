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

class ModuleData(RootModel[Any]):
    pass


@router.get("/")
def get_workflow():
    workflow = list(workflow_collection.find())
    return {"status": "success", "workflow": str(workflow)}


@router.post("/{id}")
def save_module(id: str, data: ModuleData):
    workflow_collection.update_one(
        {"id": id},
        {"$set": {"data": str(data)}},
        upsert=True
    )

    return {"status": "success", "id": id}



@router.delete("/{id}")
def delete_workflow(id: str):
    result = workflow_collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return {"status": "success", "message": "Workflow deleted"}
    else:
        return {"status": "error", "message": "Workflow not found"}
    
@router.get("/{id}")
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


@router.get("/all")
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

