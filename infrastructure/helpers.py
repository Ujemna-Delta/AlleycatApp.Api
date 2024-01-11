from fastapi import HTTPException
from fastapi.responses import JSONResponse
from requests import Response


def redirect_response(response: Response):
    content = None if not response.text else response.json()
    if 200 <= response.status_code <= 299:
        return JSONResponse(status_code=response.status_code, content=content)

    raise HTTPException(status_code=response.status_code, detail=content)
