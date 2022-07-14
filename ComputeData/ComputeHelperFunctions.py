import os
from itertools import islice

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
def convert_raw_time_data_to_dictionary_UNFILTERED(file):
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


# Copy the original dict to a new dictionary, but group them up with a splitter
def copy_dict_to_splitted_dic(d, newDict, splitter):

    for item in chunks(d, splitter):
        newDict[list(item.keys())[0]] = sum(item.values())

    return newDict


def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}

# STR[01:11:44] --> INT[4304]
def convert_string_timestamps_into_seconds(timestamp):
    try:
        h, m, s = map(int, timestamp.split(':'))
    # No hour is given --> Convert only MIN/SECS
    except ValueError:
        m, s = map(int, timestamp.split(':'))
        h = 0
    return h * 3600 + m * 60 + s

# INT[653] --> STR[10:53]
def convert_seconds_into_timestamps(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if (hour == 0):  # Without this we get '0:00:00' instead of '00:00
        return "{:02}:{:02}".format(minutes, seconds)

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def convert_raw_time_data_to_dictionary_FILTERED(dict_with_the_raw_time_data, file):
    for line in file:  # Loop through each line of the file
        line = line.replace('\n', '') # Not necessary, but makes line looks nice when printing

        if (line in dict_with_the_raw_time_data):
            dict_with_the_raw_time_data[line] = dict_with_the_raw_time_data[line] + 1

    return dict_with_the_raw_time_data


def sanitize_raw_chat_timestamp_data_and_get_last_timestamp(raw_chat_file):
    filtered_output_file = open(raw_chat_file + "CLEANED", 'w')

    for line in open(raw_chat_file):
        if line.startswith("-"):
            pass

        else:
            last_line = line
            if (len(line) == 5):
                filtered_output_file.write('0' + line)
            else:
                filtered_output_file.write(line)
    return filtered_output_file, last_line


def create_dict_with_timestamps(START, END_ROUND_DOWN):
    timestamp_dict = dict()
    for i in range(START, END_ROUND_DOWN + 1, 1):
        timestamp_dict[convert_seconds_into_timestamps(i)] = 0

    return timestamp_dict


def create_dict_with_split_value_array(splitValues):
    listOfDicts = []
    # Create a dict with the amount of split values we created
    for i in range(len(splitValues)):
        # for i in splitValues: --> i will be 10, 30, 50, 70, 110
        listOfDicts.append(dict())
    return listOfDicts