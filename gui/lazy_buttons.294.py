
#Lazy Buttons
# demonstrates a Buttons

#pg 294

from tkinter import *

root = Tk()
root.title('Labeler')
root.geometry('200x85')

app = Frame(root)

app.grid()

button1 = Button(app, text='I do nothing.')
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text='Another Button.')

button3 = Button(app)
button3.grid()
button3['text'] = 'Same Here!'

root.mainloop()
