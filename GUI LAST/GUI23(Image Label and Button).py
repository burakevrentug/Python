from tkinter import *
from PIL import Image, ImageTk
#Image Kullanmak için yukarıdaki kütüphaneyi Eklemek Gerekir. 

root= Tk()
root.geometry("400x400")
root.title("Using Image Window")
def openNew():
    new = Toplevel()
    new.title("Hello New Window")
    new.geometry("400x400")
    
    newLabel = Label(new,text="Hello")
    newLabel.pack()
    
    img_Label = ImageTk.PhotoImage(Image.open("/Users/burakevrentug/Desktop/sun_PNG13449.png"))
    imgLabel = Label(new, image=img_Label)
    imgLabel.pack(pady=5)
    new.mainloop()

img_Label = ImageTk.PhotoImage(Image.open("/Users/burakevrentug/Desktop/sun_PNG13449.png"))
   
newButton = Button(root,text="Click Me", image= img_Label,command=openNew)

newButton.pack()

#Image özelliğini button ve label da yapabiliriz. 

root.mainloop()
