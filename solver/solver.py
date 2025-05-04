import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List
from ortools.linear_solver import pywraplp
from BaseModule import BaseModule

def place_blocks_on_grid(blocks, grid_width, grid_height):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        raise RuntimeError("Solver not available")

    n = len(blocks)
    #Position decision variables
    x = [solver.IntVar(0, grid_width, f'x_{i}') for i in range(n)]
    y = [solver.IntVar(0, grid_height, f'y_{i}') for i in range(n)]

    # Ensure each block stays within grid bounds
    for i in range(n):
        w, h = blocks[i]
        solver.Add(x[i] + w <= grid_width)
        solver.Add(y[i] + h <= grid_height)

    # Add non-overlapping constraints
    for i in range(n):
        for j in range(i + 1, n):
            w1, h1 = blocks[i]
            w2, h2 = blocks[j]
      
            #No overlap decision vairables
            no_overlap = [
                solver.BoolVar(f'left_{i}_{j}'),
                solver.BoolVar(f'right_{i}_{j}'),
                solver.BoolVar(f'above_{i}_{j}'),
                solver.BoolVar(f'below_{i}_{j}')
            ]
            solver.Add(x[i] + w1 <= x[j] + grid_width * (1 - no_overlap[0]))
            solver.Add(x[j] + w2 <= x[i] + grid_width * (1 - no_overlap[1]))
            solver.Add(y[i] + h1 <= y[j] + grid_height * (1 - no_overlap[2]))
            solver.Add(y[j] + h2 <= y[i] + grid_height * (1 - no_overlap[3]))

            # At least one no-overlap condition must hold
            solver.Add(sum(no_overlap) >= 1)

    # Solve
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        positions = [(x[i].solution_value(), y[i].solution_value()) for i in range(n)]
        return positions
    else:
        return None

# Example usage


# = [((3, 2),id), ((2, 2)), (1, 4), (1, 4)]
#blocks = [(3, 2), (2, 2), (1, 4), (1, 4)]
grid_width = 10
grid_height = 10


def solve(modules : List[BaseModule],grid_width,grid_heigh) -> List[BaseModule]:

    stripped_modules = [(module.sizeX, module.sizeY) for module in modules]
    
    positions = place_blocks_on_grid(stripped_modules, grid_width, grid_heigh)

    if positions:
        for i, pos in enumerate(positions):
            modules[i].posX = pos[0]
            modules[i].posY = pos[1]
            
        return modules
    else:
        print("No feasible placement found.")
        return Exception("No feasible placement found.")



def modules_to_2d(modules: List[BaseModule], grid_width: int = 0, grid_height: int = 0) -> str:
    print(modules[5].posX)
    json_data = {
        "grid": {
            "width": grid_width,
            "height": grid_height
        },
        "blocks": [
            {
                "id": module.id,
                "name": module.name,
                "type": module.__class__.__name__ ,
                "color": module.color, 
                "position": {
                    "x": module.posX,
                    "y": module.posY
                },
                "dimensions": {
                    "width": module.sizeX,
                    "height": module.sizeY
                }
            }
            for module in modules
        ]
    }
    print(json.dumps(json_data, indent=2))
    return json.dumps(json_data, indent=2)


        
        
#modules = solve([Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf")],100,500)
#print(modules[4].posX)
#modules_to_2d(modules,100,500)