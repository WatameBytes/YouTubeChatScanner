def string_time_to_seconds(timestamp):
    h, m, s = map(int, timestamp.split(':'))
    return h * 3600 + m * 60 + s


test = {"1:24:22": 146, "1:23:22": 143, "1:42:47": 140, "1:21:59": 140}

print(test["1:24:22"])

new_key = list(test)
print(new_key[0])

test_list = list(test)
print(string_time_to_seconds(test_list[0])) # Seconds
print(string_time_to_seconds(list(test)[0]))
#print(test_list[0])
