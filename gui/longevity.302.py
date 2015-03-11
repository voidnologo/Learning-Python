# Longevity
# Demonstrates text and entry widget, and the Grid layout manager

# pg 302

from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = Label(self, text='Enter Password for the secret.')
        self.instruction_label.grid(row=0, column=0, columnspan=2, sticky=W)

        self.password_label = Label(self, text='Password: ')
        self.password_label.grid(row=1, column=0, sticky=W)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=1, column=1, sticky=W)

        self.submit_button = Button(self, text='Submit', command=self.reveal)
        self.submit_button.grid(row=2, column=0, sticky=W)

        self.secret_text = Text(self, width=35, height=3, wrap=WORD)
        self.secret_text.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        contents = self.password_entry.get()
        if contents == 'secret':
            message = "Here's the secret: live a long time."
        else:
            message = 'Wrong Password.'

        self.secret_text.delete(0.0, END)
        self.secret_text.insert(0.0, message)

#main
root = Tk()
root.title('Longevity')
root.geometry('300x150')

app = Application(root)

root.mainloop()

