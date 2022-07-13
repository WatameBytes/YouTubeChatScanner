# Groups timestamps into X[splitter] and gives us the first timestamp of the group
# PRO: Groups up the data to prevent multiple instance in the same area from occuring
# CON: Gaps occur and wanting to get '30' seconds could give us 0:01, 0:03, 0:25, 0:30, [CONTINUE]
# CON: We are only given the first TIMESTAMP --> PLAN ACCORDINGLY

from ComputeData.ComputeHelperFunctions \
    import create_output_file, writeResultsToFile, copy_dict_to_splitted_dic
from Utilities.HelperFunctions import GroupChatComputeDataDir

NUMBER_OF_LINES = -abs(30)

splitValues = [5, 10, 15, 20, 25]
listOfDicts = []
splitted_dic = []

# Create a dict with the amount of split values we created
for i in range(len(splitValues)):
    # for i in splitValues: --> i will be 10, 30, 50, 70, 110
    listOfDicts.append(dict())

def compute_group(list_of_contents, selected_file_index, dict_with_raw_time_data):
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents, GroupChatComputeDataDir)


    #Create groups in our dictionary
    for i in range(len(splitValues)):
        splitted_dic.append(copy_dict_to_splitted_dic(dict_with_raw_time_data, listOfDicts[i], splitValues[i]))

    for selected_file_index in range(len(splitValues)):
        writeResultsToFile(file_instance, splitted_dic[selected_file_index], str(splitValues[selected_file_index]), NUMBER_OF_LINES)

    print('{} has finished computing'.format(stripped_file_name + '_GROUP_ComputedData.txt'))