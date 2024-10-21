from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os
import sys
from datetime import datetime
from sklearn.model_selection import train_test_split
import pandas as pd
from src.components.data_trnsformation import DataTransformationConfig,DataTransformation


@dataclass #decorator
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")#artifacts is created in current working directory
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

#data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        #reading the dataset
        try:
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
#exception handling for data ingestion component 
#exception is used to handle the errors in python
        except Exception as e:
            raise CustomException(e,sys)
        
#main function to initiate the ingestion component
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

    
        
