import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from src.logger import logging
from dataclasses import dataclass
from src.CustomException import CustomException  
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("Artifacts", "Breast_Cancer_Disease", "Raw_data.csv")
    train_data_path: str = os.path.join("Artifacts", "Breast_Cancer_Disease", "Train_data.csv")
    test_data_path: str = os.path.join("Artifacts", "Breast_Cancer_Disease", "Test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Breast Cancer Disease: Data ingestion phase started")
        try:
            # Ensure the correct dataset path is used
            data_path = "C:/AcuMedX/notebook/data/diabetes.csv"  # Update if needed
            data = pd.read_csv(data_path)
            logging.info(f"Breast Cancer Disease: Read the data from {data_path}")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Breast Cancer Disease: Created the raw data file")

            logging.info("Breast Cancer Disease: Splitting the data into train and test")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Breast Cancer Disease: Data Splitting is done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Breast Cancer Disease: Created the train and test data files")
            logging.info("Breast Cancer Disease: Data ingestion completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        
        except Exception as e:
            logging.error("Exception occurred while ingesting the data")
            raise CustomException(e, sys)  # Fixed exception name

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()  # Added missing parentheses
