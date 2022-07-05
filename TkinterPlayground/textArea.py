from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(
    window,
    bg="light yellow",
    font=("Ink Free", 25), # Font size changes the size of our text area is MASSIVE!!!!
    height=8,
    width=20,
    padx = 20,
    pady= 20,
    fg= "purple",
)
text.pack()
button = Button(window, text = "submit", command= submit)
button.pack()

window.mainloop()