from itertools import cycle


class VigeneraCrypt:
    def __init__(self, plain_text, key):
        self.__text = plain_text
        self.__key = key
        self.__cycle = cycle(key)

    def encrypt(self):
        encrypted_letters = [
            chr(((ord(plain) + ord(key_text)) % 26) + 65) for plain, key_text in self.__bind_text_with_key()
        ]
        result = "".join(encrypted_letters)
        return result

    def decrypt(self):
        decrypted_letters = [
            chr(((ord(plain) - ord(key_text)) % 26) + 65) for plain, key_text in self.__bind_text_with_key()
        ]

        result = "".join(decrypted_letters)

        return result

    def __bind_text_with_key(self):
        return [tuple(zip(letter, next(self.__cycle)))[0] for letter in self.__text]
