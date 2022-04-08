#Destroy and pack_forget BOX
#Önemli olan label widget ını global yapmaktır. 

from tkinter import *

root = Tk()

myEntry = Entry(root, width=50,bg="blue",fg="white",borderwidth = 5)
myEntry.pack()
myEntry.insert(0,"Enter Your Name")


def myClick():
    global nameLabel
    hello = "hello " + myEntry.get()
    nameLabel = Label (root, text=hello)
    nameLabel.pack()


def hide():
    nameLabel.pack_forget()
    #namelabel.destroy()

def show():
    nameLabel.pack()

myButton = Button(root, text="Click your Name" , command= myClick)
myButton.pack()

hideButton = Button(root, text="Hide" , command= hide)
hideButton.pack()

showButton = Button(root, text="Show" , command= show)
showButton.pack()

root.mainloop()

