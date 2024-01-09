from fastapi import FastAPI, Depends
from typing import Annotated
import infrastructure

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def settings(setts: Annotated[infrastructure.AppSettings, Depends(infrastructure.get_settings)]):
    return {"settings": setts.persistence_url}
