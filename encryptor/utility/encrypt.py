from encryptor.utility.cryption_frame import CryptionFrame
from tkinter import messagebox


class EncryptionFrame(CryptionFrame):
    button_text = "ENCRYPT MESSAGE"
    upper_box_text = "Enter Text To Encrypt"
    lower_box_text_type = "decrypt"
    lower_box_initial_text = "CIPHER TEXT"

    button_color = '#3333ff'


    def __init__(self, parent, text):
        super().__init__(parent, text)
        self.encryption_input = self.upper_box
        self.encryption_output = self.lower_box
        self.__backend = self.get_backend()
        self.encrypt_key = self.middle_box
        self.action_button.configure(command=self.encrypt_text)

    def encrypt_text(self):
        input_text = self.encryption_input.get("1.0", "end").replace("\n", " ")

        user_key = self.encrypt_key.get()
        if input_text:
            if user_key:
                self.encryption_output.configure(state="normal")
                self.encryption_output.delete("1.0", "end")
                self.__backend.set_text(input_text)
                self.__backend.set_key(user_key)
                result = self.__backend.encrypt()
                self.encryption_output.insert("1.0", result)
                self.encryption_output.configure(state='disabled')
            else:
                messagebox.showerror("ERROR", "Please enter Key")
        else:
            messagebox.showerror("ERROR", "Please enter text to encrypt")
