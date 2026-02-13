from dataclasses import dataclass
from hate_speech.constant import *
import os 

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME
        self.ZIP_FILE_NAME = ZIP_FILE_NAME
        self.S3_DATA_KEY = S3_DATA_KEY   
        
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(),
            ARTIFACTS_DIR,
            DATA_INGESTION_ARTIFACTS_DIR
            
        )

        self.DATA_ARTIFACTS_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_INGESTION_IMBALANCE_DATA_DIR
        )

        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_INGESTION_RAW_DATA_DIR
        )

        self.ZIP_FILE_DIR = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR
        )

        self.ZIP_FILE_PATH = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            self.ZIP_FILE_NAME
        )

@dataclass
class DataValidationConfig:
    schema_file_path: str
    train_file_path: str
    validation_status_file_path: str

