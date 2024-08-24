import customtkinter as ctk


def create_help_tab(self: ctk.CTk):
    # Create the Help tab
    self.help_tab = self.notebook.add("Help")

    # Help tab content
    help_text = (
        "\n\nThis tool allows you to encrypt and decrypt text \nUsing the Vigenera Cipher.\n\n\n"
        "1. **Encrypt Tab:**\n"
        "   - Enter the text you want to encrypt in the input area.\n"
        "   - Click the 'Encrypt' button to generate the encrypted text.\n"
        "   - The encrypted text will appear in the read-only output area.\n\n\n\n"
        "2. **Decrypt Tab:**\n"
        "   - Enter the text you want to decrypt in the input area.\n"
        "   - Click the 'Decrypt' button to retrieve the original text.\n"
        "   - The decrypted text will appear in the read-only output area.\n\n\n\n"
        "Note:\n"
        "   - The text entered should not contain none english letters \n\tand punctuation marks.\n\n"
        "   - For Any Bugs Reach Out to natanipeter@gmail.com"
    )
    help_label = ctk.CTkLabel(
        self.help_tab,
        text=help_text,
        wraplength=550,
        justify="left",
        anchor="nw",
        font=("Helvetica",14)
    )
    help_label.pack(fill="both", expand=True, padx=10, pady=10)
