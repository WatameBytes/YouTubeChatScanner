from tkinter import *

characters = ["Ganyu", "Barbara", "Yanfei"]

def order():
    if(x.get() == 0):
        print("You got Ganyu!")
    elif(x.get() == 1):
        print("You got Ganyu 2.0")
    elif(x.get() == 2):
        print("You got Yanfei!")
    else:
        print("...")

window = Tk()

x = IntVar()

ganyuImage = PhotoImage(file="Images/ganyu.png")
barbaraImage = PhotoImage(file="Images/ganyu.png")
yanfeiImage = PhotoImage(file="Images/yanfei.png")
characterImage = [ganyuImage, barbaraImage, yanfeiImage]

for index in range(len(characters)):
    radiobutton = Radiobutton(
        window,
        text=characters[index], # adds text to radio buttons
        variable= x, # Groups radio buttons together if they share the same variable
        value=index, # Assigns each radio button a different value
        padx= 25, # Adds padding to the x axis
        pady= 10,
        font= ("Impact", 50),
        image= characterImage[index], # Adds image to radio button
        compound="left", # adds image & text (left-side)
        indicatoron= 0, # Remove the button and make it a giant push button
        width= 375, # Sets width of radio button,
        command=order # Set command of radio button to function

    )
    radiobutton.pack(anchor=W)

window.mainloop()