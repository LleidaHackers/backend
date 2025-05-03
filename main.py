from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/test")
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

