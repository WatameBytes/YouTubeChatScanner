import os
import threading
from itertools import islice

from ComputeData import ComputeHelperFunctions
from ComputeData.Algorithm.HierarchicalClustering import compute_hierachical_clustering
from ComputeData.ComputeHelperFunctions import write_results_to_file, convert_raw_time_data_to_dictionary_UNFILTERED, \
    sanitize_raw_chat_timestamp_data_and_get_last_timestamp
from Utilities import HelperFunctions

from ComputeData.Algorithm.PureCount import compute_no_group
from ComputeData.Algorithm.GroupCount import compute_group
from ComputeData.Algorithm.FillerGroup import compute_filler_group
from Utilities.HelperFunctions import STREAM_DELAY


def dataProcessing():
    # Get the user input that will grab us a RAW_CHAT_DATA file
    File, list_of_contents, selected_file_index = ComputeHelperFunctions.\
        files_displayed_to_user_and_user_selects_file(HelperFunctions.RawChatDataDir, "_ChatData.txt")

    # Create a dictionary with that text file and give us a counter for the timestamps in the file
    dict_with_raw_time_data = convert_raw_time_data_to_dictionary_UNFILTERED(File)

    # Create a clean chat data file --> [Normalize timestamps, remove negative timestamps, and get last timestamp]
    filtered_file, last_line = sanitize_raw_chat_timestamp_data_and_get_last_timestamp(File.name, STREAM_DELAY)


    #compute_no_group(list_of_contents, selected_file_index, dict_with_raw_time_data)
    #compute_group(list_of_contents, selected_file_index, dict_with_raw_time_data)
    #compute_filler_group(list_of_contents, selected_file_index, filtered_file, last_line)

    compute_hierachical_clustering(list_of_contents, selected_file_index, filtered_file, last_line)





