import os
from itertools import islice

originalDict = dict()
newDict = dict()
nSplitter = 20

_10SplitDict = dict()
_30SplitDict = dict()
_50SplitDict = dict()
_70SplitDict = dict()
_90SplitDict = dict()
_110SplitDict = dict()
_130SplitDict = dict()
_150SplitDict = dict()
_170SplitDict = dict()
_190SplitDict = dict()

from Utilities import HelperFunctions


def DataCompute():
    listOfContents = HelperFunctions.getContents(HelperFunctions.RawChatDataDir, ".txt")

    for index, value in enumerate(listOfContents):
        print("\t[{}]: {}".format(index, value))
    i = None

    try:
        i = input("Please select the text-file you want to compute: ")
    except:
        print("An exception was found!")
        return
    File = None

    try:
        File = open(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)], "r")
    except:
        print("{} isn't a valid choice".format(i))
        return

    timeToDict(File)

    file_name = os.path.basename(HelperFunctions.RawChatDataDir + "\\" + listOfContents[int(i)])
    strippedFileName = file_name.split("_")[0]

    copyOrgignalToNew(originalDict, newDict, 20)

    copyOrgignalToNew(originalDict, _10SplitDict, 10)
    copyOrgignalToNew(originalDict, _30SplitDict, 30)
    copyOrgignalToNew(originalDict, _50SplitDict, 50)
    copyOrgignalToNew(originalDict, _70SplitDict, 70)
    copyOrgignalToNew(originalDict, _90SplitDict, 90)
    copyOrgignalToNew(originalDict, _110SplitDict, 110)
    copyOrgignalToNew(originalDict, _130SplitDict, 130)
    copyOrgignalToNew(originalDict, _150SplitDict, 150)
    copyOrgignalToNew(originalDict, _170SplitDict, 170)
    copyOrgignalToNew(originalDict, _190SplitDict, 190)

    # Empties the file
    with open(HelperFunctions.ComputedDataDir + '/' + strippedFileName + '_ComputedData.txt', 'w'): pass
    starData = open(HelperFunctions.ComputedDataDir + '/' + strippedFileName + '_ComputedData.txt', 'a')

    writeToData(starData, newDict, 'orginal')
    writeToData(starData, _10SplitDict, '10')
    writeToData(starData, _30SplitDict, '30')
    writeToData(starData, _50SplitDict, '50')
    writeToData(starData, _70SplitDict, '70')
    writeToData(starData, _90SplitDict, '90')
    writeToData(starData, _110SplitDict, '110')
    writeToData(starData, _130SplitDict, '130')
    writeToData(starData, _150SplitDict, '150')
    writeToData(starData, _170SplitDict, '170')
    writeToData(starData, _190SplitDict, '190')

    print('{} has finished computing'.format(strippedFileName+'_ComputedData.txt'))

def timeToDict(file):
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

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}

# Looks to see of the first character is a negative sign
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}

def printDic(dictionary):
    for x in dictionary.keys():
        print(x)

# Copy the values of item into a dictionary we can use for ourselves
def copyOrgignalToNew(d, newDict, splitter):
    for item in chunks(d, splitter):
        # print('Name: ', list(item.keys())[0] ,item, 'sum is ', sum(item.values()))
        # Key would be the time it starts with the sum of the values between it
        newDict[list(item.keys())[0]] = sum(item.values())

def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def writeToData(starData, newDict, nameOfDict):
    starData.write('{} splitter'.format(nameOfDict))
    dic2 = dict(sorted(newDict.items(), key=lambda x: x[1]))
    try:
        starData.write("___HHMMSS\n")
        for i in range(-1, -31, -1):
            starData.write(("{}:\t{}\t*:{}\tHH:MM:SS\n".format(abs(i) ,list(dic2)[i], list(dic2.values())[i])))

    except:
        pass

    sumOfData = sum(dic2.values())

    numOfData = len(dic2)
    avg = (sumOfData / numOfData) + nSplitter
    starData.write("Avg: {}\n".format(avg))
    starData.write('\n')

    # Write to the text file stars :: Perhaps didive by 10 or something to lower it's meaning 270 -> 27 stars
    # for x, y in newDict.items():
    #     starData.write(("Start at {} *:{}\t".format(x, y)))
    #     for n in range(y):
    #         starData.write(('*'))
    #     starData.write("\n")

    starData.write("============================================\n\n")


