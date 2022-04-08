#Destroy tamamen veriyi ortadan kaldırır. 


from tkinter import *

root = Tk()

myEntry = Entry(root, width=50,bg="blue",fg="white",borderwidth = 5)
myEntry.pack()
myEntry.insert(0,"Enter Your Name")

#Scope İçinde bulunan değişkenler dışarıdan görünmez Bunlar localdir

def myClick():
    global nameLabel
    hello = "hello " + myEntry.get()
    nameLabel = Label (root, text=hello)
    nameLabel.pack()
    
#Hide Function
def hide():
    nameLabel.grid_forget()
    #ıf we want we use .destoy()

def show():
    nameLabel.grid(row=, column=)
    
def clear():
    nameLabel.destroy()



myButton = Button(root, text="Click your Name" , command= myClick)
myButton.pack()

myButton2 = Button(root, text="Hide" , command= hide)
myButton2.pack()

myButton3 = Button(root, text="Show" , command= show)
myButton3.pack()

myButton4 = Button(root, text="Clear" , command= clear)
myButton4.pack()



root.mainloop()

