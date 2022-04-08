from tkinter import * 

root = Tk()

root.title("Using Menu Widgets")
root.geometry("400x400")

def fakeCommand():
    pass


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


root.mainloop()
