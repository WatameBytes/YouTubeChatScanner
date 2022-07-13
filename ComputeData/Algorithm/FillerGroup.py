def string_time_to_seconds(timestamp):
    try:
        h, m, s = map(int, timestamp.split(':'))
    except ValueError:
        m, s = map(int, timestamp.split(':'))
        h = 0
    return h * 3600 + m * 60 + s

def seconds_to_time_stamp(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)




def compute_filler_group(list_of_contents, selected_file_index, dict_with_raw_time_data, File):
    print("null")

def convert_raw_time_data_to_dictionary(dict_with_the_raw_time_data, file):
    for line in file: # Loop through each line of the file
        line = line.replace('\n','')

        if(line in dict_with_the_raw_time_data):
            print("FOUND")
            dict_with_the_raw_time_data[line] = dict_with_the_raw_time_data

    print(dict_with_the_raw_time_data)
    return dict_with_the_raw_time_data

raw_chat_file = "FaunaHolocure_ChatData.txt"
filtered_file = "FaunaCLEANED_ChatData.txt"

filter = open(filtered_file, 'w')

readFilter = open(filtered_file, 'r')


for line in open(raw_chat_file):
    if line.startswith("-"): pass

    else:
        filter.write(line)
        last_line = line


print(last_line)

timestamps = []
d = dict()

START = 0
END = string_time_to_seconds(last_line)

print("Start at {}".format(START))
print("End at {}".format(END))

for i in range(START, END + 1, 1):
    timestamps.append(seconds_to_time_stamp(i))
    d[seconds_to_time_stamp(i)] = 0


data = convert_raw_time_data_to_dictionary(d, readFilter)

print(d)
print(data)




