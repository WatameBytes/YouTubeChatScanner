from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You have pasted some text")

window = Tk()

ganyuImage = PhotoImage(file="Images/ganyu.png")

menubar = Menu(window)

window.config(menu = menubar)

fileMenu = Menu(menubar, tearoff = 0, font=("MV Boli", 15))
menubar.add_cascade(label = "File", menu = fileMenu) # THink of this as our header

fileMenu.add_command(label = "Open", command=openFile, image=ganyuImage, compound="left") # Clickable Option
fileMenu.add_command(label = "Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label = "Cut", command=cut) # Cliclable Option
editMenu.add_command(label = "Copy", command=copy)
editMenu.add_separator()
editMenu.add_command(label = "Paste", command=paste)

window.mainloop()