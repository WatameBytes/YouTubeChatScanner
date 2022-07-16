# Creates timestamps for ANYTHING between 0:00:00 to the end of the video
# Meaning we break the data into seconds instead of groups --> 10 means break it every 10 secs
# PRO: THE BEST ALGORITHM OF THE THREE
# PRO: Implemented an OFFSET, since chat takes time to react due to stream delay and human reaction
# CON: One con I see is that we are manually grouping them by seconds. We could look into grouping them with some
# clustering algorithm

from Utilities.HelperFunctions import FilterChatComputeDataDir, splitValues, NUMBER_OF_LINES, STREAM_DELAY, ROUND_DOWN_VALUE

from ComputeData.ComputeHelperFunctions \
    import create_output_file, convert_string_timestamps_into_seconds, \
    convert_raw_time_data_to_dictionary_FILTERED, \
    sanitize_raw_chat_timestamp_data_and_get_last_timestamp, create_dict_with_timestamps, \
    copy_dict_to_splitted_dic, create_dict_with_split_value_array, write_results_to_file


def compute_filler_group(list_of_contents, selected_file_index, raw_chat_file):
    splitted_dic = []

    listOfDicts = create_dict_with_split_value_array(splitValues)

    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents, FilterChatComputeDataDir)
    filtered_file, last_line = sanitize_raw_chat_timestamp_data_and_get_last_timestamp(raw_chat_file.name, STREAM_DELAY)

    START = 0

    # We can make sure we can break it into 10 sec marks
    END = convert_string_timestamps_into_seconds(last_line)
    END_ROUND_DOWN = END - (END % ROUND_DOWN_VALUE)

    d = create_dict_with_timestamps(START, END_ROUND_DOWN)

    data = convert_raw_time_data_to_dictionary_FILTERED(d, open(filtered_file.name, 'r'))
    for i in range(len(splitValues)):
        splitted_dic.append(copy_dict_to_splitted_dic(data, listOfDicts[i], splitValues[i]))

    for selected_file_index in range(len(splitValues)):
        write_results_to_file(file_instance, splitted_dic[selected_file_index], str(splitValues[selected_file_index]), NUMBER_OF_LINES)

    for selected_file_index in range(len(splitValues)):
        write_results_to_file(file_instance, splitted_dic[selected_file_index], str(splitValues[selected_file_index]), NUMBER_OF_LINES)

    file_instance.close()
    print('{} has finished computing'.format(stripped_file_name + '_FILLER_ComputedData.txt'))