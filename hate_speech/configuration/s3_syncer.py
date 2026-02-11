import os

# class S3Sync:

#     def sync_folder_to_s3(self, bucket_name, filepath, filename):
#         """
#         Upload file to S3
#         """
#         command = f"aws s3 cp {filepath}/{filename} s3://{bucket_name}/{filename}"
#         os.system(command)

#     def sync_folder_from_s3(self, bucket_name, filename, destination):
#         """
#         Download file from S3
#         """
#         os.makedirs(destination, exist_ok=True)
#         command = f"aws s3 cp s3://{bucket_name}/{filename} {destination}/{filename}"
#         os.system(command)
import boto3

class S3Sync:
    def __init__(self):
        self.s3 = boto3.client("s3")

    def sync_folder_from_s3(self, bucket, key, destination):
        os.makedirs(destination, exist_ok=True)
        local_path = os.path.join(destination, os.path.basename(key))

        self.s3.download_file(bucket, key, local_path)
        return local_path

    def sync_folder_to_s3(self, bucket, key, filepath):
        self.s3.upload_file(filepath, bucket, key)

