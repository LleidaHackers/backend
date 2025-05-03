
from fastapi.responses import RedirectResponse
from DataCenters import Server_Square
from routes import modules
from solver import solver
app = FastAPI()

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/tet")
def test():
    return {
        "source": [
            {
                "name": "Solar Panel",
                "icon": "Sun",
                "specs": ["Output: 20W", "Type: Renewable"],
                "cost": 2000,
            },
        ],
        "sink": [
            {
                "name": "Server",
                "icon": "Server",
                "specs": ["Consumption: 10W", "Critical Load"],
                "cost": 1500,
            },
            {
                "name": "Cooler",
                "icon": "Snowflake",
                "specs": ["Consumption: 5W", "Thermal Control"],
                "cost": 1000,
            },
        ],
    }

@app.get("/2d_image")
def solve_grid():
    modules = solver.solve([Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf")],100,500)
    return solver.modules_to_2d(modules,100,500)
    

app.include_router(modules.router, prefix="/modules", tags=["modules"])