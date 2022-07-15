# Groups timestamps into X[splitter] and gives us the first timestamp of the group
# PRO: Groups up the data to prevent multiple instance in the same area from occuring
# CON: Gaps occur and wanting to get '30' seconds could give us 0:01, 0:03, 0:25, 0:30, [CONTINUE]
# CON: We are only given the first TIMESTAMP --> PLAN ACCORDINGLY


from Utilities.HelperFunctions import GroupChatComputeDataDir, splitValues, NUMBER_OF_LINES

from ComputeData.ComputeHelperFunctions \
    import create_output_file, write_results_to_file, copy_dict_to_splitted_dic, create_dict_with_split_value_array



listOfDicts = []
splitted_dic = []

def compute_group(list_of_contents, selected_file_index, dict_with_raw_time_data):
    listOfDicts = create_dict_with_split_value_array(splitValues)
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents, GroupChatComputeDataDir)

    #Create groups in our dictionary
    for i in range(len(splitValues)):
        splitted_dic.append(copy_dict_to_splitted_dic(dict_with_raw_time_data, listOfDicts[i], splitValues[i]))

    for selected_file_index in range(len(splitValues)):
        write_results_to_file(file_instance, splitted_dic[selected_file_index], str(splitValues[selected_file_index]), NUMBER_OF_LINES)

    print('{} has finished computing'.format(stripped_file_name + '_GROUP_ComputedData.txt'))