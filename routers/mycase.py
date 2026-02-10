import logging
from typing import Optional
from models.request import Keys
from fastapi import APIRouter, status, Query

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/MyCase",
    tags=["Mycase"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_tokens(
    request: Keys
):
    logging.info(request)
    return request

@router.get("/")
def get_tokens(code : Optional[str] = Query(None)):

    if code:
        logging.info(f"Code: {code}")
        return {"Status":"Success", "Received_code":code}
    
    logger.warning("The code does not provided")
    return{"Status":"Error", "Message":"No code provided"}