import customtkinter as ctk
from PIL import Image
import os

from encryptor.mainbackend.loggers import custom_logger

file_path = os.path.dirname(os.path.abspath(__file__))


class ImagePaths:
    copy_image_path = file_path + "/assets/copy_image.png"
    paste_image_path = file_path + "/assets/paste_image.png"


class ImageWidget(ctk.CTkImage):
    def __init__(self, image_type):
        __paste_light_image = Image.open(ImagePaths.paste_image_path)
        __copy_light_image = Image.open(ImagePaths.copy_image_path)
        __size = (25, 25)
        self.__image = __paste_light_image if image_type == "paste" else __copy_light_image
        super().__init__(light_image=self.__image, dark_image=self.__image, size=__size)


class LabelWidget(ctk.CTkLabel):
    def __init__(self, parent, text: str, font=(36, 36), text_color: str = 'white'):
        super().__init__(master=parent, text=text, font=font, text_color=text_color)
        self.pack(pady=6, padx=10)


class TextBoxWidget(ctk.CTkTextbox):
    def __init__(self, parent, color='#fff', text="Enter Text To Decrypt", text_box_type="encrypt"):
        super().__init__(master=parent, height=150, fg_color=color, text_color='#000')
        self.__type = 1 if text_box_type == "encrypt" else 0
        self.insert("1.0", text)
        self.bind('<Button-1>', self.clear_text)
        self.copy = ButtonWidget(self, color, self.copy_text, "copy")
        self.paste = ButtonWidget(self, color, self.paste_text, "paste")
        self.place_button()

    def place_button(self):
        if self.__type:
            self.paste.place(relx=0.98, rely=0.02, anchor='ne')
            return
        self.copy.place(relx=0.98, rely=0.02, anchor='ne')
        return

    def copy_text(self, *args, **kwargs):
        try:
            copy_text = self.get("1.0", "end")
            self.clipboard_clear()
            self.clipboard_append(copy_text)
            custom_logger.info("Copying Success")
        except Exception as e:
            custom_logger.error(f"Error Happened: {e}")

    def paste_text(self, *args, **kwargs):
        try:
            text = self.clipboard_get()
            self.delete("1.0", "end")
            self.insert("1.0", text)
            custom_logger.info("Pasting Success")
        except Exception as e:
            custom_logger.error(f"Error Happened: {e}")

    def clear_text(self, *args, **kwargs):
        self.delete("1.0", "end")
        self.unbind('<Button-1>')


class ButtonWidget(ctk.CTkButton):
    def __init__(self, parent, color, command_function=None, image_type=None):
        self.__command = command_function
        if image_type:
            image = ImageWidget("paste") if image_type == "paste" else ImageWidget("copy")

            super().__init__(master=parent, image=image, text='', width=20, height=1, corner_radius=5,
                             command=self.command, fg_color=color, hover_color=color)
            return

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        if callable(value):
            self.__command = value
            return
        raise TypeError("Command Must be a callable object")
