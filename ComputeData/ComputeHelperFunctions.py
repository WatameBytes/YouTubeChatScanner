import os
from itertools import islice
from Utilities import HelperFunctions

# Check to see if a string, -0:22, is a negative sign
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False


def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}

# Convert a text file that has been cleaned and a dictionary with ALL timestamps
def convert_raw_time_data_to_dictionary_FILTERED(dict_with_the_raw_time_data, file):
    for line in file:  # Loop through each line of the file
        line = line.replace('\n', '') # Not necessary, but makes line looks nice when printing

        if (line in dict_with_the_raw_time_data):
            dict_with_the_raw_time_data[line] = dict_with_the_raw_time_data[line] + 1

    return dict_with_the_raw_time_data

# Convert a text file with timestamps and place them into a dictionary and how many times they appear
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

# STR[01:11:44] --> INT[4304]
def convert_string_timestamps_into_seconds(timestamp):
    try:
        h, m, s = map(int, timestamp.split(':'))
    # No hour is given --> Convert only MIN/SECS
    except ValueError:
        m, s = map(int, timestamp.split(':'))
        h = 0
    return h * 3600 + m * 60 + s

# Group the contents of a dictionary WITH a splitter
def copy_dict_to_splitted_dic(d, newDict, splitter):
    for item in chunks(d, splitter):
        newDict[list(item.keys())[0]] = sum(item.values())
    return newDict


def create_dict_with_split_value_array(splitValues):
    listOfDicts = []
    # Create a dict with the amount of split values we created
    for i in range(len(splitValues)):
        # for i in splitValues: --> i will be 10, 30, 50, 70, 110
        listOfDicts.append(dict())
    return listOfDicts


def create_dict_with_timestamps(START, END_ROUND_DOWN):
    timestamp_dict = dict()
    for i in range(START, END_ROUND_DOWN + 1, 1):
        timestamp_dict[convert_seconds_into_timestamps(i)] = 0

    return timestamp_dict

# Give it an array of files, user choice index, and the directory to SAVE it in that directory
def create_output_file(user_choice_index, listOfContents, directory=None):
    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(user_choice_index)])

    stripped_file_name = file_name.split("_")[0]  # We want to rename "file_ChatData.txt --> ComputedData.txt

    if(not directory):
        # Empties the file
        with open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt', 'w'): pass

        # Create a file instance that we can use later
        file_instance = open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt','a')
    if(directory):
        # Empties the file
        with open(directory + '/' + stripped_file_name + '_ComputedData.txt', 'w'): pass

        # Create a file instance that we can use later
        file_instance = open(directory + '/' + stripped_file_name + '_ComputedData.txt', 'a')

    return file_instance, stripped_file_name


def get_last_timestamp_from_from(chat_file):
    for line in open(chat_file):
        last_line = line
    return last_line

# Display a directory contents and allow the user to select a file
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


def sanitize_raw_chat_timestamp_data_and_get_last_timestamp(raw_chat_file, OFFSET):
    stripped_file_name = raw_chat_file.split("_")[0]  # We want to rename "file_ChatData.txt --> ComputedData.txt
    filtered_output_file = open(stripped_file_name + "_CLEANED.txt", 'w')

    for line in open(raw_chat_file):
        if line.startswith("-"):
            pass

        else:
            if(OFFSET != 0):
                line = convert_string_timestamps_into_seconds(line)
                if(line <= OFFSET):
                    line = 0
                else:
                    line -= OFFSET
                    line = convert_seconds_into_timestamps(line)
                    filtered_output_file.write(line + '\n')
                    last_line = line



            else:
                if (len(line) == 5):
                    filtered_output_file.write('0' + line)
                else:
                    filtered_output_file.write(line)
                last_line = line

    return filtered_output_file, last_line


def write_results_to_file(file_instance, splitted_dict, name_of_dict, LAST_INDEX):
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
