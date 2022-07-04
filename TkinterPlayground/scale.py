from tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + " degress C")

window = Tk()

ganyuImage = PhotoImage(file="Images/ganyu.png")
ganyuLabel = Label(image=ganyuImage)
ganyuLabel.pack()


scale = Scale(
    window,
    from_=100,
    to= 0,
    length=600,
    orient=VERTICAL, # Orientation of the scale
    font= ("Consolas", 20),
    tickinterval= 10, # Adds numerica indicators for value
    #showvalue= 0, # hide current value
    resolution= 5, # increment of slider
    troughcolor= "#69EAFE",
    fg = "#FF1C00",
    bg = "#111111",

)

scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"] ) # Always center it

scale.pack()

#yanfeiImage = PhotoImage(file="Images/yanfei.png")
yanfeiLabel = Label(image=ganyuImage)
yanfeiLabel.pack()

button = Button(
    window,
    text="Submit",
    command=submit
)
button.pack()

window.mainloop()