# No sorting at all, just count the values and list the highest to lowest

from ComputeData.ComputeHelperFunctions \
    import convert_raw_time_data_to_dictionary, create_output_file, writeResultsToFile

from Utilities import HelperFunctions

NUMBER_OF_LINES = -abs(30)

def compute_no_group(File, list_of_contents, selected_file_index):
    dict_with_raw_time_data = convert_raw_time_data_to_dictionary(File)
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents,
                                                           HelperFunctions.PureChatComputeData)
    writeResultsToFile(file_instance, dict_with_raw_time_data, "No Grouping", NUMBER_OF_LINES)



