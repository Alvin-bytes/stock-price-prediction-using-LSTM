import pandas as pd
from utils.logger import Logger
from utils.exception import CustomException

class DataIngestor:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.logger = Logger("data_ingestion.log")

    def ingest_data(self):
        try:
            # Logic to ingest data from the specified file
            data = pd.read_csv(self.data_file_path)
            self.logger.info("Data ingestion successful.")
            return data
        except Exception as e:
            error_message = f"Failed to ingest data: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message)