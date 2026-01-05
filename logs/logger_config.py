import sys
import logging
from pythonjsonlogger import jsonlogger

def setup_logging():
    LOG_FORMAT = (
        '%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d %(message)s'
    )

    formatter = jsonlogger.JsonFormatter(LOG_FORMAT)

    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(formatter)

    logger = logging.getLogger()

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)