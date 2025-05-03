
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import modules
from routes import build
from routes import data_center
from routes import workflow
from routes import weather
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(modules.router, prefix="/modules", tags=["modules"])
app.include_router(workflow.router, prefix="/workflow", tags=["workflow"])
app.include_router(data_center.router, prefix="/data-center", tags=["data-center"])
app.include_router(build.router, prefix="/build", tags=["build simulation"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
