class UserAnswer:
    print(
        "NOTICE          NOTICE           NOTICE      NOTICE\n"
        "By default, the app is set for encryption purposes.\n"
        "If you want to decrypt, Press any key to  Otherwise the 'ENTER' key")
    choice = input()
    action = 1 if choice else 0
    name = 'Cipher' if action else "Plain"
    text = input(f"What's your {name} text? ")
    key = input("Enter the key: ")

    @staticmethod
    def collect_key(value):
        isValid = False
        while not isValid:
            new_key = input("Please enter a valid key: ")
            if value % len(new_key) == 0:
                print("---------------------------------------------------------")
                return new_key
            else:
                print(f"Choose a key whose length is a factor of {value} and has no spaces")


class Vigenere:

    def __init__(self):
        import string
        self.__key = ""
        self.__text = ""
        self.__message = ""
        self.__action = 0
        self.number_index = dict(enumerate(string.ascii_lowercase))
        self.letter_index = {item[1]: item[0] for item in self.number_index.items()}
        self.blocks = []
        self.zipped_numerical_letters = []

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = Vigenere.__clean_user_input(value)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        cleaned_key = Vigenere.__clean_user_input(value)
        if not self.text:
            word = 'Cipher' if self.__action else 'Plain'
            print(f"You can't set the key before setting the {word} text.")
        if len(self.text) % len(cleaned_key) == 0:
            self.__key = cleaned_key
        else:
            print(f"Choose a key whose length is a factor of {len(self.text)} and has no spaces")

    def __change_action(self):
        self.__action = 1

    @staticmethod
    def __clean_user_input(plain_text: str) -> str:
        return plain_text.strip().lower().replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

    def divide_plain_text_into_blocks_of_the_key(self, plain_text: str):
        if len(plain_text) == 0:
            return
        else:
            first, remainder = plain_text[:len(self.key)], plain_text[len(self.key):]
            self.blocks.append(first)
            self.divide_plain_text_into_blocks_of_the_key(remainder)

    def letter_to_number_zip_with_the_key(self, letter: str, key: str) -> zip:
        number_block = [self.letter_index.get(value, -1) for value in letter]
        numerical_key = [self.letter_index.get(value, -1) for value in key]
        return zip(number_block, numerical_key)

    def main(self):
        user_input = UserAnswer()
        self.text = user_input.text
        self.key = user_input.key
        if self.key:
            print("---------------------------------------------------------")
        else:
            self.key = user_input.collect_key(len(self.text))
        if user_input.action:
            self.__change_action()
        self.divide_plain_text_into_blocks_of_the_key(self.text)
        if self.key:
            if self.__action:
                self.__mimic_work("Decrypting")
                print(f"The Plain text is {self.__decrypt().lower()}")
                return
            self.__mimic_work("Encrypting")
            print(f"The Cipher text is {self.__encrypt().upper()}")

    def __mimic_work(self, activity):
        import time
        print(f"{activity}: \"{self.text}\" with key: \"{self.key}\" ")
        time.sleep(1)
        print(f"{activity}.")
        time.sleep(1)
        print(f"{activity}..")
        time.sleep(1)
        print(f"{activity}...")
        time.sleep(1)
        print("Done.")

    def __encrypt(self) -> str:
        for block in self.blocks:
            block_list = list(self.letter_to_number_zip_with_the_key(block, self.key))
            self.zipped_numerical_letters += block_list

        return "".join([self.number_index.get(cipher_letter) for cipher_letter in
                        [sum(letter) % 26 for letter in self.zipped_numerical_letters]])

    def __decrypt(self) -> str:
        cipher_numerical_letters = []

        for block in self.blocks:
            block_list = list(self.letter_to_number_zip_with_the_key(block, self.key))
            self.zipped_numerical_letters += block_list

        for letter in self.zipped_numerical_letters:
            difference = letter[0] - letter[1]

            if difference > 0:
                cipher_numerical_letters.append(difference)
            else:
                cipher_numerical_letters.append(difference + 26)

        return "".join([self.number_index.get(cipher_letter) for cipher_letter in cipher_numerical_letters])


if __name__ == "__main__":
    Vigenere().main()
