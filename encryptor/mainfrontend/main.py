import customtkinter as ctk

from encryptor.mainfrontend.GeneralUI import GeneralUI
from vigenera.backend.VigeneraBackend import VigeneraBackend


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#000")
        ctk.set_appearance_mode("system")

        # INITIAL APP CONFIGURATION
        self.__frontend, self.__backend = GeneralUI, VigeneraBackend()
        self.caesar_first_loading, self.vigenera_first_loading = False, False
        self.first, self.number_of_tabs = 0, 2
        __width, __height, __left, __top = self.__set_position()
        self.__first_tab, self.__second_tab, self.__last_tab, = "AFFINE CIPHER", "CAESAR CIPHER", "VIGENERA CIPHER"
        self.name = self.__first_tab

        # APP SETTINGS
        self.title("UNIVERSAL ENCRYPTOR")
        self.geometry(f"{__width}x{__height}+{int(__left)}+{int(__top)}")
        self.resizable(False, False)

        # MAIN OUTER TAB
        self.main_notebook = ctk.CTkTabview(self,
                                            command=self.__set_other_tabs,
                                            fg_color='#50e3c2',
                                            text_color="#ffffff",
                                            bg_color="black",
                                            corner_radius=8
                                            )
        self.main_notebook.pack(expand=True, fill='both', padx=10,pady=10)

        #
        self.affine_tab = self.main_notebook.add(self.__first_tab)
        self.affine = self.__frontend(self.affine_tab)
        self.affine_tab.configure(fg_color='#50e3c2')
        self.affine.pack(expand=True, fill="both", padx=10, ipadx=5, ipady=5)

        self.caesar_tab = self.main_notebook.add(self.__second_tab)

        self.vigenera_tab = self.main_notebook.add(self.__last_tab)

    def __set_other_tabs(self):
        self.name = self.main_notebook.get()
        first_lower_letter = self.name.lower()[0]
        if first_lower_letter == "c":
            self.main_notebook.configure(fg_color='#f5a623')
            self.__set_second_tab()
        elif first_lower_letter == "v":
            self.main_notebook.configure(fg_color='#4a90e2')
            self.__set_last_tab()
        else:
            self.main_notebook.configure(fg_color='#50e3c2')

    def __set_second_tab(self):
        if self.first < self.number_of_tabs:
            self.caesar = self.__frontend(self.caesar_tab)
            if not self.caesar_first_loading:
                self.first += 1
                self.caesar_first_loading = True
                self.caesar.pack(expand=True, fill="both", padx=5, ipadx=5, ipady=5)

    def __set_last_tab(self):
        if self.first < self.number_of_tabs:
            self.vigenera = self.__frontend(self.vigenera_tab)
            if not self.vigenera_first_loading:
                self.first += 1
                self.vigenera_first_loading = True
                self.vigenera.pack(expand=True, fill="both", padx=5, ipadx=5, ipady=5)

    def __set_position(self):
        width, height, x, y = 440, 716, self.winfo_screenwidth(), self.winfo_screenheight()
        return 440, 716, (x - width) / 2, (y - height) / 2

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    window = MainWindow()
    window.run()
