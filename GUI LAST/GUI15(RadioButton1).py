from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Using Radio Button")
global myLabel
def runRadioButton():
    write = "You clicked " + str(v.get())
    myLabel = Label(root, text =write)
    myLabel.pack()

#Değerlerimiz int mi olacak yok sa String mi? Buna karar veriyoruz. 

v = IntVar()
radioButton1 = Radiobutton(root, text="1. Option", variable=v,value=1)
radioButton2 = Radiobutton(root, text="2. Option", variable=v,value=2)

radioButton1.pack()
radioButton2.pack()

clickButton = Button(root, text="Click Me Baby", command=runRadioButton)
clickButton.pack(pady=20)

root.mainloop()
