from ComputeData.ComputeHelperFunctions import convert_string_timestamps_into_seconds
# TODO: REQUIRE US TO HAVE AN INTERVAL DICT

group = {'02:12-02:14': 3, '02:18-02:21': 4, '02:27-02:28': 2, '02:31-02:32': 2, '02:36-02:37': 2, '02:50-02:52': 3, '02:56-02:57': 2, '03:00-03:01': 2}

keys = list(group)
value = list(group.values())

print(group)


def group_me(keys, check, overlap):
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
    group_me(keys, check, overlap)


group_me(keys, len(keys), 5)

clustered_dict = dict()
for x in range(len(keys)):
    clustered_dict[keys[x]] = value[x]

print(clustered_dict)


