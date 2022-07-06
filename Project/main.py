from tkinter import *



def makeButton(text, command):
    return Button(window, text=text, command=command)

def submit():
    print("Hello World")

def download():
    print("Downloading Video")

def editor():
    print("Editing Video")

def data():
    print("Viewing Data")

def computeChat():
    print("Computing Chat")


window = Tk(className="youTube Chat Data")
window.geometry("750x750")

chatEntry = Entry(window)
chatEntry.pack()

getChat_button = makeButton("Get Chat", submit)
getChat_button.pack()

videoEntry = Entry(window)
videoEntry.pack()

downloadVideo_button = makeButton("Download Video", download)
downloadVideo_button.pack()


scale = Scale(
    window,
    from_= 0,
    to= 190,
    length=400,
    orient=HORIZONTAL,
    tickinterval=20,
    resolution=10,
)
scale.pack()


computeChat_button = makeButton("Compute Chat", computeChat)
computeChat_button.pack()


editor_button = makeButton("View Data", data)
editor_button.pack()


editor_button = makeButton("Trim Video", editor)
editor_button.pack()

window.mainloop()