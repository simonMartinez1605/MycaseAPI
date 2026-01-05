import logging
import uvicorn
from routers import mycase
from exceptions import APIError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from logs.logger_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(mycase.router)

@app.exception_handler(APIError)
async def api_error_handler(request: Request, exc: APIError):
    # Loguea la excepción con nivel WARNING o ERROR
    logger.warning(f"Error controlled: {exc.detail} | Status: {exc.status_code} | Path: {request.url.path}")
    
    # Devuelve una respuesta JSON limpia
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    # Loguea el error interno con traceback completo
    logger.error(f"Error dont controlled in Path: {request.url.path}", exc_info=True)
    
    # Devuelve un error 500 genérico al cliente
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error. Check logs for Request ID."},
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=4000, 
        reload=True, 
        log_level="info"
    )