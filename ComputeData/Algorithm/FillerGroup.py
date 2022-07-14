from Utilities.HelperFunctions import FilterChatComputeDataDir
from ComputeData.ComputeHelperFunctions \
    import create_output_file, convert_string_timestamps_into_seconds, \
    convert_raw_time_data_to_dictionary_FILTERED, \
    sanitize_raw_chat_timestamp_data_and_get_last_timestamp, create_dict_with_timestamps

def compute_filler_group(list_of_contents, selected_file_index, raw_chat_file):
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents, FilterChatComputeDataDir)
    filtered_file, last_line = sanitize_raw_chat_timestamp_data_and_get_last_timestamp(raw_chat_file.name)

    START = 0

    # We can make sure we can break it into 10 sec marks
    round_down_value = 10
    END = convert_string_timestamps_into_seconds(last_line)
    END_ROUND_DOWN = END - (END % round_down_value)

    d = create_dict_with_timestamps(START, END_ROUND_DOWN)

    data = convert_raw_time_data_to_dictionary_FILTERED(d, open(filtered_file.name, 'r'))

    print('{} has finished computing'.format(stripped_file_name + '_FILLER_ComputedData.txt'))