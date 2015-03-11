from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.categories = ['horror', 'anime', 'comedy', 'romance', 'balloons', 'rabbits', 'brains']
        self.intvars = []
        self.checkboxes = []
        i = 0

        for genre in self.categories:
            self.intvars.append(BooleanVar())

            self.checkboxes.append(Checkbutton(
                self,
                variable=genre,
                text=genre.capitalize(),
                command=self.update_text
            ).grid(row=i%3, column=i//3, sticky=W))
            i += 1

        print(self.checkboxes)
        print(self.intvars)


    def update_text(self):
        for i in self.checkboxes:
            if i[1].get()==0:
                #do what ever you want
                i[2].destroy()
        pass

#main
root = Tk()
root.title('Test')
app = Application(root)
root.mainloop()
