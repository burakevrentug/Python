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

#Define a Menu


myMenu = Menu(root)

root.config(menu=myMenu)

#Creat Menu Items

fileMenu= Menu(myMenu)

myMenu.add_cascade(label = "File" , menu=fileMenu)
#Cascade basamaklandırmak demek 

fileMenu.add_command(label="New", command= fakeCommand)
fileMenu.add_separator()  #Seperator Koyuyoruz 
fileMenu.add_command(label ="Exit", command= root.destroy)

#CREATE ANother SubMenu Edit 

editMenu = Menu(myMenu)

myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command= editMenuFunction)
editMenu.add_command(label="Copy", command= fakeCommand)
editMenu.add_command(label="Paste", command= fakeCommand)



root.mainloop()
