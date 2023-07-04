import dill
import pickle
import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException_ANIL

from sklearn.metrics import r2_score,accuracy_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path:str, obj):
    try:
        os.makedirs(name=os.path.dirname(file_path), exist_ok=True )
        logging.info(f'Directory "{os.path.dirname(file_path)}" is created')

        with open(file=file_path, mode= "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"object is saved at a file path:{file_path}")
    except Exception as e:
        raise CustomException_ANIL(e,sys)

def  evaluate_models(X_train,y_train,X_test,y_test,models:dict,params:dict):
    logging.info('evaluating the given models based on r2 score')
    try:
        report = dict()
        for model_name,model in models.items():
            logging.info(model)
            parameter_dict = params[model_name]
            gd = GridSearchCV(estimator=model, param_grid= parameter_dict,
                              cv=3, n_jobs=-1,verbose=2 ,scoring=accuracy_score)
            gd.fit(X = X_train, y = y_train)
            logging.info(f'utils.py:: GridSearchCV best estimator: {gd.best_estimator_} ')
            logging.info(f'utils.py:: GridSearchCV best parameters: {gd.best_params_} ')

            model.set_params(**gd.best_params_)
            model.fit(X = X_train, y = y_train)
            preds = model.predict(X_test)

            logging.info('utils.py:: best model is utilised to find r2 score')
            r2 = r2_score(y_test, preds)
            report[model_name] = r2
            logging.info(f'utils.py:: best model is {model} and r2 score is {r2}')

        return report
    except Exception as e:
        raise CustomException_ANIL(e, sys)
        

def load_object(file_path:str):
    '''It will help in loading object(pickel) file using dill module'''
    logging.info("loading object is started")
    try:
        with open(file_path,mode="rb") as file_obj:
            logging.info(f"object is saved at a file path:{file_path}")
            return dill.load(file_obj)
        
    except Exception as e:
        raise CUstomException_ANIL(e,sys)


class CustomData:
    '''
    calss CustomData()::
    In constructor it will take all features of a datapoint as patrameters.
    The method of the class `` will convert this datapoint into a dataframe having 
    columns as features and row having values.
    '''
    def __init__(self, 
                gender:str, 
                race_ethnicity:str, 
                parental_level_of_education:str,
                lunch:str,
                test_preparation_course:str,
                reading_score:int,
                writing_score:int):

                self.gender = gender
                self.race_ethnicity = race_ethnicity
                self.parental_level_of_education = parental_level_of_education
                self.lunch = lunch
                self.test_preparation_course = test_preparation_course
                self.reading_score = reading_score
                self. writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict:dict ={
                'gender':[self.gender], 
                'race_ethnicity':[self.race_ethnicity], 
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self. writing_score]
             }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException_ANIL(e,sys)


