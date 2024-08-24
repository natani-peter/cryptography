import customtkinter as ctk


def create_decrypt_tab(self: ctk.CTk):
    # Create the Decrypt tab
    self.decrypt_tab = self.notebook.add("Decrypt")

    # Encrypt tab widgets
    ctk.CTkLabel(self.decrypt_tab, text="VIGENERA CIPHER", font=(32, 32), text_color="white").pack(pady=6)
    self.decrypt_input = ctk.CTkTextbox(self.decrypt_tab, height=150)
    self.decrypt_input.insert("1.0", "Enter Text To Decrypt")
    self.decrypt_input.pack(expand=True, fill="both", padx=10, pady=10)

    self.decrypt_key = ctk.CTkEntry(self.decrypt_tab, fg_color="#111", placeholder_text='Enter your Key',
                                    placeholder_text_color="white", show="*")
    self.decrypt_key.pack(expand=False, pady=2)
    ctk.CTkButton(self.decrypt_tab, text="Decrypt", command=self.decrypt_text).pack(pady=4)

    self.decrypt_output = ctk.CTkTextbox(self.decrypt_tab, height=150)
    self.decrypt_output.insert("1.0", "PLAIN TEXT")
    self.decrypt_output.configure(state="disabled")
    self.decrypt_output.pack(expand=True, fill="both", padx=10, pady=10)
