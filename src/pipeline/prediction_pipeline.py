import sys

from src.logger import logging
from src.exception import CustomException_ANIL
from src.utils import load_object, CustomData

from src.components.model_trainer import ModelTrainerConfig
from src.components.data_transformation import DataTransformationConfig




class Predict:
    '''Class Predict():
    It will take a datapoint from from front end web application. It will load pickel files of model and preprocessor.
    The datapoint will be transformed and then model is used to find the output at that datapoint. Finally It will Show 
    result on webapplication.
    '''
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = ModelTrainerConfig().trained_model_path
            preprocessor_path = DataTransformationConfig().preprocessor_pkl_file_path

            model = load_object(model_path)
            preprocessor = loda_object(preprocessor_path)

            df_transformed = preprocessor.transform(features) 
            prediction = model.predict(df_transformed)

            
        except Exception as e:
            raise CustomException_ANIL(e, sys)