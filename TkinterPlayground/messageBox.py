from tkinter import *
from tkinter import messagebox # import the messageBox library

def click():
    #messagebox.showinfo(title="This is an info message box", message="You are a person")
    #messagebox.showwarning(title="This is an info message box", message="You have a VIRUS")
    #messagebox.showerror(title="This is an info message box", message="Something went wrong")
    if(messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing? :)")):
        print("You did a thing")
    else:
        print("You canceled a thing :(")
    # if(messagebox.askretrycancel(title="Ask Retry Cancel", message= "Do you want to retry the thing?")):
    #     print("You retried a thing!")
    # else:
    #     print("You canceled a thing! :(")
    # answer = messagebox.askquestion(title="Ask question", message="Do you like pie?")
    # if(answer == "yes"):
    #     print("I like pie too!")
    # else:
    #     print("Why do you not like pie?")


window = Tk()

button = Button(
    window,
    command=click,
    text="click me"
)

button.pack()



window.mainloop()
