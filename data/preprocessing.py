import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from utils.logger import Logger
from utils.exception import CustomException

class DataPreprocessor:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        self.logger = Logger("data_preprocessing.log")

    def preprocess_data(self):
        try:
            # Logic to preprocess the data
            raw_data = pd.read_csv(self.raw_data_path)

            # Drop any duplicate rows
            raw_data.drop_duplicates(inplace=True)

            # Remove rows with missing values
            raw_data.dropna(inplace=True)

            # Convert the date column to datetime
            raw_data['Date'] = pd.to_datetime(raw_data['Date'])

            # Sort the data by date in ascending order
            raw_data.sort_values('Date', inplace=True)

            # Set the date column as the index
            raw_data.set_index('Date', inplace=True)

            # Scale numerical features using MinMaxScaler
            scaler = MinMaxScaler()
            scaled_data = scaler.fit_transform(raw_data[['Open', 'High', 'Low', 'Close', 'Volume']])
            scaled_df = pd.DataFrame(scaled_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index=raw_data.index)

            # Additional preprocessing steps...

            # Save the preprocessed data to a new file
            scaled_df.to_csv(self.processed_data_path)

            self.logger.info("Data preprocessing successful.")
            return scaled_df
        except Exception as e:
            error_message = f"Failed to preprocess data: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message)