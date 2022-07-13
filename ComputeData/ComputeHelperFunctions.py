import os

from Utilities import HelperFunctions
from Utilities.HelperFunctions import MainDirectory, getContents

def files_displayed_to_user_and_user_selects_file(file_directory, extension):
    list_of_contents = HelperFunctions.getContents(file_directory, extension)

    for index, value in enumerate(list_of_contents):  # Display the files in the directory with a choice number
        print("\t[{}]: {}".format(index, value))

    try:
        i = input("Please select the text-file you want to compute: ")
    except:
        print("An exception was found!")
        return

    try:  # Attempt to open the file the user selected
        File = open(HelperFunctions.RawChatDataDir + "\\" + list_of_contents[int(i)], "r")
    except:
        print("{} isn't a valid choice".format(i))
        return

    return File, list_of_contents, i



# Convert timestamps of a file into a dictionary and count how many times each timestamp appears
def convert_raw_time_data_to_dictionary(file):
    dict_with_the_raw_time_data = {}
    for line in file: # Loop through each line of the file
        line = line.strip() # Remove the leading spaces and newline character
        line = line.lower() # Convert characters to lowercase
        # line = line.translate(line.maketrans("", "", string.punctuation)) # Removes the ':'
        words = line.split(" ") # Split the line into words

        for word in words: # Iterate over each word in line
            if (check_negative_sign(word)): pass # Looks for a negative value and skips it

            elif word in dict_with_the_raw_time_data: # Check if the word is already in dictionary
                dict_with_the_raw_time_data[word] = dict_with_the_raw_time_data[word] + 1 # Increment count of word by 1

            else: dict_with_the_raw_time_data[word] = 1 # Add the word to dictionary with count 1

    return dict_with_the_raw_time_data

# Checks to see if the first "number" is a negative
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False


def create_output_file(i, listOfContents, directory=None):
    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)])

    stripped_file_name = file_name.split("_")[0]  # We want to rename "file_ChatData.txt --> ComputedData.txt

    if(not directory):
        with open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt',
                  'w'): pass  # Empties the file

        file_instance = open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt',
                             'a')  # Create a file instance that we can use later
    if(directory):
        with open(directory + '/' + stripped_file_name + '_ComputedData.txt',
                  'w'): pass  # Empties the file

        file_instance = open(directory + '/' + stripped_file_name + '_ComputedData.txt',
                             'a')  # Create a file instance that we can use later


    return file_instance, stripped_file_name


def writeResultsToFile(file_instance, splitted_dict, name_of_dict, LAST_INDEX):
    file_instance.write('{} splitter'.format(name_of_dict))

    sorted_dict_highest_to_lowest = dict(sorted(splitted_dict.items(), key=lambda x: x[1]))

    try:
        file_instance.write("___HHMMSS\n")
        for i in range(-1, LAST_INDEX - 1, -1):
            file_instance.write(("{}:\t{}\t*:{}\tHH:MM:SS\n"
            .format(
                abs(i),
                list(sorted_dict_highest_to_lowest)[i],
                list(sorted_dict_highest_to_lowest.values())[i]
            )
            ))
    except:
        pass

    file_instance.write("============================================\n\n")
