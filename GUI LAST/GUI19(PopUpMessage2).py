from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("400x400")

root.title ("Using Pop Up Message Box ")


#Popup Box
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup1():
    messagebox.showinfo("Popup Title", "This code is writen by Burak Evrentuğ")
   
def popup2():
    messagebox.showwarning("Popup Title", "This code is writen by Burak Evrentuğ")

    
def popup3():
    messagebox.showerror("Popup Title", "This code is writen by Burak Evrentuğ")

    
def popup4():
    response = messagebox.askquestion("Popup Title", "This code is writen by Burak Evrentuğ")
    myLabel = Label(root,text=response).pack()
    #Yes ve No Döner
    '''
    if (response =="yes"):
    '''
    
def popup5():
    response = messagebox.askokcancel("Popup Title", "This code is writen by Burak Evrentuğ")
   
    myLabel = Label(root,text=response).pack()
      '''
    if (response ==1): 
    '''
    #1 ve 0 döner

def popup6():
    response =  messagebox.askyesno("Popup Title", "This code is writen by Burak Evrentuğ")
    myLabel = Label(root,text=response).pack()
    #1 ve 0 döner


popUpButton1 = Button(root,text="Show Info", command=popup1)
popUpButton1.pack()

popUpButton2 = Button(root,text="Show Warning", command=popup2)
popUpButton2.pack()

popUpButton3 = Button(root,text="Show Error", command=popup3)
popUpButton3.pack()

popUpButton4 = Button(root,text="Ask Question", command=popup4)
popUpButton4.pack()

popUpButton5 = Button(root,text="Ask OK/Cancel", command=popup5)
popUpButton5.pack()

popUpButton5 = Button(root,text="Ask Yes/No", command=popup6)
popUpButton5.pack()

root.mainloop()