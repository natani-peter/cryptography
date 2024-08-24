from vigenera.backend.validators import Validator
from vigenera.backend.loggers import Logger
from vigenera.backend.cryption import VigeneraCrypt


class VigeneraBackend:
    __validator = Validator()

    def __init__(self):
        self.__name__ = "VigeneraBackend"
        self.__logger = Logger("Natani Peter").logger
        self.__key = ""
        self.__text = ""

    @property
    def key(self):
        return self.__key

    @property
    def logger(self):
        return self.__logger

    @property
    def text(self):
        return self.__text

    @key.setter
    @__validator.clean_text
    @__validator.verify("key")
    def key(self, key_text) -> None:
        self.__key = "".join(key_text)
        self.__logger.info("Key is set to \"{}\"".format(" ".join(key_text)))

    @text.setter
    @__validator.clean_text
    def text(self, user_text):
        self.__text = user_text
        self.__logger.info("Plain Text is set to \"{}\"".format(" ".join(user_text)))

    def encrypt(self):
        self.__logger.info(f"Encrypting".upper())
        result = " ".join([VigeneraCrypt(word, self.key).encrypt() for word in self.text])
        self.__logger.info(f"Result: \"{result}\"\n\n")
        return result, self.text, self.key

    def decrypt(self):
        self.__logger.info(f"Decrypting".upper())
        result = " ".join([VigeneraCrypt(word, self.key).decrypt() for word in self.text])
        self.__logger.info(f"Result: \"{result}\"\n\n")
        return result, self.text, self.key
