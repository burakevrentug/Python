#INPUT (ENTRY) BOX


from tkinter import *

root = Tk()

myEntry = Entry(root, width=30,bg="blue",fg="white",borderwidth = 5)
myEntry.pack()
myEntry.insert(0,"Enter Your Name")


def myClick():
    hello = "hello " + myEntry.get()
    nameLabel = Label (root, text=hello)
    nameLabel.pack()



myButton = Button(root, text="Click your Name" , command= myClick)
myButton.pack()

root.mainloop()

