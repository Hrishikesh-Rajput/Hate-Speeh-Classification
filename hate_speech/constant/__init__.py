import os
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)

BUCKET_NAME = "hate-speech-ml-data"
ZIP_FILE_NAME = "dataset.zip"
S3_DATA_KEY = "data/raw/dataset.zip"

LABEL = "label"
TWEET = "tweet"

# data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngetionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR= "imbalance_data.csv"
DATA_INGESTION_RAW_DATA_DIR= "raw_data.csv"
