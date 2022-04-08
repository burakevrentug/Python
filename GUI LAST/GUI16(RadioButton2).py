from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Using Radio Button")
global myLabel 
def runRadioButton():
  
    if (v.get() =="one"):
        myLabel= Label(root, text="You choosed 1. Option ").pack()
    elif (v.get() =="two"):
        myLabel= Label(root, text="You choosed 2. Option ").pack()  
#Bu uygulamada hem if hem de String value örneği yapıyoruz. 
v = StringVar()
v.set("one")
# İlk Seçilenin otomatik olarak ne olmasını istiyorsak set kullanıyoruz. 
radioButton1 = Radiobutton(root, text="1. Option", variable=v,value="one")
radioButton2 = Radiobutton(root, text="2. Option", variable=v,value="two")

radioButton1.pack()
radioButton2.pack()

clickButton = Button(root, text="Click Me Baby", command=runRadioButton)
clickButton.pack(pady=20)
root.mainloop()
