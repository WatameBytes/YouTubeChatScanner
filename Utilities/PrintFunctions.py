# List the choices the user can type


def print_list_of_choices():
    print(
        "1: Get Chat Data\n"
        "2: Download YouTube Video\n"
        "3: Compute Chat Data\n"
        "4: Exit\n"
        "5: Current Threads\n"
        "6: List Contents\n"
        "7: Compute Data\n"
        "8: Open File Explorer"
    )


# Print out what the program is currently working on
def print_current_queue(choiceOneBuffer, choiceTwoBuffer, choiceThreeBuffer):
    print("===================")
    print("Getting Chat Data: {}".format(choiceOneBuffer))
    print("Downloading Video: {}".format(choiceTwoBuffer))
    print("Computing Chat Data: {}".format(choiceThreeBuffer))
    print("==================")

# If the user types a value not assigned -> Inform the user their choices
def print_improper_choice():
    print("Improper Choice! Please type 0 to view your options!")