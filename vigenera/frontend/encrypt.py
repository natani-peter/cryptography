import customtkinter as ctk


def create_encrypt_tab(self: ctk.CTk):
    # Create the Encrypt tab
    self.encrypt_tab = self.notebook.add("Encrypt")

    # Encrypt tab widgets
    ctk.CTkLabel(self.encrypt_tab, text="VIGENERA CIPHER", font=(32, 32), text_color="white").pack(pady=6)
    self.encrypt_input = ctk.CTkTextbox(self.encrypt_tab, height=150)
    self.encrypt_input.insert("1.0", "Enter Text To Encrypt")
    self.encrypt_input.pack(expand=True, fill="both", padx=10, pady=10)

    self.encrypt_key = ctk.CTkEntry(self.encrypt_tab, fg_color="#111", placeholder_text='Enter your Key',
                                    placeholder_text_color="white",)
    self.encrypt_key.pack(expand=False, pady=2)
    ctk.CTkButton(self.encrypt_tab, text="Encrypt", command=self.encrypt_text).pack(pady=4)

    self.encrypt_output = ctk.CTkTextbox(self.encrypt_tab, height=150)
    self.encrypt_output.insert("1.0", "ENCRYPTED TEXT")
    self.encrypt_output.configure(state="disabled")
    self.encrypt_output.pack(expand=True, fill="both", padx=10, pady=10)
