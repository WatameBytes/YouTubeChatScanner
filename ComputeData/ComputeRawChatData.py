import os
from itertools import islice
from Utilities import HelperFunctions

originalDict = dict()
newDict = dict()
nSplitter = 20

splitValues = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
listOfDicts = []

# for i in splitValues: --> i will be 10, 30, 50, 70, 110
for i in range(len(splitValues)):
    listOfDicts.append(dict())


def DataProcessing():
    listOfContents = HelperFunctions.getContents(HelperFunctions.RawChatDataDir, ".txt")

    for index, value in enumerate(listOfContents):
        print("\t[{}]: {}".format(index, value))

    try:
        i = input("Please select the text-file you want to compute: ")
    except:
        print("An exception was found!")
        return


    try:
        File = open(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)], "r")
    except:
        print("{} isn't a valid choice".format(i))
        return



    convertRawTimeDataToDictionary(File)

    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)])
    strippedFileName = file_name.split("_")[0]

    copyOrgignalToNew(originalDict, newDict, 20)

    for i in range(len(splitValues)):
        copyOrgignalToNew(originalDict, listOfDicts[i], splitValues[i])

    # Empties the file
    with open(HelperFunctions.ComputedDataDir + '/' + strippedFileName + '_ComputedData.txt', 'w'): pass

    starData = open(HelperFunctions.ComputedDataDir + '/' + strippedFileName + '_ComputedData.txt', 'a')

    writeResultsToFile(starData, newDict, 'orginal')

    for i in range(len(splitValues)):
        writeResultsToFile(starData, listOfDicts[i], str(splitValues[i]))

    print('{} has finished computing'.format(strippedFileName+'_ComputedData.txt'))

def convertRawTimeDataToDictionary(file):
    # Loop through each line of the file
    for line in file:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        # line = line.translate(line.maketrans("", "", string.punctuation)) # This removes the ':'

        # Split the line into words
        words = line.split(" ")
        # Iterate over each word in line
        for word in words:
            # Looks for a negative value and skips it
            if (check_negative_sign(word)):
                pass
            # Check if the word is already in dictionary
            elif word in originalDict:
                # Increment count of word by 1
                originalDict[word] = originalDict[word] + 1
            else:
                # Add the word to dictionary with count 1
                originalDict[word] = 1


def printDic(dictionary):
    for x in dictionary.keys():
        print(x)


# Checks to see if the first "number" is a negative
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False


def writeResultsToFile(starData, newDict, nameOfDict):
    starData.write('{} splitter'.format(nameOfDict))
    dic2 = dict(sorted(newDict.items(), key=lambda x: x[1]))
    try:
        starData.write("___HHMMSS\n")
        for i in range(-1, -31, -1):
            starData.write(("{}:\t{}\t*:{}\tHH:MM:SS\n".format(abs(i) ,list(dic2)[i], list(dic2.values())[i])))

    except:
        pass

    starData.write("============================================\n\n")


def printDic(dictionary):
    for x in dictionary.keys():
        print(x)


# Copy the original dict to a new dictionary, but group them up with a splitter
def copyOrgignalToNew(d, newDict, splitter):
    for item in chunks(d, splitter):
        newDict[list(item.keys())[0]] = sum(item.values())


def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}
