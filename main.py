from fastapi import FastAPI, Depends
from typing import Annotated
from routers import leagues_router, points_router, races_router, tasks_router
import infrastructure

app = FastAPI()
app.include_router(leagues_router.router)
app.include_router(points_router.router)
app.include_router(points_router.completion_router)
app.include_router(races_router.router)
app.include_router(races_router.completion_router)
app.include_router(tasks_router.router)
app.include_router(tasks_router.completion_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def settings(setts: Annotated[infrastructure.AppSettings, Depends(infrastructure.get_settings)]):
    return {"settings": setts.persistence_url}
