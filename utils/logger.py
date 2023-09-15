import datetime

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def info(self, message):
        self._log("INFO", message)

    def error(self, message):
        self._log("ERROR", message)

    def _log(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] - {message}"
        with open(self.log_file_path, "a") as log_file:
            log_file.write(log_entry + "\n")