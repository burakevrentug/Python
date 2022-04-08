from tkinter import *
#Eger Message Box eklemek istiyorsak ayrı bir import ihtiyacın var
from tkinter import messagebox
#Message box ekrana uyarı veriyor.

window = Tk()

window.title("Facebook Login")

window.geometry("500x250")
window.configure(background="yellow")
#İstersen burada yello değil ara renk istersen renk kodu da yazabilirsin. 
#Facebook için 2 tane label , 2 textbox 1 button ihtiyacımız olacak

label1= Label(window,text="username",bg="blue",fg="white",font="Times 24 bold")
label1.pack()
label2= Label(window,text="password",bg="blue",fg="white",font="Times 24 bold")
label2.pack()

#Bölgeleri x ve y koordinatı olarak veriyoruz.

label1.place(x=0,y=0)
label2.place(x=0,y=50)

nameEntry= Entry(window ,width=10)
nameEntry.place(x=150, y=0)

passWordEntry= Entry(window ,width=10)
passWordEntry.place(x=150, y=50)

def clicked():
    if ( nameEntry.get() =="burak" and passWordEntry.get()=="1234"):
        messagebox.showinfo("Home Page", "You entered")
    else:
       messagebox.showinfo("Home Page", "Wrong Password or name") 

btn = Button(window,text ="Sign In", command=clicked)

btn.pack()
btn.place(x=150, y=100)
