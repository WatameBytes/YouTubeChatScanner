from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)
    #print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size()) # Readjust the list after performing an action

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(
    window,
    bg="#F7FFDE",
    font=("Constantia", 35),
    width= 12,
    selectmode=MULTIPLE, # Allows us to select multiple things
)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox =  Entry(window)
entryBox.pack()

submit_button = Button(window, text="submit", command=submit) # YOu can click on the list
submit_button.pack()


add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()