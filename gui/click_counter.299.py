#Click Counter
# Demonstrates binding and event with an event handler

# pg 299

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.button_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.button = Button(self)
        self.button['text'] = 'Total Clicks: {}'.format(self.button_clicks)
        self.button['command'] = self.update_count
        self.button.grid()

    def update_count(self):
        self.button_clicks += 1
        self.button['text'] = 'Total Clicks: {}'.format(self.button_clicks)


#main
root = Tk()
root.title('Click Counter')
root.geometry('200x85')

app = Application(root)

root.mainloop()
