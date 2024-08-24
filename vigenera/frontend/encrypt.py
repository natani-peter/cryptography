import customtkinter as ctk
from PIL import Image
import os

file_path = os.path.dirname(os.path.abspath(__file__))


class ImagePaths:
    copy_image_path = file_path + "/assets/blue copy.png"
    paste_image_path = file_path + "/assets/blue paste.png"


def create_encrypt_tab(self: ctk.CTk):
    # Create the Encrypt tab
    self.encrypt_tab = self.notebook.add("Encrypt")

    # Encrypt tab widgets
    ctk.CTkLabel(self.encrypt_tab, text="VIGENERA CIPHER", font=(32, 32), text_color="white").pack(pady=6)

    self.encrypt_input = ctk.CTkTextbox(self.encrypt_tab, height=150, fg_color='#111')
    self.encrypt_input.insert("1.0", "Enter Text To Encrypt")
    self.encrypt_input.pack(expand=True, fill="both", padx=10, pady=10)

    paste_image = ctk.CTkImage(Image.open(ImagePaths.paste_image_path), size=(30, 30))
    paste_image.background_color = "#111"
    paste_button = (ctk.CTkButton(self.encrypt_input, image=paste_image, text='', width=20, height=1, corner_radius=0,
                                  fg_color="#111", command=lambda: self.paste_text("e")))

    paste_button.place(relx=0.99, rely=0.01, anchor='ne', )

    self.encrypt_key = ctk.CTkEntry(self.encrypt_tab, fg_color="#111", placeholder_text='Enter your Key',
                                    placeholder_text_color="white", show="*", width=390)
    self.encrypt_key.pack(expand=False, pady=5,ipady=5)
    ctk.CTkButton(self.encrypt_tab, text="Encrypt", command=self.encrypt_text).pack(pady=4)

    self.encrypt_output = ctk.CTkTextbox(self.encrypt_tab, height=150, fg_color="#111")
    self.encrypt_output.insert("1.0", "ENCRYPTED TEXT")
    self.encrypt_output.configure(state="disabled")
    self.encrypt_output.pack(expand=True, fill="both", padx=10, pady=10)

    copy_image = ctk.CTkImage(light_image=Image.open(ImagePaths.copy_image_path),
                              dark_image=Image.open(ImagePaths.copy_image_path), size=(30, 30))

    ctk.CTkButton(self.encrypt_output, image=copy_image, text='', width=20, height=20, corner_radius=0,
                  fg_color="#111", command=lambda: self.copy_text("e")).place(relx=0.99, rely=0.01,
                                                                              anchor='ne', )
