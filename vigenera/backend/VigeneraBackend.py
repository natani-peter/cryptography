from encryptor.mainbackend.validators import Validator
from vigenera.backend.cryption import VigeneraCrypt
from encryptor.mainbackend.main_backend import InterfaceBackend


class VigeneraBackend(InterfaceBackend):
    __validator = Validator()

    def __init__(self):
        super().__init__()
        self.__name__ = "VigeneraBackend"
        self.__key = ""
        self.__text = ""

    @__validator.clean_text
    @__validator.verify("key")
    def set_key(self, key_text) -> None:
        self.__key = "".join(key_text)
        self.logger.info(f"-{self.__name__} Key is set to \"{" ".join(key_text)}\"")

    @__validator.clean_text
    def set_text(self, user_text):
        self.__text = user_text
        self.logger.info(f"{self.__name__} Plain Text is set to \"{" ".join(user_text)}\"")

    def encrypt(self):
        self.logger.info(f"Encrypting".upper())
        result = " ".join([VigeneraCrypt(word, self.__key).encrypt() for word in self.__text])
        self.logger.info(f"{self.__name__} Result: \"{result}\"\n\n")
        return result

    def decrypt(self):
        self.logger.info(f"Decrypting".upper())
        result = " ".join([VigeneraCrypt(word, self.__key).decrypt() for word in self.__text])
        self.logger.info(f"{self.__name__} Result: \"{result}\"\n\n")
        return result
