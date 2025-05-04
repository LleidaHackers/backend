

from solver import solver
app = FastAPI()

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import modules
from routes import build
from routes import data_center
from routes import workflow
from routes import weather
from routes import gemini
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/2d_image")
def solve_grid():
    modules = solver.solve([Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf"),Transformer_100("asdf")],100,500)
    return solver.modules_to_2d(modules,100,500)
    


app.include_router(modules.router, prefix="/modules", tags=["modules"])
app.include_router(workflow.router, prefix="/workflow", tags=["workflow"])
app.include_router(data_center.router, prefix="/data-center", tags=["data-center"])
app.include_router(build.router, prefix="/build", tags=["build simulation"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])
app.include_router(gemini.router, prefix="/gemini", tags=["gemini"])


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

