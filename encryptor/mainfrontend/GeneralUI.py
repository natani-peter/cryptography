import customtkinter as ctk
from encryptor.utility.encrypt import EncryptionFrame
from encryptor.utility.decrypt import DecryptionFrame
from encryptor.utility.help_frame import HelpFrame


class GeneralUI(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        self.title = "General UI"

        super().__init__(master=parent, anchor='center', corner_radius=10)


        self.__parent = parent
        self.__name = self.__parent.master.master.name

        # tabs
        self.encryption_tab = self.add("ENCRYPT")
        self.decryption_tab = self.add("DECRYPT")
        self.help_tab = self.add("HELP")

        # put widgets on tabs
        self.encrypt_frame = EncryptionFrame(self.encryption_tab, kwargs.get('entry_text', "Enter Your Encryption Key"))

        self.encrypt_frame.pack(expand=True, fill="both", )
        self.encrypt_frame.configure(fg_color='#7ED321')

        self.decrypt_frame = DecryptionFrame(self.decryption_tab, kwargs.get('entry_text', "Enter Your Decryption Key"))
        self.decrypt_frame.pack(expand=True, fill="both")
        self.decrypt_frame.configure(fg_color='#9c4624')

        self.help_frame = HelpFrame(self.help_tab, name=self.name)
        self.help_frame.configure(fg_color='#9013FE')

    @property
    def name(self):
        return self.__name
