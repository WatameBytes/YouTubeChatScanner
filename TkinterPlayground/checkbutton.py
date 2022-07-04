from tkinter import *

def display():
    if(x.get() == 1): # if(x.get())  --> Return true or false :: if(x.get() == "YES"
        print("You agree")
    else:
        print("You didn't agree :(")


window = Tk()

x = IntVar() # If we use True/False we should use BooleanVar :: StringVar if we use "YES"/"NO"

ganyu_photo = PhotoImage(file="ganyu.png")

check_button = Checkbutton(
    window,
    text= "I agree to something",
    variable= x,
    onvalue= 1, # True
    offvalue= 0, # False
    command= display,
    font=("Arial", 20),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00", # Remove the flash when we click on the button OR "YES"
    activebackground="black", # Remove the flash when we click on the button OR "NO"
    padx= 25,
    pady= 10,
    image= ganyu_photo,
    compound="left",

)


check_button.pack()

window.mainloop()