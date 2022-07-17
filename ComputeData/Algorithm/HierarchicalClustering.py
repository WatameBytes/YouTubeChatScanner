import numpy as np

from ComputeData.ComputeHelperFunctions import create_output_file, \
    sanitize_raw_chat_timestamp_data_and_get_last_timestamp, convert_string_timestamps_into_seconds, \
    create_dict_with_timestamps, convert_raw_time_data_to_dictionary_FILTERED
from Utilities.HelperFunctions import FilterChatComputeDataDir, STREAM_DELAY, ROUND_DOWN_VALUE


def compute_hierachical_clustering(list_of_contents, selected_file_index, filtered_file, last_line):
    START = 0

    END = convert_string_timestamps_into_seconds(last_line)
    END_ROUND_DOWN = END - (END % ROUND_DOWN_VALUE)

    # Generate a dictionary with timestamps from the START[0] to the end
    d = create_dict_with_timestamps(START, END_ROUND_DOWN)

    # This dictionary will contain how many times an instance occures in a timestamp
    data = convert_raw_time_data_to_dictionary_FILTERED(d, open(filtered_file.name, 'r'))

    sum = 0
    counter = 0
    highest_value = 0

    timestamp_list = []
    # Get the average that we will use for our threshold
    for k,v in data.items():
        if v not in timestamp_list:
            timestamp_list.append(v)

        if(v == 0 or v < 3):
            continue
        sum += v
        counter += 1
        if (v > highest_value):
            highest_value = v



    timestamp_list.sort()
    print(timestamp_list)
    avg = sum/counter
    avg = int(round(avg))
    placeholder = timestamp_list[int(len(timestamp_list)/4)]

    print("Placeholder: {}".format(placeholder))
    print("Sum: {}".format(sum))
    print("Counter: {}".format(counter))

    print("Avg: {}".format(avg))
    print("Highest Value: {}".format(highest_value))

    #print(data)
    print("======================")
    #cluster_dict = cluster(data, 5)
    cluster_dict = cluster(data, placeholder)
    print("======================")
    print(cluster_dict)

    # We want to remove single timestamps and keep only group
    # Remove 00:15 : 7 ---> Keep 02:12 - 02:14

    cleaned_dict = remove_non_intervals(cluster_dict)
    print(cleaned_dict)


    keys = list(cleaned_dict)

    values = list(cleaned_dict.values())
    overlap = 30

    group_me(keys, len(keys), overlap, values)

    clustered_dict = dict()

    for x in range(len(keys)):
        clustered_dict[keys[x]] = values[x]

    print("Clustered Dict")
    print(clustered_dict)

    print(remove_single_second(clustered_dict))


def cluster(data, threshhold):
    cluster_dict = dict()
    make_dict = True
    saved_key = None

    for k, v in data.items():
        if (v > threshhold) and make_dict:
            saved_key = k
            cluster_dict[saved_key] = data[saved_key]
            make_dict = False

        elif (v > threshhold) and not make_dict:
            #cluster_dict[saved_key] = cluster_dict[saved_key] + 1
            cluster_dict[saved_key] = cluster_dict[saved_key] + v
            new_key = str(saved_key) + "-"
            new_key = new_key.split("-")[0]
            new_key = new_key + "-" + k
            cluster_dict[new_key] = cluster_dict.pop(saved_key)
            saved_key = new_key

        else:
            make_dict = True

    return cluster_dict

def remove_non_intervals(data):
    cleaned_dict = dict()

    for k,v in data.items():
        if '-' in k:
            cleaned_dict[k] = v

    return cleaned_dict

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

def remove_single_second(data):
    removed_single_second = dict()

    for k,v in data.items():
        if(convert_string_timestamps_into_seconds(k.split("-")[1]) - convert_string_timestamps_into_seconds(k.split("-")[0]) == 1):
            continue
        removed_single_second[k] = v

    return removed_single_second