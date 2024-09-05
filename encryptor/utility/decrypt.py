from encryptor.utility.cryption_frame import CryptionFrame
from tkinter import messagebox


class DecryptionFrame(CryptionFrame):
    button_text = "DECRYPT MESSAGE"
    upper_box_text = "Enter Text To Decrypt"
    lower_box_text_type = "decrypt"
    lower_box_initial_text = "PLAIN TEXT"

    button_color = '#00ab13'


    def __init__(self, parent, text):
        super().__init__(parent, text)
        self.decrypt_input = self.upper_box
        self.decrypt_output = self.lower_box
        self.__backend = self.get_backend()
        self.decrypt_key = self.middle_box
        self.action_button.configure(command=self.decrypt_text)

    def decrypt_text(self):
        input_text = self.decrypt_input.get("1.0", "end").replace("\n", " ")
        user_key = self.decrypt_key.get()
        if input_text:
            if user_key:
                self.decrypt_output.configure(state="normal")
                self.decrypt_output.delete("1.0", "end")
                self.__backend.set_text(input_text)
                self.__backend.set_key(user_key)
                result = self.__backend.decrypt()
                self.decrypt_output.insert("1.0", result)
                self.decrypt_output.configure(state='disabled')
            else:
                messagebox.showerror("ERROR", "Please enter Key")
        else:
            messagebox.showerror("ERROR", "Please enter text to encrypt")
