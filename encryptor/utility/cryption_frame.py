import customtkinter as ctk
from encryptor.utility.widgets import TextBoxWidget, LabelWidget
from encryptor.mainbackend.main_backend import InterfaceBackend


class CryptionFrame(ctk.CTkFrame):
    button_text = ""
    upper_box_text = ""
    lower_box_text_type = ""
    lower_box_initial_text = ""

    def __init__(self, parent, text):
        super().__init__(master=parent)
        self.backend = self.get_backend()
        self.name = parent.master.name

        LabelWidget(self, text=self.name)
        self.upper_box = TextBoxWidget(self, text=self.upper_box_text)
        self.upper_box.pack(expand=True, fill="both")

        self.middle_box = ctk.CTkEntry(self, width=300, corner_radius=5, placeholder_text=text, fg_color='#222',
                                       text_color='white')
        self.middle_box.pack(expand=False, fill="both", pady=8, ipady=2)

        self.action_button = ctk.CTkButton(self, text=self.button_text)
        self.action_button.pack(pady=4, ipady=2)

        self.lower_box = TextBoxWidget(self, text="", text_box_type=self.lower_box_text_type)
        self.lower_box.insert("1.0", self.lower_box_initial_text)
        self.lower_box.configure(state="disabled")
        self.lower_box.pack(expand=True, fill="both", pady=8)

    @staticmethod
    def get_backend(name="") -> InterfaceBackend:
        from vigenera.backend.VigeneraBackend import VigeneraBackend

        backend = VigeneraBackend()
        if name:
            pass
        return backend
