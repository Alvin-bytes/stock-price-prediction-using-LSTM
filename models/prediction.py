import logging
from utils.logger import Logger
from utils.exception import CustomException
from tensorflow.keras.models import load_model

class ModelLoader:
    def __init__(self):
        self.logger = Logger("model_loading.log")

    def load_model(self, file_path):
        try:
            # Logic for loading the trained model from a file
            loaded_model = load_model(file_path)

            self.logger.info("Model loading successful.")
            return loaded_model

        except Exception as e:
            error_message = f"Failed to load the model: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message)

class StockPricePredictor:
    def __init__(self):
        self.logger = Logger("prediction.log")

    def predict(self, model, data):
        try:
            # Logic for making stock price predictions using the trained model
            X_test = preprocess_data(data)  # Assuming you have a preprocess_data function

            predictions = model.predict(X_test)

            self.logger.info("Stock price prediction successful.")
            return predictions

        except Exception as e:
            error_message = f"Failed to make stock price predictions: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message) 
