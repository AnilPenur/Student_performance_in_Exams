
import sys

from src.components.data_ingestion import Data_Ingestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.logger import logging
from src.exception import CustomException_ANIL



class TrainingPipeline:
    '''TrainingPipeline class::
    It will take datapoint from app.py as input and using `preprocdessor.pkl` the datapoint will be transformed 
    into the input required for the object of `ModelTrainer()`. The best model is output having maximum r2_score 
    and its pickel file is createde into artifacts folder.
    '''
    def __init__(self):
        pass

    def training(self):
        logging.info('training_pipeline.py:: Training has been started')
        try:
            data_ingestion_object = Data_Ingestion()
            train_path, test_path = data_ingestion_object.initiate_data_ingestion()
            logging.info('training_pipeline.py:: Pdata insgestion has been done')

            data_transformation_object = DataTransformation()
            train_t_dataset, test_t_dataset = data_transformation_object.initiate_data_transformation(train_path, test_path)
            logging.info('training_pipeline.py:: data transformation has been done')


            data_training_object = ModelTrainer()
            train_output_str = data_training_object.initiate_model_training(train_t_dataset, test_t_dataset)
            print(train_output_str)
            logging.info('training_pipeline.py:: data training has been done')

        except Exception as e:
            raise CustomException_ANIL(e,sys)

if __name__=="__main__":
    training_pipeline_object = TrainingPipeline()
    training_pipeline_object.training()