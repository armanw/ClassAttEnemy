import logging
from datetime import datetime

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"logs{datetime.now().strftime("%Y%m%d %H%M")}", mode="a")

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(level=logging.INFO)
console_handler.setLevel(level=logging.DEBUG)
file_handler.setLevel(level=logging.WARNING)

formater = logging.Formatter("{asctime} {levelname}: {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formater)
file_handler.setFormatter(formater)