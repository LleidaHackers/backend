import fastapi
from fastapi import APIRouter, Depends, HTTPException

router= APIRouter()


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
