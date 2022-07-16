from turtle import width

from matplotlib import pyplot as plt

from ComputeData.ComputeHelperFunctions import convert_seconds_into_timestamps, convert_string_timestamps_into_seconds


def k():
    data = {
        0: 1,
        1: 5,
        2: 6,
        3: 0,
        4: 0,
        5: 1,
        6: 2,
        7: 3,
        8: 5,
        9: 9,
        10: 7
    }

    timestamp_dict = dict()

    for i in range(0, 10169 + 1, 1):
        timestamp_dict[convert_seconds_into_timestamps(i)] = 0


    file = open('ComputeData\\FauanFallGuys_CLEANED.txt', 'r')
    print("HELLO WORLD")
    for line in file:
        line = line.replace('\n', '')

        if (line in timestamp_dict):

            timestamp_dict[line] = timestamp_dict[line] + 1

    #print(timestamp_dict)

    cluster_dict = cluster(data, 5)
    #cluster_dict = cluster(timestamp_dict, 5)
    print(cluster_dict)


def cluster(data, threshhold):
    cluster_dict = dict()
    make_dict = True
    saved_key = None

    for k, v in data.items():
        if (v > threshhold) and make_dict:
            saved_key = convert_seconds_into_timestamps(k)
            cluster_dict[saved_key] = 1
            make_dict = False

        elif (v > threshhold) and not make_dict:
            cluster_dict[saved_key] = cluster_dict[saved_key] + 1
            new_key = str(saved_key) + "-"
            new_key = new_key.split("-")[0]
            new_key = new_key + "-" + str(convert_seconds_into_timestamps(k))
            cluster_dict[new_key] = cluster_dict.pop(saved_key)
            saved_key = new_key

        else:
            make_dict = True
    return cluster_dict
