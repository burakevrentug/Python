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
    
def show():
    myFrame.grid(row=1,column=0, columnspan=1, padx=40, pady=40)

def hide():
    myFrame.grid_forget()


#Define a Menu


myMenu = Menu(root)

root.config(menu=myMenu)

#Creat Menu Items

fileMenu= Menu(myMenu)

myMenu.add_cascade(label = "File" , menu=fileMenu)
#Cascade basamaklandırmak demek 

fileMenu.add_command(label="New", command= fakeCommand)
fileMenu.add_separator()  #Seperator Koyuyoruz 
fileMenu.add_command(label ="Exit", command= root.quit)

#CREATE ANother SubMenu Edit 

editMenu = Menu(myMenu)

myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command= editMenuFunction)
editMenu.add_command(label="Copy", command= fakeCommand)
editMenu.add_command(label="Paste", command= fakeCommand)


showButton = Button (root, text="Show", command=show)
hideButton = Button (root, text="Hide", command=hide)

showButton.grid(row=0, column=0)
hideButton.grid(row=0, column=1)

myFrame = Frame (root,width= 200,height=200,bd=1, bg="blue",relief="sunken")
myFrame.grid(row=1,column=0, columnspan=1, padx=40, pady=40)

frameLabel = Label(myFrame, text="Hello World", font=("Helvetica",20))
frameLabel.pack(padx=20, pady=40)#padx ve pady kullanmadığımızda label frame e yapışır
root.mainloop()

