import logging
from fastapi import APIRouter, status
from models.request import Keys

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
def get_tokens():
    logging.info("Request")
    return