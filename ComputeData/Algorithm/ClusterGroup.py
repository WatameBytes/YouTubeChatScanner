from ComputeData.ComputeHelperFunctions \
    import create_output_file, write_results_to_file, copy_dict_to_splitted_dic, create_dict_with_split_value_array, \
    sanitize_raw_chat_timestamp_data_and_get_last_timestamp
from Utilities import HelperFunctions
from Utilities.HelperFunctions import NUMBER_OF_LINES, ClusterChatComputeDataDir, STREAM_DELAY, \
    CLUSTER_INTERVAL_THRESHHOLD, CLUSTER_OVERLAP_RADIUS
from ComputeData.ComputeHelperFunctions import convert_seconds_into_timestamps, convert_string_timestamps_into_seconds

def compute_cluster(list_of_contents, selected_file_index, raw_chat_file):
    file_instance, stripped_file_name = create_output_file(selected_file_index, list_of_contents,
                                                           ClusterChatComputeDataDir)

    filtered_file, last_line = sanitize_raw_chat_timestamp_data_and_get_last_timestamp(raw_chat_file.name, STREAM_DELAY)

    timestamp_dict = dict()

    # TODO FIX IT SO IT ISNT HARDCODED TO HAVE 10169
    # From the start and end of the timestamp folder
    # print(last_line)
    final_length = convert_string_timestamps_into_seconds(last_line) + 1

    for i in range(0, final_length, 1):
        timestamp_dict[convert_seconds_into_timestamps(i)] = 0

    for line in open(filtered_file.name, 'r'):
        line = line.replace('\n', '')

        if (line in timestamp_dict):
            timestamp_dict[line] = timestamp_dict[line] + 1

    # timestamp_dict: Is practically PureCount Algo, but with cleaned data
    # and the data is cleaned --> An improved version of PureCount


    # Cluster_Interval_Threshold: How many times should a timestamp appear to consider it? Assume it's 5
    # 00:18, 00:18, 00:18, 00:18, 00:18, 00:18,  We passed the threshhold, so consider it
    # We find other timestamps near it that also passed the timestamp threshold and group them!

    # '02:12': 12, '02:13': 8, '02:14': 6 -- CLUSTER --> '02:12 - 02:14': 3 ONLY SEQUENTIAL!!!!
    cluster_dict = cluster(timestamp_dict, CLUSTER_INTERVAL_THRESHHOLD)


    # Only keep timestamp intervals and remove single timestamps
    # '02:09': 1, '02:12-02:14': 3 -- REMOVE_NON --> '02:12-02:14': 3
    cleaned_dict = remove_non_intervales(cluster_dict)

    keys = list(cleaned_dict)
    value = list(cleaned_dict.values())

    # Our cluster overlap radius is 15 for this example
    # {'02:12-02:14': 3, '02:18-02:21': 4, '02:27-02:28': 2,
    # '02:31-02:32': 2, '02:36-02:37': 2, '02:50-02:52': 3, '02:56-02:57': 2, '03:00-03:01': 2,
    # GROUP ALGO
    # '02:12-03:01': 20  ANYTHING WITHIN OVERLAP_RADIUS is grouped!!!!
    group_me(keys, len(keys), CLUSTER_OVERLAP_RADIUS, value)

    clustered_dict = dict()

    for x in range(len(keys)):
        clustered_dict[keys[x]] = value[x]

    write_results_to_file(file_instance, clustered_dict, "Cluster", NUMBER_OF_LINES)
    # print(clustered_dict)

    # file_instance.write("TEST")


    print('{} has finished computing'.format(stripped_file_name + '_CLUSTER_ComputedData.txt'))



def remove_non_intervales(data):
    cleaned_dict = dict()
    make_dict = True
    saved_key = None

    for k,v in data.items():
        if '-' in k:
            cleaned_dict[k] = v

    return cleaned_dict


def cluster(data, threshhold):
    cluster_dict = dict()
    make_dict = True
    saved_key = None

    for k, v in data.items():
        if (v > threshhold) and make_dict:
            saved_key = k
            cluster_dict[saved_key] = 1
            make_dict = False

        elif (v > threshhold) and not make_dict:
            cluster_dict[saved_key] = cluster_dict[saved_key] + 1
            new_key = str(saved_key) + "-"
            new_key = new_key.split("-")[0]
            new_key = new_key + "-" + k
            cluster_dict[new_key] = cluster_dict.pop(saved_key)
            saved_key = new_key

        else:
            make_dict = True
    return cluster_dict

def group_me(keys, check, overlap, value):
    if check == 0:
        return

    before_group_size = len(keys)

    for i in range(len(keys)):
        if (i + 1 >= len(keys)):
            break

        check_first = keys[i].split('-')[1]
        check_first_value = value[i]

        check_second = keys[i + 1].split('-')[0]
        check_second_value = value[i + 1]

        if ((convert_string_timestamps_into_seconds(check_second) - convert_string_timestamps_into_seconds(check_first)) < overlap):
            new_key = keys[i].split('-')[0] + "-"
            new_key = new_key + keys[i + 1].split('-')[1]

            keys[i] = new_key
            keys.pop(i + 1)

            value[i] = check_first_value + check_second_value
            value.pop(i + 1)


    if(before_group_size == len(keys)):
        return

    check -= 1
    group_me(keys, check, overlap, value)
