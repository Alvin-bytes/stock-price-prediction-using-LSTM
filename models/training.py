import logging
from utils.logger import Logger
from utils.exception import CustomException
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class StockPriceTrainer:
    def __init__(self):
        self.logger = Logger("training.log")

    def train_model(self, data):
        try:
            # Logic for training the stock price prediction model
            X_train, y_train = preprocess_data(data)  # Assuming you have a preprocess_data function

            model = Sequential()
            model.add(LSTM(128, input_shape=(X_train.shape[1], X_train.shape[2])))
            model.add(Dense(1))

            model.compile(optimizer='adam', loss='mse')
            model.fit(X_train, y_train, epochs=10, batch_size=32)

            self.logger.info("Model training successful.")
            return model

        except Exception as e:
            error_message = f"Failed to train the model: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message) 
