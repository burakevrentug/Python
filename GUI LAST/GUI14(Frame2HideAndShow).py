#Frames 

from tkinter import * 

root = Tk()

root.title("Using Menu Widgets")
root.geometry("400x400")

def fakeCommand():
    myLabel= Label(text="You clicked Some Menu Item")
    myLabel.pack()

def editMenuFunction():
    editRoot = Tk()
    labelEdit= Label(editRoot, text="Welcome to Edit Menu")
    labelEdit.pack()
    

def new():
    forgetFrame()
    fileFrame.grid(row=1,column=0, columnspan=1, padx=40, pady=40)

def cut():
    forgetFrame()
    editFrame.grid(row=1,column=0, columnspan=1, padx=40, pady=40)

def forgetFrame():
    fileFrame.grid_forget()
    editFrame.grid_forget()

#Define a Menu


myMenu = Menu(root)

root.config(menu=myMenu)

#Creat Menu Items

fileMenu= Menu(myMenu)

myMenu.add_cascade(label = "File" , menu=fileMenu)
#Cascade basamaklandırmak demek 

fileMenu.add_command(label="New", command= new)
fileMenu.add_separator()  #Seperator Koyuyoruz 
fileMenu.add_command(label ="Exit", command= root.quit)

#CREATE ANother SubMenu Edit 

editMenu = Menu(myMenu)

myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command= cut)
editMenu.add_command(label="Copy", command= fakeCommand)
editMenu.add_command(label="Paste", command= fakeCommand)


fileFrame = Frame (root,width= 200,height=200,bd=1, bg="blue",relief="sunken")

fileFrameLabel = Label(fileFrame, text="New Frame", font=("Helvetica",20))
fileFrameLabel.pack(padx=40, pady=40)#padx ve pady kullanmadığımızda label frame e yapışır

editFrame = Frame (root,width= 200,height=200,bd=1, bg="blue",relief="sunken")

editFrameLabel = Label(editFrame,text="Cut Frame", font=("Helvetica",20))
editFrameLabel.pack(padx=40, pady=40)

root.mainloop()

