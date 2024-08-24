import logging
from logging.handlers import RotatingFileHandler
import os


class Logger:
    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.DEBUG)

        # rotating file logger for everything
        self.__current_path = os.path.dirname(__file__)

        script = os.path.dirname(os.path.abspath(__file__))
        log_folder = os.path.join(script, 'my_logs')

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        filename = f"vigeneraLogs.log"
        location = os.path.join(log_folder, filename)

        self.__handler = RotatingFileHandler(location, maxBytes=1000,
                                             backupCount=4)
        self.__handler.setLevel(logging.DEBUG)
        self.__formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.__handler.setFormatter(self.__formatter)

        # stream logger for top errors
        self.__stream_handler = logging.StreamHandler()
        self.__stream_handler.setLevel(logging.WARNING)
        self.__stream_handler.setFormatter(self.__formatter)

        # add loggers
        self.__logger.addHandler(self.__stream_handler)
        self.__logger.addHandler(self.__handler)

    @property
    def logger(self):
        return self.__logger
