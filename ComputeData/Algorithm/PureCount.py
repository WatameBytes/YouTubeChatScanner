# No sorting at all, just count the values and list the highest to lowest
# PRO: Gives us the EXACT timestamp that chat reacted
# CON: If chat reacted in a moment for more than one sec, we have multiple instances in the same time area

from ComputeData.ComputeHelperFunctions \
    import convert_raw_time_data_to_dictionary_UNFILTERED, create_output_file, write_results_to_file

from Utilities import HelperFunctions

NUMBER_OF_LINES = -abs(30)

def compute_no_group(list_of_contents, selected_file_index, dict_with_raw_time_data):
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents,
                                                           HelperFunctions.PureChatComputeDataDir)

    write_results_to_file(file_instance, dict_with_raw_time_data, "No Grouping", NUMBER_OF_LINES)

    print('{} has finished computing'.format(stripped_file_name + '_PURE_ComputedData.txt'))



