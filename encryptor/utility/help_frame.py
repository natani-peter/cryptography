import customtkinter as ctk


class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, corner_radius=10)
        self.__name = kwargs.get('name', '').title()

        title_label = ctk.CTkLabel(
            self, text=f"{self.__name.upper()}\nHELP", font=("Times New Roman", 35), justify='center'
        )
        title_label.pack(pady=2)
        help_text = (f"\n\nThis tool allows you to encrypt and decrypt text \nUsing the {self.__name}.\n\nENCRYPT "
                     f"TAB\nEnter the text  to encrypt in the input area. \nClick the  button to generate the "
                     f"encrypted text. \nThe encrypted text will appear in the output area. \n\nDECRYPT TAB\nEnter "
                     f"the text  to decrypt in the input area. \nClick the  button to retrieve the original text. "
                     f"\nThe decrypted text will appear in the  output area. \n\nNote:\n* The text entered should not "
                     f"contain none english letters and punctuation marks.\n\n"
                     f"{"* The Key must be in the  form 'ax + b' or 'ax + -b' where a and b are natural numbers.\n\n"
                        if self.__name[0] == "A" else ""}For Any Bugs Reach Out to 'natanipeter@gmail.com'")

        help_label = ctk.CTkLabel(
            self,
            text=help_text,
            wraplength=350,
            justify="center",
            anchor="nw",
            font=("Times New Roman", 17),
            text_color='white'
        )
        help_label.pack(pady=5)
        self.pack(fill="both", expand=True, padx=5, pady=5)
