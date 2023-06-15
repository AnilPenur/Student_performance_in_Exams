import logging
import os
from datetime import datetime

date_time_format = '%d_%m_%Y_%H_%M_%S'
LOG_FILE = f"{datetime.now().strftime(date_time_format)}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)
log_file_path = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename =  log_file_path,
    format="[%(asctime)s] %(lineno)s %(name)s - %(levelname)s %(message)s",
    level= logging.INFO
)

#code testing below
# if __name__=="__main__":
#     logging.info('I am testing logger.py file')