from tkinter import *

root = Tk()

root.title("Grid Options")
root.geometry("400x400")

myLabel1 = Label ( root, text = "Section 1", fg= "black", bg= "red", font=("Helvtica",32 ))
myLabel1.grid(row = 0, column=0)


#columnspan de grid özelliklerinde biri 
#rowspan de satır karış 
myLabel2 = Label (root , text = "Section 2")
myLabel2.grid(row=1,column=0,sticky=W)

#sticky=W -> Sola yanaştırır
#sticky=E -> Sona yanaştırır 

myLabel3 = Label (root , text = "Section 3")
myLabel3.grid(row=2,column=0)

root.mainloop()
