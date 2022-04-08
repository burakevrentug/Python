from tkinter import *


root= Tk()
root.geometry("400x400")
root.title("Using New Window")


def openNew():
    root.destroy()
    new = Tk()
    new.title("Hello New Window")
    new.geometry("200x200")
    
    newLabel = Label(new,text="Hello")
    newLabel.pack()
    destroyButton = Button(new,text="Exit",command=new.destroy)
    destroyButton.pack()
    new.mainloop()


newButton = Button(root,text="Click Me", command=openNew)
newButton.pack()




root.mainloop()
