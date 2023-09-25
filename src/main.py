from config import settings
from log_x import log_arbiter
from time import sleep

logger = log_arbiter(__name__)

if __name__ == "__main__":
    """This is the main function or the entrypoint of the project IOT SMART BUILDING"""
    while True:
        logger.info("Welcome to IOT SMART HOME ... :)")
        sleep(1)
