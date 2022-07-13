import os
from itertools import islice

from ComputeData import ComputeHelperFunctions
from ComputeData.ComputeHelperFunctions import writeResultsToFile
from Utilities import HelperFunctions

from ComputeData.Algorithm.PureCount import compute_no_group

splitValues = [10, 20, 30, 50, 70, 90, 110, 130, 150, 170, 190]
listOfDicts = []

# Create a dict with the amount of split values we created
for i in range(len(splitValues)):
    # for i in splitValues: --> i will be 10, 30, 50, 70, 110
    listOfDicts.append(dict())


def dataProcessing():
    # Check if the user input is valid and a file exist
    File, list_of_contents, selected_file_index = ComputeHelperFunctions.\
        files_displayed_to_user_and_user_selects_file(HelperFunctions.RawChatDataDir, "txt")

    compute_no_group(File, list_of_contents, selected_file_index)
    # # Convert the contents of a file (HH:MM:SS) and place it into multiple dictionaries
    # dict_with_raw_time_data = ComputeHelperFunctions.convert_raw_time_data_to_dictionary(
    #     File)
    #
    # file_instance, stripped_file_name = create_output_file(selected_file_index,
    #     list_of_contents)  # Create the output file that will hold all of our data
    #
    #
    #
    # # Create groups in our dictionary
    # for i in range(len(splitValues)):
    #     copy_dict_to_splitted_dic(dict_with_raw_time_data, listOfDicts[i], splitValues[i])
    #
    # for selected_file_index in range(len(splitValues)):
    #     writeResultsToFile(file_instance, listOfDicts[selected_file_index], str(splitValues[selected_file_index]))
    #
    # print('{} has finished computing'.format(stripped_file_name + '_ComputedData.txt'))


def create_output_file(i, listOfContents):
    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)])

    stripped_file_name = file_name.split("_")[0]  # We want to rename "file_ChatData.txt --> ComputedData.txt

    with open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt',
              'w'): pass  # Empties the file

    file_instance = open(HelperFunctions.ComputedDataDir + '/' + stripped_file_name + '_ComputedData.txt',
                         'a')  # Create a file instance that we can use later

    return file_instance, stripped_file_name


# Copy the original dict to a new dictionary, but group them up with a splitter
def copy_dict_to_splitted_dic(d, newDict, splitter):
    for item in chunks(d, splitter):
        newDict[list(item.keys())[0]] = sum(item.values())


def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}
