import customtkinter as ctk

from encryptor.mainfrontend.GeneralUI import GeneralUI
from vigenera.backend.VigeneraBackend import VigeneraBackend


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#333")
        ctk.set_appearance_mode("system")
        self.__frontend = GeneralUI
        self.first = 0
        self.number_of_tabs = 2
        self.c_first, self.v_first = False, False
        self.__backend = VigeneraBackend()
        __width, __height, __left, __top = self.__set_position()
        self.__first_tab, self.__second_tab, self.__last_tab = "AFFINE CIPHER", "CAESAR CIPHER", "VIGENERA CIPHER"
        self.name = self.__first_tab
        # self.bind('<Configure>', self.print)

        self.title("UNIVERSAL ENCRYPTOR")
        self.geometry(f"{__width}x{__height}+{int(__left)}+{int(__top)}")
        self.resizable(False, False)

        self.main_notebook = ctk.CTkTabview(self, command=self.__set_other_tabs)
        self.main_notebook.pack(expand=True, fill='both')

        self.affine_tab = self.main_notebook.add(self.__first_tab)
        self.affine = self.__frontend(self.affine_tab)
        self.affine.pack(expand=True, fill="both", padx=10)

        self.caesar_tab = self.main_notebook.add(self.__second_tab)

        self.vigenera_tab = self.main_notebook.add(self.__last_tab)

    def print(self, event):
        print(event)

    def __set_other_tabs(self):
        self.name = self.main_notebook.get()
        first_lower_letter = self.name.lower()[0]
        if first_lower_letter == "c":
            self.__set_second_tab()
        elif first_lower_letter == "v":
            self.__set_last_tab()

    def __set_second_tab(self):
        if self.first < self.number_of_tabs:

            if not self.c_first:
                self.first += 1
                self.c_first = True

            self.caesar = self.__frontend(self.caesar_tab)
            self.caesar.pack(expand=True, fill="both", padx=10)

    def __set_last_tab(self):
        if self.first < self.number_of_tabs:

            if not self.v_first:
                self.first += 1
                self.v_first = True

            self.vigenera = self.__frontend(self.vigenera_tab)
            self.vigenera.pack(expand=True, fill="both", padx=10)

    def __set_position(self):
        width, height, x, y = 426, 716, self.winfo_screenwidth(), self.winfo_screenheight()
        return 426, 716, (x - width) / 2, (y - height) / 2

    def run(self):
        self.mainloop()
