#Labeler
# demonstrates a label

#pg 293

from tkinter import *

root = Tk()
root.title('Labeler')
root.geometry('200x50')

app = Frame(root)

app.grid()
label = Label(app, text='I am a label!')
label.grid()

root.mainloop()
