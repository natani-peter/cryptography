import customtkinter as ctk


class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, )
        self.__name = kwargs.get('name', '').title()

        title_label = ctk.CTkLabel(
            self, text=f"{self.__name.upper()}\nHELP", font=("Helvetica", 35), justify='center'
        )
        title_label.pack(pady=5)
        help_text = (
            f"\n\nThis tool allows you to encrypt and decrypt text \nUsing the {self.__name}.\n\n\n"
            "1. Encrypt Tab\n\n"
            "Enter the text you want to encrypt in the input area. \n"
            "Click the 'Encrypt' button to generate the encrypted text. \n"
            "The encrypted text will appear in the read-only output area. \n\n\n\n"
            "2. Decrypt Tab\n\n"
            "Enter the text you want to decrypt in the input area. \n"
            "Click the 'Decrypt' button to retrieve the original text. \n"
            "The decrypted text will appear in the read-only output area. \n\n\n"
            "Note:\n\n"
            "The text entered should not contain none english letters  \n\nand punctuation marks.\n\n"
            f"{"The Key entered must be in the  form 'ax + b' or 'ax + -b' "
               "\n\nwhere a and b are natural numbers.\n\n" if self.__name[0] == "A" else ""}"
            "For Any Bugs Reach Out to natanipeter@gmail.com"
        )
        help_label = ctk.CTkLabel(
            self,
            text=help_text,
            wraplength=450,
            justify="center",
            anchor="nw",
            font=("Helvetica", 14),
            text_color='white'
        )
        help_label.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
