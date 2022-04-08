from tkinter import *

root = Tk()
root.title("Using Radio Button")
root.geometry("400x400")

def writeSomething():
    myLabel = Label(root, text= v.get())
    myLabel.pack()


v= IntVar() 

radioButton1 = Radiobutton(root, text = "Makarna", variable= v, value = 1)
radioButton1.pack()

myButton = Button(root, text="Click Me", command = writeSomething)
myButton.pack()
root.mainloop()
