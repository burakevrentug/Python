
from tkinter import *

root = Tk()
root.title("Entry Widget")
root.iconbitmap('/Users/burakevrentug/Desktop/GUI LAST/GUI7/a.ico') 
def myClick():
    hello = "hello " + myEntry.get()
    nameLabel = Label (root, text=hello)
    nameLabel.pack()
    
myEntry = Entry(root, width=50,bg="blue",fg="white",borderwidth = 5)
myEntry.pack()
myEntry.insert(0,"Enter Your Name")


myButton = Button(root, text="Click your Name" , command= myClick)
myButton.pack()

root.mainloop()

