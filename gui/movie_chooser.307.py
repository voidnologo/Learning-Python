#Movie Chooser
# demonstrates checkboxes

# pg 307

from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(
            self,
            text='Choose your favorite movie types',
        ).grid(row=0, column=0, sticky=W)

        Label(
            self,
            text='Select all that apply:',
        ).grid(row=1, column=0, sticky=W)

        self.likes_comedy = BooleanVar()
        Checkbutton(
            self,
            text='Comedy',
            variable=self.likes_comedy,
            command=self.update_text
        ).grid(row=2, column=0, sticky=W)

        self.likes_drama = BooleanVar()
        Checkbutton(
            self,
            text='Drama',
            variable=self.likes_drama,
            command=self.update_text
        ).grid(row=3, column=0, sticky=W)

        self.likes_romance = BooleanVar()
        Checkbutton(
            self,
            text='Romance',
            variable=self.likes_romance,
            command=self.update_text
        ).grid(row=4, column=0, sticky=W)

        self.likes_horror = BooleanVar()
        Checkbutton(
            self,
            text='Horror',
            variable=self.likes_horror,
            command=self.update_text
        ).grid(row=2, column=1, sticky=W)

        self.likes_anime = BooleanVar()
        Checkbutton(
            self,
            text='Anime',
            variable=self.likes_anime,
            command=self.update_text
        ).grid(row=3, column=1, sticky=W)

        self.likes_bollywood = BooleanVar()
        Checkbutton(
            self,
            text='Bollywood',
            variable=self.likes_bollywood,
            command=self.update_text
        ).grid(row=4, column=1, sticky=W)
