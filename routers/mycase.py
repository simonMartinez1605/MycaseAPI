import logging
from fastapi import APIRouter, status

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/MyCase",
    tags=["TLA"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_tokens(
    request
):
    logging.info(request)
    return request

@router.get("/")
def get_tokens():
    return 