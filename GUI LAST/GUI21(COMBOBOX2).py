from tkinter import * 
from tkinter import ttk
#Combobox kullanmak için ttk kullanılmalı

root = Tk()
root.title("Using ComboBox")
root.geometry("400x400")

def learn():
    if(my_combo.get()=="Monday"):
        myLabel= Label(root,text="You clicked Monday")
        myLabel.pack()
    elif(my_combo.get()=="Tuesday"):
        myLabel= Label(root,text="You clicked Tuesday")
        myLabel.pack()
    elif(my_combo.get()=="Wednesday"):
        myLabel= Label(root,text="You clicked Wednesday")
        myLabel.pack()
    
    

options = [
    "Monday",
    "Tuesday",
    "Wednesday"
    ]

my_combo = ttk.Combobox(root,value=options)
my_combo.current(0) #İlk Seçeneği Belirler 
my_combo.pack(pady=10)

myButton = Button(root, text="Learn", command=learn)
myButton.pack()

root.mainloop()