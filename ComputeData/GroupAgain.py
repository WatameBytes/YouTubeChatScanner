from itertools import islice

from ComputeData.ComputeHelperFunctions import convert_string_timestamps_into_seconds

group = {'02:12-02:14': 3, '02:18-02:21': 4, '02:27-02:28': 2, '02:31-02:32': 2, '02:36-02:37': 2, '02:50-02:52': 3, '02:56-02:57': 2, '03:00-03:01': 2}

keys = list(group)

#keys = list(group)
value = list(group.values())

# print(keys)
# print(value)

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

def get_nth_value(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, value in enumerate(dictionary.values()):
        if i == n:
            return value
    raise IndexError("dictionary index out of range")

cluster_group = dict()
make_dict = True
saved_key = None


index = 1
print(group)
#del group[next(islice(group, index, None))]
#print(group)
overlap = 5


print("==================")
orginal = keys

def group_me(keys, check):
    if check == 0:
        return

    before_group_size = len(keys)


    for i in range(len(keys)):
        if (i + 1 >= len(keys)):
            break

        check_first = keys[i].split('-')[1]
        check_second = keys[i + 1].split('-')[0]

        if ((convert_string_timestamps_into_seconds(check_second) - convert_string_timestamps_into_seconds(check_first)) < overlap):
            new_key = keys[i].split('-')[0] + "-"
            new_key = new_key + keys[i + 1].split('-')[1]

            keys[i] = new_key
            keys.pop(i + 1)

        # print("Keys:{} ".format(keys))
        # print("===================")


    if(before_group_size == len(keys)):
        return

    check -= 1
    group_me(keys, check)


group_me(keys, len(keys))

print(keys)

# #print(len(group))
# for i in range(len(group)):
#     print(group.values())

#for k,v in group.values():

    #print(k)


# for i in range(len(keys)):
#
#     if(len(keys) == i or ((i + 1) > len(keys))):
#         break
#
#     first = keys[i]
#     second = keys[i + 1]
#
#     print(overlap)
#     print(first)
#     print(second)
#
#     check_first = convert_string_timestamps_into_seconds(first.split('-')[1])
#     check_second = convert_string_timestamps_into_seconds(second.split('-')[0])
#
#     if((check_second - check_first) < overlap):
#         new_key = first.split('-')[0] + "-" + second.split('-')[1]
#         print("New key: " + new_key)
#
#         print("Overlap detected")
#         cluster_group[new_key] = value[i] + value[i + 1]
#
#
#     keys.pop(i + 1)
#     value.pop(i + 1)
#     print("-----------")
#
#
# print("HELLO WORLD")
# print("HE")
# print(group)
# print(cluster_group)

