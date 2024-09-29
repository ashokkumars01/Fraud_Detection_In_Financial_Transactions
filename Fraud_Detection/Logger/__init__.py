import logging
from datetime import datetime

import os

LOG_FOLDER_NAME = "Logs"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME = f"log{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_FOLDER_NAME, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FOLDER_NAME, LOG_FILE_NAME)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log to a file named 'app.log'
    filemode='w',
    level=logging.INFO,  # Log messages with level ERROR and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)