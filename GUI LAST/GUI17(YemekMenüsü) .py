
from tkinter import * 

root = Tk()

root.title("Using CheckButton")
root.geometry("400x400")
sonHesap=0
priceLabel = Label(root, text="0")
priceLabel.grid(row=0, column=0)

def hesapla():    

    if(v1.get()=="makarna"):
        sonHesap = int(priceLabel['text'])
        sonHesap =sonHesap + 10
        priceLabel["text"]=str(sonHesap)
        
    elif(v2.get()=="dürüm"):
        sonHesap = int(priceLabel['text'])
        sonHesap =sonHesap + 5
        priceLabel["text"]=str(sonHesap)

    elif(v1.get()=="makarna" and v2.get()=="dürüm"):
        sonHesap = int(priceLabel['text'])
        sonHesap =sonHesap + 15
        priceLabel["text"]=str(sonHesap)

        
    check1.deselect()
    check2.deselect()

v1 = StringVar()
v2 = StringVar()

check1 = Checkbutton(root, text= "Makarna", variable = v1, onvalue="makarna",offvalue="Makarna Seçilmedi" )
check1.deselect()
check1.grid(row=1,column=1)
    
check2 = Checkbutton(root, text= "Dürüm", variable = v2, onvalue="dürüm",offvalue="Dürüm Seçilmedi" )
check2.deselect()
check2.grid(row=2,column=1)

myButton = Button(root, text = "Hesapla",command=hesapla)
myButton.grid(row=3,column=1)
root.mainloop()
