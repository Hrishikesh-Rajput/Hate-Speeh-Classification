# from hate_speech.logger import logging
# import sys
# import os
# from hate_speech.configuration.s3_syncer import S3Sync
# # s3 = S3Sync()
# # s3.sync_folder_from_s3(
# #     bucket_name="hate-speech-ml-data",
# #     filename="data/raw/dataset.zip",
# #     destination="data/raw"
# # )

import os
import sys
from hate_speech.logger import logging
from hate_speech.configuration.s3_syncer import S3Sync


def main():
    BUCKET_NAME = "hate-speech-ml-data"

    # S3 object key (path inside bucket)
    S3_DATA_KEY = "data/raw/dataset.zip"

    # Local destination folder
    LOCAL_DATA_DIR = os.path.join("data", "raw")

    s3 = S3Sync()

    logging.info("Downloading dataset from S3...")
    print("⬇️ Downloading dataset from S3...")

    downloaded_path = s3.sync_folder_from_s3(
        bucket=BUCKET_NAME,
        key=S3_DATA_KEY,
        destination=LOCAL_DATA_DIR
    )

    logging.info(f"Dataset downloaded to {downloaded_path}")
    print(f"✅ Downloaded to: {downloaded_path}")


if __name__ == "__main__":
    main()

