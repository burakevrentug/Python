from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())
    myLabel = Label(master, text=res).grid(row=3, sticky=W)
 
master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=0, column=2)
 
 
mainloop()
