import customtkinter as ctk
from vigenera.frontend.encrypt import ImagePaths
from PIL import Image


def create_decrypt_tab(self: ctk.CTk):
    # Create the Decrypt tab
    self.decrypt_tab = self.notebook.add("Decrypt")

    # Encrypt tab widgets
    ctk.CTkLabel(self.decrypt_tab, text="VIGENERA CIPHER", font=(32, 32), text_color="white").pack(pady=6)

    self.decrypt_input = ctk.CTkTextbox(self.decrypt_tab, height=150)
    self.decrypt_input.insert("1.0", "Enter Text To Decrypt")
    self.decrypt_input.pack(expand=True, fill="both", padx=10, pady=10)

    paste_image = ctk.CTkImage(light_image=Image.open(ImagePaths.paste_image_path),
                               dark_image=Image.open(ImagePaths.paste_image_path), size=(30, 30))

    paste_button = (ctk.CTkButton(self.decrypt_input, image=paste_image, text='', width=20, height=1, corner_radius=0,
                                  fg_color="#111", command=self.paste_text))

    paste_button.place(relx=0.99, rely=0.01, anchor='ne', )

    self.decrypt_key = ctk.CTkEntry(self.decrypt_tab, fg_color="#111", placeholder_text='Enter your Key',
                                    placeholder_text_color="white", show="*",width=390)
    self.decrypt_key.pack(expand=False, pady=5,ipady=5)
    ctk.CTkButton(self.decrypt_tab, text="Decrypt", command=self.decrypt_text).pack(pady=4)

    self.decrypt_output = ctk.CTkTextbox(self.decrypt_tab, height=150)
    self.decrypt_output.insert("1.0", "PLAIN TEXT")
    self.decrypt_output.configure(state="disabled")
    self.decrypt_output.pack(expand=True, fill="both", padx=10, pady=10)

    copy_image = ctk.CTkImage(light_image=Image.open(ImagePaths.copy_image_path),
                              dark_image=Image.open(ImagePaths.copy_image_path), size=(30, 30))

    ctk.CTkButton(self.decrypt_output, image=copy_image, text='', width=20, height=20, corner_radius=0,
                  fg_color="#111", command=self.copy_text).place(relx=0.99, rely=0.01,
                                                                 anchor='ne', )
