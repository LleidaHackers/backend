
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import modules
from fastapi.middleware.cors import CORSMiddleware

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

app.include_router(modules.router, prefix="/modules", tags=["modules"])
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
