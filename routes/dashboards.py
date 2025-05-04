from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

@router.get("/dashboards")
def get_dashboards():
    file_path = "data/data.json"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Dashboards file not found.")
    
    try:
        with open(file_path, "r") as f:
            dashboards = json.load(f)
        return dashboards
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding dashboards JSON.")
