import dill
import pickle
import os
import sys

from src.logger import logging
from src.exception import CustomException_ANIL



def save_object(file_path:str, obj):
    try:
        os.makedirs(name=os.path.dirname(file_path), exist_ok=True )
        logging.info(f'Directory "{os.path.dirname(file_path)}" is created')

        with open(file=file_path, mode= "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"object is saved at a file path:{file_path}")
    except Exception as e:
        raise CustomException_ANIL(e,sys)

