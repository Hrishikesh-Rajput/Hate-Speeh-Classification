import sys
import os 
from hate_speech.logger import logging
from hate_speech.exception import HateSpeechException
from hate_speech.components.data_ingestion import DataIngestion 

from hate_speech.entity.config_entity import (DataIngestionConfig)
from hate_speech.entity.artifact_entity import (DataIngestionArtifacts)
from hate_speech.components.data_validation import DataValidation
from hate_speech.entity.config_entity import DataValidationConfig
from hate_speech.entity.artifact_entity import DataValidationArtifacts


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from S3 Storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from S3 Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise HateSpeechException(e, sys) from e
    
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:

            # ==============================
            # 1️⃣ Data Ingestion
            # ==============================
            data_ingestion_artifacts = self.start_data_ingestion()
            logging.info("Data Ingestion completed")

            # ==============================
            # 2️⃣ Data Validation
            # ==============================
            data_validation_config = DataValidationConfig(
                schema_file_path="hate_speech/configuration/schema.yaml",
                train_file_path=data_ingestion_artifacts.raw_data_file_path,
                validation_status_file_path=os.path.join("artifacts", "validation_status.txt")
            )

            data_validation = DataValidation(
                data_validation_config=data_validation_config
            )

            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info("Data Validation completed")

            if not data_validation_artifacts.validation_status:
                raise Exception("Data Validation Failed ❌")

            logging.info("Data Validation Passed ✅")

            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise HateSpeechException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:

        data_validation_config = DataValidationConfig(
            schema_file_path="hate_speech/config/schema.yaml",
            train_file_path=data_ingestion_artifacts.raw_data_file_path,
            validation_status_file_path=os.path.join("artifacts", "validation_status.txt")
        )

        data_validation = DataValidation(data_validation_config=data_validation_config)

        return data_validation.initiate_data_validation()
