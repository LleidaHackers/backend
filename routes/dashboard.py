from fastapi import APIRouter, Depends
import json

router = APIRouter()

@router.get("/get-plant-data/{id}")
def get_data(id: str):
    with open("data/dashboard.json", "r") as f:
        nodes = json.load(f)
    return nodes