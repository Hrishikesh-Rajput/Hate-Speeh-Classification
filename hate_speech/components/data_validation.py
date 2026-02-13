import os
import pandas as pd
import yaml
from hate_speech.entity.config_entity import DataValidationConfig
from hate_speech.entity.artifact_entity import DataValidationArtifacts

class DataValidation:

    def __init__(self, data_validation_config: DataValidationConfig):
        self.data_validation_config = data_validation_config

    def read_schema(self):
        with open(self.data_validation_config.schema_file_path, "r") as file:
            return yaml.safe_load(file)

    def validate_columns(self, df, schema):
        schema_columns = schema["columns"].keys()
        return all(column in df.columns for column in schema_columns)

    def validate_null_values(self, df):
        return not df.isnull().values.any()

    def initiate_data_validation(self):

        df = pd.read_csv(self.data_validation_config.train_file_path)
        schema = self.read_schema()
    
        print("Actual CSV Columns:", df.columns.tolist())
    
        # Remove unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
        # Drop null rows
        df = df.dropna()
    
        status = True
    
        if not self.validate_columns(df, schema):
            print("Column validation failed")
            status = False
    
        target_column = schema["target_column"]
    
        if df[target_column].nunique() < 2:
            print("Only one class found")
            status = False
    
        return DataValidationArtifacts(validation_status=status)


