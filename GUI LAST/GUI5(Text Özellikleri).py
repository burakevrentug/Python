from tkinter import *

root = Tk()

root.title("Burak Hoş Geldin")
root.geometry("400x400")

myLabel1 = Label ( root, text = "Section 1", fg= "black", bg= "red", font=("Helvtica",32 ))
myLabel1.pack()
#fg = font rengi
#bg = arkaka plan 
#font = ("yazı tipi", yazi boyutu)
#height ile label'ın uzunluğu hazırlanır.
#width ile label'ın genişliği hazırlanır. 
myLabel2 = Label (root , text = "Section 2", relief ="raised", state = "normal")
myLabel2.pack(pady=50)
#pady = üsten boşluk miktarı 
#relief -> sunken çökük mod
#relief -> raised yüksek mod
#relief -> groove
#relief -> ridge

#state = "disabled" ile görünürlük azaltılır.
#state = "normal" ile normale döner
#Pack yerine gird (row = 0 , column=0) gibi grid değerleri de verilir. 


root.mainloop()
