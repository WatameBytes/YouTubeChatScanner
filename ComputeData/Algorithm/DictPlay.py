dict = {
    "Neko": 2,
    "Doggo": 5
}
print(dict)

if "Neko" in dict:
    print("FOUND YOU ^_^")
    dict["Neko"] = dict["Neko"] + 1

print(dict)

def increment(x):
    return x + 1

x = 10
print(x)
y = increment(x)
print(y)

