from ComputeData.ComputeHelperFunctions import convert_seconds_into_timestamps, convert_string_timestamps_into_seconds

def k():

    timestamp_dict = dict()

    # From the start and end of the timestamp folder
    for i in range(0, 10169 + 1, 1):
        timestamp_dict[convert_seconds_into_timestamps(i)] = 0


    file = open('ComputeData\\FauanFallGuys_CLEANED.txt', 'r')
    for line in file:
        line = line.replace('\n', '')

        if (line in timestamp_dict):
            timestamp_dict[line] = timestamp_dict[line] + 1


    cluster_dict = cluster(timestamp_dict, 5)
    print("Cluster-Data: {}".format(cluster_dict))

    print("Removing non-interval values")
    cleaned_dict = remove_non_intervals(cluster_dict)
    print("Cleaned-Data: {}".format(cleaned_dict))

    keys = list(cleaned_dict)
    value = list(cleaned_dict.values())
    overlap = 15
    group_me(keys, len(keys), overlap, value)

    clustered_dict = dict()

    for x in range(len(keys)):
        clustered_dict[keys[x]] = value[x]

    print("Clustered Dict")
    print(clustered_dict)







def remove_non_intervals(data):
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
