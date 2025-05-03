from ortools.linear_solver import pywraplp

def place_blocks_on_grid(blocks, grid_width, grid_height):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        raise RuntimeError("Solver not available")

    n = len(blocks)
    #Position decision variables
    x = [solver.IntVar(0, grid_width, f'x_{i}') for i in range(n)]
    y = [solver.IntVar(0, grid_height, f'y_{i}') for i in range(n)]
    print(x)
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


modules = [((3, 2),id), ((2, 2)), (1, 4), (1, 4)]
blocks = [(3, 2), (2, 2), (1, 4), (1, 4)]
grid_width = 10
grid_height = 10
def solver(modules,grid):
    positions = place_blocks_on_grid(blocks, grid.width, grid.height)
    if positions:
        for i, pos in enumerate(positions):
            print(f"Block {i} placed at {pos}")
    else:
        print("No feasible placement found.")
