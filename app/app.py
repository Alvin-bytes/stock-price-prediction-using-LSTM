from flask import Flask, render_template
from utils.logger import Logger
from utils.exception import CustomException

app = Flask(__name__)
logger = Logger("app.log")

@app.route('/')
def index():
    try:
        return render_template('index.html')

    except Exception as e:
        error_message = f"Failed to render template: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message)

if __name__ == '__main__':
    app.run()