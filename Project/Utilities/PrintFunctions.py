# List the choices the user can type
def print_list_of_choices():
    print("1: Get Chat Data\n2: Download YouTube Video\n3: Compute Chat Data\n4: Exit\n5: Current Threads")


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