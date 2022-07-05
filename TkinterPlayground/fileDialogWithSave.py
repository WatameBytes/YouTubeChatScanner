from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(
        initialdir="C:\\Users\\Arisa\\PycharmProjects\\julyProject",
        defaultextension=".txt", filetypes=[
            ("Text File", "*.txt"),
            ("Any File", "*.*")
        ])
    if file is None:
        return # -> No more exceptions if we don't type anything!
    filetext = str(text.get(1.0, END))
    #filetext = input("Enter some text") --> Now we can select a file and type things in the console
    file.write(filetext)
    file.close()

window = Tk()


button = Button(
    text= "Save",
    command= saveFile,
)

text = Text(window)
text.pack()

button.pack()


window.mainloop()