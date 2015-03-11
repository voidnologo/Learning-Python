#Lazy Buttons 2
# Demonstrates using a class with tinker

# pg 297

from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text='I do nothing.')
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text='Me too.')

        self.button3 = Button(self)
        self.button3.grid()
        self.button3['text'] = 'Same Here.'


#main
root = Tk()
root.title('Lazy Buttons 2')
root.geometry('200x85')

app = Application(root)
root.mainloop()
