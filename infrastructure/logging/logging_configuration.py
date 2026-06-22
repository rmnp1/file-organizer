import logging
from pythonjsonlogger.json import JsonFormatter

class LoggingConfiguration:
    """
    centralized logging configuration for the application

    initializes the root logger and prevents duplicate
    handler registration
    """
    _initialized = False

    @classmethod
    def setup(cls):
        if cls._initialized:
            return

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()

            formatter = JsonFormatter(["asctime", "levelname", "message"], json_ensure_ascii=False)

            handler.setFormatter(formatter)
            logger.addHandler(handler)

        cls._initialized = True


