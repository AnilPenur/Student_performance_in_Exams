import os
import sys
import numpy as np


from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    AdaBoostRegressor,
    GradientBoostingRegressor
    )
# from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException_ANIL
from dataclasses import dataclass
from src.utils import evaluate_models,save_object
from src.components.data_ingestion import Data_Ingestion
from src.components.data_transformation import DataTransformation


@dataclass 
class ModelTrainerConfig():
    trained_model_path:str = os.path.join('artifacts',"model.pkl")

class ModelTrainer:
    """ModelTrainer Class::
    It's constructor start with creating a location to save model.pkl file after the best model is created.
    `initiate_model_training(train_array_t, test_arry_t)` method will take transformed array as input and 
    split into test and train array which seperates the X and y. Various algorithms are applied on the dataset,
    and the best model is dumped into pickel file.
    """
    logging.info('model_trainer.py:: Entered Model Trainer class')
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array_t, test_arry_t):
        logging.info('model_trainer.py:: model training started')
        try:
            X_train,y_train,X_test,y_test=(
                train_array_t[:,:-1],
                train_array_t[:,-1],
                test_arry_t[:,:-1],
                test_arry_t[:,-1]
            )
            logging.info('model_trainer.py:: X and y are seperated from train and test array')

            models:dict = {
                'linear regression':LinearRegression(),
                'KNeighborsRegressor':KNeighborsRegressor(),
                'DecisionTreeRegressor':DecisionTreeRegressor(),
                'RandomForestRegressor':RandomForestRegressor(),
                'AdaBoostRegressor':AdaBoostRegressor(),
                'GradientBoostingRegressor':GradientBoostingRegressor(),
                'CatBoostRegressor':CatBoostRegressor()
                #'XGBRegressor':XGBRegressor(),
            }

            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            #get best model from model report having 
            best_model_score = max(list(model_report.values()))
            best_model_name = list(model_report.keys())[np.argmax(list(model_report.values()))]

            # Check based on model score
            if best_model_score <=0.60:
                raise CustomException_ANIL("model_trainer.py:: Model performance is inadequate please try different settings")
            else:
                logging.info('model_trainer.py:: Model performance is acceptable')
            
            logging.info(f"model_trainer.py:: as per model_evaluation best model:{best_model_name} and best r2 score :{best_model_score}")

            best_model = models[best_model_name]
            best_model.fit(X_train,y_train)
            y_pred = best_model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            logging.info('model_trainer.py:: re-evaluating model and saving model to pickel file')
             
            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj=best_model
             )

            return "The best model is {} and having r2_score of {}".format(best_model_name, r2)

        except Exception as e:
            raise CustomException_ANIL(e, sys)


# #CHECK for model trainer 
# if __name__=='__main__':
#     model_trainer_object = ModelTrainer()
#     model_path = model_trainer_object.model_trainer_config.trained_model_path
#     print("model_path:",model_path)

#     data_ingestion_object = Data_Ingestion()
#     train_path,test_path = data_ingestion_object.initiate_data_ingestion()
#     print('train_path:',train_path)
#     print('test_path:',test_path)

#     data_transformation_object = DataTransformation()
#     df_train_t,df_test_t = data_transformation_object.initiate_data_transformation(train_path,test_path)
#     logging.info(" initiate_data_transformation is successfully executed")

#     r2 = model_trainer_object.initiate_model_training(df_train_t,df_test_t)
#     print('model_trainer successfully executed r2:',r2)
