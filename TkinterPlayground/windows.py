from tkinter import *

window = Tk() # Instantiate an ionstance of a window
window.geometry("500x500")
window.title("YouTube Chat Scanner")

icon = PhotoImage(file="Images/ganyu.png") # https://pixeljoint.com/pixelart/141183.htm
window.iconphoto(True, icon)
window.config(background="#5CFCFF")

window.mainloop() # Place Window on computer screen, listen for events