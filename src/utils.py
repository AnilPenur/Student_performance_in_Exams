import dill
import pickle
import os
import sys

from src.logger import logging
from src.exception import CustomException_ANIL

from sklearn.metrics import r2_score


def save_object(file_path:str, obj):
    try:
        os.makedirs(name=os.path.dirname(file_path), exist_ok=True )
        logging.info(f'Directory "{os.path.dirname(file_path)}" is created')

        with open(file=file_path, mode= "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"object is saved at a file path:{file_path}")
    except Exception as e:
        raise CustomException_ANIL(e,sys)

def  evaluate_models(X_train,y_train,X_test,y_test,models:dict):
    logging.info('evaluating the given models based on r2 score')
    try:
        report = dict()
        for model_name,model in models.items():
            logging.info(model)
            model.fit(X = X_train, y = y_train)
            preds = model.predict(X_test)
            r2 = r2_score(y_test, preds)
            report[model_name] = r2

        return report
    except Exception as e:
        raise CustomException_ANIL(e, sys)
