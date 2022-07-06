import _Gui


def main():
    _Gui.display_The_Program() # Display the GUI for us [Pretty model]
    _Gui.gui() # The logic that reads and parse input in the gui [Logic]

if __name__ == '__main__':
    main()

# Logic for the program [Documentation]
# Main.py --> _Gui.py
# Main.py: Main method that calls _Gui.py
# _Gui.py --> _CollectChat
# _Gui.py collects data that user inputs and sends it to _CollectChat
# _CollectChat.py --> _GetDataAndStars [Made it a class to send multiple things]
# _CollectChat.py counts the time when a chat message was sent and sends it to _GetDataAndStars to make it readable
# [Warning] !! _GetDataAndStars.py is a mess !!
# _GetDataAndStars.py breaks the data into stars/numbers and places gives us data depending on the domain we hardcoded