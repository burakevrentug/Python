from tkinter import *

root = Tk()

def myClick():
    myLabel1 = Label(root,text = "Look! You clicked a Button")
    myLabel1.pack()

myLabel = Label(root, text ="Hello I am learning How to use Button on Python")
myLabel.pack()
myButton = Button(root , text ="Click Me", command = myClick, fg="red", bg="#000000")
#Padx Genişlik pady= boy
myButton.pack()

root.mainloop()
