from fastapi import APIRouter
import json
from pymongo import MongoClient
from pydantic import RootModel
from typing import Any  # en vez de from typing import Any
import ast
from solver import solver
from utils import parseModule  # Asegúrate de que `parseModule` esté accesible
from bson.objectid import ObjectId  # Asegúrate de importar ObjectId
from fastapi.responses import JSONResponse
router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
workflow_collection = db["mycollection_wf"]
module_collection = db["mycollection_dc"]
data_center_collection = db["mydatacenter_collection"]
sat_collection = db["sat_collection"]


@router.get("/sats")
def get_all_sat_solutions():
    # Buscar todos los documentos en la colección sat_collection
    solutions = sat_collection.find()
    
    # Convertir los documentos de MongoDB a una lista de diccionarios
    results = []
    for solution in solutions:
        # Remover el campo _id y solo agregar id y solution
        solution_data = {
            "id": solution.get("id"),
            "solution": solution.get("solution")
        }
        results.append(solution_data)
    
    # Si no hay soluciones, retornar un mensaje apropiado
    if not results:
        return JSONResponse(content={"message": "No solutions found."}, status_code=404)
    
    # Retornar todas las soluciones encontradas
    return JSONResponse(content={"solutions": results}, status_code=200)

@router.get("/sat/{id}")
def get_sat_solution(id: str):
    # Buscar el documento en la colección sat_collection por id
    solution = sat_collection.find_one({"id": id})
    
    if solution:
        parsed_solution = json.loads(solution["solution"])
        # Si se encuentra la solución, devolverla con solo los campos id y solution
        return JSONResponse(content={"solution": parsed_solution}, status_code=200)
    else:
        # Si no se encuentra, devolver un error
        return JSONResponse(content={"error": "Solution not found", "id": id}, status_code=404)


@router.get("/{id}")
def get_sat_solver(id: str):
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
                    obj.connectedOut.append(target)
                elif obj.id == target and source not in obj.connectedIn:
                    obj.connectedIn.append(source)
        data_center = data_center_collection.find_one({"_id": ObjectId(id)})
        grid = 800,800
        print(f"{parsedObjects}")
        modules = solver.solve(parsedObjects,grid[0],grid[1])
        result= solver.modules_to_2d(modules,grid[0],grid[1])    
        sat_collection.insert_one(
            {
                "id": id,
                "solution": result
            })
        return JSONResponse(content={"solution": result}, status_code=200)
        


