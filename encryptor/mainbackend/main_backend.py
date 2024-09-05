from abc import ABC, abstractmethod
from .loggers import custom_logger


class InterfaceBackend(ABC):
    def __init__(self):
        self.logger = custom_logger

    @abstractmethod
    def set_text(self, text):
        pass

    @abstractmethod
    def set_key(self, key):
        pass

    @abstractmethod
    def encrypt(self):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError
