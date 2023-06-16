import pandas as pd
import numpy as np
import os

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import sys
from src.exception import CustomException_ANIL
from src.logger import logging
from src.utils import save_object
from src.components.data_ingestion import Data_Ingestion

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_pkl_file_path:str = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_preprocessor_pkl_file(self):
        logging.info("Entered into get_preprocessor_pkl_file method")
        try:
            
            #add cat_featutres and Numerical feature in utils and import here
            num_columns = ['reading_score', 'writing_score']
            cat_columns = ['gender','race_ethnicity','parental_level_of_education',
                           'lunch','test_preparation_course']
            
            num_pipeline = Pipeline(
                steps=[
                    ('Misiing value Imputer',SimpleImputer(strategy= 'median' )),
                    ('Standard Scaling', StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('missing value imputer', SimpleImputer(strategy= 'most_frequent')),
                    ('One Hot Encoding',OneHotEncoder()),
                    ('Standard Scaling', StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer(
                transformers= [
                    ('numerical columns', num_pipeline, num_columns),
                    ('categorical columns', cat_pipeline, cat_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException_ANIL(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try: 
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)
            logging.info("The train and test dataset has been loaded")

            target_column = "math_score"

            df_train_input_feature = df_train.drop(columns=target_column, axis=1)
            df_train_target_feature = df_train[target_column]
            df_test_input_feature = df_test.drop(columns=target_column, axis=1)
            df_test_target_feature = df_test[target_column]
            logging.info("dependent and independent features are seprated")

            preprocessor_object = self.get_preprocessor_pkl_file()

            df_train_input_feature_transformed = preprocessor_object.fit_transform(df_train_input_feature)
            df_test_input_feature_transformed = preprocessor_object.transform(df_test_input_feature)
            logging.info("Independent feature are transformed using preprocessor object")

            df_train_transformed = np.c_[df_train_input_feature_transformed,np.array(df_train_target_feature)]
            df_test_transformed = np.c_[df_test_input_feature_transformed,np.array(df_test_target_feature)]

            logging.info("independent feature and dependent feature dataset are merged and its value is returned")

            save_object(
                file_path= self.data_transformation_config.preprocessor_pkl_file_path,
                obj = preprocessor_object
            )
            logging.info('Preprocessor file is created')

            return (
                df_train_transformed,
                df_test_transformed,
                self.data_transformation_config.preprocessor_pkl_file_path
            )

        except Exception as e:
            raise CustomException_ANIL(e,sys)

# testing of data transformation code
# if __name__=="__main__":
#     data_ingestion_object = Data_Ingestion()
#     train_path,test_path = data_ingestion_object.initiate_data_ingestion()
#     print('train_path',train_path)
#     print('test_path',test_path)
#     data_transformation_object = DataTransformation()
#     data_transformation_object.initiate_data_transformation(train_path,test_path)