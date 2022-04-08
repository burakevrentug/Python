
from tkinter import * 

root = Tk()

root.title("Using CheckButton")
root.geometry("400x400")
sonHesap=0



def hesapla():
     

    if(v1.get()=="makarna"):
        
        priceLabel = Label(root, text="15 TL").pack()
        
    elif(v2.get()=="dürüm"):
        priceLabel = Label(root, text="10 TL").pack()
        


v1 = StringVar()
v2 = StringVar()

check1 = Checkbutton(root, text= "Makarna", variable = v1, onvalue="makarna",offvalue="Makarna Seçilmedi" )
check1.deselect()
check1.pack()
    

check2 = Checkbutton(root, text= "Dürüm", variable = v2, onvalue="dürüm",offvalue="Dürüm Seçilmedi" )
check2.deselect()
check2.pack()

myButton = Button(root, text = "Hesapla",command=hesapla).pack()

root.mainloop()