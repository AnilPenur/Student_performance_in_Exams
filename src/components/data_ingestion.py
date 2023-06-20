import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException_ANIL

from dataclasses import dataclass
# you can instantiate, print, and compare data class instances straight out of the box

@dataclass
class DataIngestionConfig:
    train_dataset_path:str = os.path.join("artifacts",'train.csv')
    test_dataset_path:str = os.path.join("artifacts",'test.csv')
    raw_dataset_path:str = os.path.join("artifacts",'raw.csv')

class Data_Ingestion:
    '''Data_Ingestion class 
    Constructor will creates three paths for train, test and raw dataset.
    Data is read from csv file, and spilted into train and test dataset.
    Saved these files at their respective path and Finally returned the path for train and test dataset,
     so that they are read whenever their requirement occures.
    '''
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('data_ingestion.py:: Data Ingestion has been started')
        try:
            # Edit this path for new dataset
            dataset_path = "src/notebook/data/stud.csv"
           
            df = pd.read_csv(dataset_path)

            train_set ,test_set = train_test_split(df , test_size= 0.2, random_state= 43)
            logging.info("data_ingestion.py:: Dataset is splitted into train and test set having test size 20 percent")

            os.makedirs(name= os.path.dirname(self.data_ingestion_config.train_dataset_path),
                        exist_ok= True
                        )

            train_set.to_csv(self.data_ingestion_config.train_dataset_path, index= False)
            test_set.to_csv(self.data_ingestion_config.test_dataset_path, index= False)
            df.to_csv(self.data_ingestion_config.raw_dataset_path, index= False)

            logging.info("data_ingestion.py:: Data Ingestion is done, data saved in 'artifact' folder")

            return (
                self.data_ingestion_config.train_dataset_path,
                self.data_ingestion_config.test_dataset_path
            )

        except Exception as e:
            raise CustomException_ANIL(e,sys)

# data igestion test here using logs folder
# if __name__=='__main__':
#     data_ingestion_object = Data_Ingestion()
#     data_ingestion_object.initiate_data_ingestion()
