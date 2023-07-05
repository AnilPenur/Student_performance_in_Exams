import sys

from src.logger import logging
from src.exception import CustomException_ANIL
from src.utils import CustomData
from src.utils import load_object

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

            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            logging.info('predict_pipelin.py::model and preprocessor pkl files a re loaded')

            df_transformed = preprocessor.transform(features) 
            prediction = model.predict(df_transformed)
            logging.info('prediction is done')
            # print(prediction)
            logging.info(f'prediction is:{prediction[0]}')

            return prediction[0]

        except Exception as e:
            raise CustomException_ANIL(e, sys)


# Test predict pipeline code
# if __name__=='__main__':
#     features = CustomData(
#         gender='female', 
#         race_ethnicity='group C',
#         parental_level_of_education='some college',
#         lunch='standard',
#         test_preparation_course='completed',
#         reading_score=69,
#         writing_score=90)
#     input_data = features.get_data_as_data_frame()
        							
#     pred_obj = Predict()
#     predicted_value = pred_obj.predict(features=input_data)
#     print('the output is probably 88:: predicted::',predicted_value)
#     logging.info('Prediction pipeline is complete')