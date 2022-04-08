from tkinter import *
import random
from tkinter import messagebox

hakSayisi = 7
oyun = Tk()
oyun.title("Beni Tahmin Et")
oyun.geometry("400x400")

bilgisayar = random.randint(0, 100)


def kontrol():
    kullanici = int(numberEntry.get())
    hakSayisi = int(labelExample['text'])
    if hakSayisi > 0:
        if (kullanici < bilgisayar):
            hakSayisi -= 1
            messagebox.showerror("Üzgünüm", "Daha büyük sayı girerek tekrar dene")
        elif (kullanici > bilgisayar):
            hakSayisi -= 1
            messagebox.showerror("Üzgünüm", "Daha küçük sayı girerek tekrar dene")

        elif (kullanici == bilgisayar):

            messagebox.showerror("Tebrikler", "Tebrikler")

    else:
        messagebox.showerror("Üzgünüm", "Hakkınız Bitti")
    labelExample.config(text=str(hakSayisi))
    #labelExample["text"] = str(hakSayisi)


numberEntry = Entry(oyun)
kontrolButton = Button(oyun, text="Kontrol Et", command=kontrol)
labelExample = Label(oyun, text="7")

numberEntry.grid(row=0, column=0)
kontrolButton.grid(row=1, column=0)
labelExample.grid(row=2, column=0)

oyun.mainloop()

