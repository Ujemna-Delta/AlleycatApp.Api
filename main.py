from fastapi import FastAPI, Depends
from typing import Annotated
from routers import races_router
import infrastructure

app = FastAPI()
app.include_router(races_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def settings(setts: Annotated[infrastructure.AppSettings, Depends(infrastructure.get_settings)]):
    return {"settings": setts.persistence_url}
