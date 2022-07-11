import os
from itertools import islice
from Utilities import HelperFunctions
from Utilities.HelperFunctions import check_negative_sign

dict_with_the_raw_time_data = dict()

splitValues = [10, 20, 30, 50, 70, 90, 110, 130, 150, 170, 190]
listOfDicts = []


# Create a dict with the amount of split values we created
for i in range(len(splitValues)):
    # for i in splitValues: --> i will be 10, 30, 50, 70, 110
    listOfDicts.append(dict())

def dataProcessing():

    # Check if the user input is valid and a file exist
    File, list_of_contents, selected_file_index = \
        files_displayed_to_user_and_user_selects_file(HelperFunctions.RawChatDataDir, "txt")


    convert_raw_time_data_to_dictionary(File) # Convert the contents of a file (HH:MM:SS) and place it into multiple dictionaries

    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents) # Create the output file that will hold all of our data


    for i in range(len(splitValues)):
        copy_dict_to_splitted_dic(dict_with_the_raw_time_data, listOfDicts[i], splitValues[i])

    for selected_file_index in range(len(splitValues)):
        writeResultsToFile(file_instance, listOfDicts[selected_file_index], str(splitValues[selected_file_index]))

    print('{} has finished computing'.format(stripped_file_name + '_ComputedData.txt'))


def files_displayed_to_user_and_user_selects_file(file_directory, extension):
    list_of_contents = HelperFunctions.getContents(file_directory, extension)

    for index, value in enumerate(list_of_contents): # Display the files in the directory with a choice number
        print("\t[{}]: {}".format(index, value))

    try:
        i = input("Please select the text-file you want to compute: ")
    except:
        print("An exception was found!")
        return

    try: # Attempt to open the file the user selected
        File = open(HelperFunctions.RawChatDataDir + "\\" + list_of_contents[int(i)], "r")
    except:
        print("{} isn't a valid choice".format(i))
        return

    return File, list_of_contents, i

def convert_raw_time_data_to_dictionary(file):
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


def create_output_file(i, listOfContents):
    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)])

    stripped_file_name = file_name.split("_")[0] # We want to rename "file_ChatData.txt --> ComputedData.txt

    with open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt', 'w'): pass # Empties the file


    file_instance = open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt', 'a') # Create a file instance that we can use later

    return file_instance, stripped_file_name


def writeResultsToFile(file_instance, splitted_dict, name_of_dict):
    file_instance.write('{} splitter'.format(name_of_dict))

    sorted_dict_highest_to_lowest = dict(sorted(splitted_dict.items(), key=lambda x: x[1]))

    try:
        file_instance.write("___HHMMSS\n")
        for i in range(-1, -31, -1):
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


# Copy the original dict to a new dictionary, but group them up with a splitter
def copy_dict_to_splitted_dic(d, newDict, splitter):
    for item in chunks(d, splitter):
        newDict[list(item.keys())[0]] = sum(item.values())

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}
