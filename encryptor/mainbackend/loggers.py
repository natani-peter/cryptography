import logging
from logging.handlers import RotatingFileHandler
import os


class Logger:
    __instance = None

    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)

        # rotating file logger for everything

        script = os.path.dirname(os.path.abspath(__file__))
        log_folder = os.path.join(script, 'my_logs')

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        filename = f"vigeneraLogs.log"
        location = os.path.join(log_folder, filename)

        self.__handler = RotatingFileHandler(location, maxBytes=1000,
                                             backupCount=4)
        self.__handler.setLevel(logging.DEBUG)
        self.__formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        self.__handler.setFormatter(self.__formatter)

        # stream logger for top errors
        self.__stream_handler = logging.StreamHandler()
        self.__stream_handler.setLevel(logging.WARNING)
        self.__stream_handler.setFormatter(self.__formatter)

        # add loggers
        self.__logger.addHandler(self.__stream_handler)
        self.__logger.addHandler(self.__handler)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
            return cls.__instance
        return cls.__instance

    @property
    def logger(self):
        return self.__logger


custom_logger = Logger("Custom Logger").logger
