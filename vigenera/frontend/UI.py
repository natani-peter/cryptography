import customtkinter as ctk
from tkinter import messagebox
from vigenera.backend.VigeneraBackend import VigeneraBackend
from vigenera.frontend import encrypt, decrypt, help


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#202020")

        ctk.set_appearance_mode("system")

        self.__backend = VigeneraBackend()
        width, height = 430, 650
        x, y = (self.winfo_screenwidth() - width) // 2, (self.winfo_screenheight() - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.title("VIGENERA CIPHER")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill='both')

        self.notebook = ctk.CTkTabview(self.main_frame, anchor='center')
        self.notebook.pack(fill="both", expand=True, padx=5, pady=5)

        # add tabs

        encrypt.create_encrypt_tab(self)
        decrypt.create_decrypt_tab(self)
        help.create_help_tab(self)

        self.encrypt_input.bind('<Button-1>', self.clear_text)
        self.decrypt_input.bind('<Button-1>', self.clear_text_cipher)

    def encrypt_text(self):
        input_text = self.encrypt_input.get("1.0", "end").replace("\n", " ")
        print((input_text))
        user_key = self.encrypt_key.get()
        if input_text:
            if user_key:
                self.encrypt_output.configure(state="normal")
                self.encrypt_output.delete("1.0", "end")
                self.__backend.text = input_text
                self.__backend.key = user_key
                result = self.__backend.encrypt()[0]
                self.encrypt_output.insert("1.0", result)
                self.encrypt_output.configure(state='disabled')
            else:
                messagebox.showerror("ERROR", "Please enter Key")
        else:
            messagebox.showerror("ERROR", "Please enter text to encrypt")

    def decrypt_text(self):
        input_text = self.decrypt_input.get("1.0", "end").replace("\n", " ")
        user_key = self.decrypt_key.get()
        if input_text:
            if user_key:
                self.decrypt_output.configure(state="normal")
                self.decrypt_output.delete("1.0", "end")
                self.__backend.text = input_text
                self.__backend.key = user_key
                result = self.__backend.decrypt()[0]
                self.decrypt_output.insert("1.0", result)
                self.decrypt_output.configure(state='disabled')
            else:
                messagebox.showerror("ERROR", "Please enter Key")
        else:
            messagebox.showerror("ERROR", "Please enter text to encrypt")

    def clear_text(self, *args, **kwargs):
        self.encrypt_input.delete("1.0", "end")
        self.encrypt_input.unbind("<Button-1>")

    def clear_text_cipher(self, *args, **kwargs):
        self.decrypt_input.delete("1.0", "end")
        self.decrypt_input.unbind("<Button-1>")

    def copy_text(self, tab='d', *args, **kwargs):
        try:
            copied_text = self.encrypt_output.get("1.0", "end").replace("\n", " ") if (
                    tab[0] == 'e') else self.decrypt_output.get("1.0", "end").replace("\n", " ")
            self.clipboard_clear()
            self.clipboard_append(copied_text)
            self.__backend.logger.info("Copying Success")
        except Exception as e:
            self.__backend.logger.error(f"Error Happened: {e}")

    def paste_text(self, tab="d", *args, **kwargs):
        try:
            wanted_text_box = self.encrypt_input if (tab[0] == 'e') else self.decrypt_input
            text = self.clipboard_get()
            wanted_text_box.delete("1.0", "end")
            wanted_text_box.insert("1.0", text)
            self.__backend.logger.info("Pasting Success")
        except Exception as e:
            self.__backend.logger.error(f"Error Happened: {e}")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
