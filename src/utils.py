import dill
import pickle
import os
import sys
import pandas as pd

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
        

def load_object(file_path:str):
    '''It will help in loading object(pickel) file using dill module'''
    try:
        with open(file_path,mode="rb") as file_obj:
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


