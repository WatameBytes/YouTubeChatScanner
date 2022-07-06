# Using the chat timestmaps, create a dictionary that will count the occurences
# and show us the most popular times within a time frame
# The time shown is where to start

import string
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

def writeToData(starData, newDict, nameOfDict):
    starData.write('{} splitter'.format(nameOfDict))
    dic2 = dict(sorted(newDict.items(), key=lambda x: x[1]))
    try:
        starData.write("___HHMMSS\n")
        starData.write(("1st: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-1], list(dic2.values())[-1])))
        starData.write(("2nd: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-2], list(dic2.values())[-2])))
        starData.write(("3rd: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-3], list(dic2.values())[-3])))
        starData.write(("4th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-4], list(dic2.values())[-4])))
        starData.write(("5th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-5], list(dic2.values())[-5])))
        starData.write(("6th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-6], list(dic2.values())[-6])))
        starData.write(("7th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-7], list(dic2.values())[-7])))
        starData.write(("8th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-8], list(dic2.values())[-8])))
        starData.write(("9th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-9], list(dic2.values())[-9])))
        starData.write(("10th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-10], list(dic2.values())[-10])))
        starData.write(("11th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-11], list(dic2.values())[-11])))
        starData.write(("12th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-12], list(dic2.values())[-12])))
        starData.write(("13th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-13], list(dic2.values())[-13])))
        starData.write(("14th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-14], list(dic2.values())[-14])))
        starData.write(("15th: {}\t*:{}\tHH:MM:SS\n".format(list(dic2)[-15], list(dic2.values())[-15])))

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


# Python requires that we work top-down...
class CalculateData:
    def __init__(self, chatDataFile, justTheName):
        self.file = open(chatDataFile)

        # Counts how many instances a timestamp appears :: plus removes negative values
        self.timeToDict() # Create the original

        valuesForDicts = [
            10, 30, 50, 70, 90, 110, 130, 150, 170, 190
        ]

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
        with open(justTheName + '_StarData.txt', 'w'): pass

        starData = open(justTheName + '_StarData.txt', 'a')

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

        print('{} has finished computing'.format(justTheName))
    # Places the data into a dictionary for us to use
    def timeToDict(self):
        # Loop through each line of the file
        for line in self.file:
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


    def printDic(self, dictionary):
        for x in dictionary.keys():
            print(x)

    def chunks(self, data, SIZE=1000000):
        it = iter(data)
        for i in range(0, len(data), SIZE):
            yield {k: data[k] for k in islice(it, SIZE)}


    # def declareDics(self):
    #     self.originalDict = dict()
    #     self._10SplitDict = dict()
    #     self._30SplitDict = dict()
    #     self._50SplitDict = dict()
    #     self._70SplitDict = dict()
    #     self._90SplitDict = dict()
    #     self._110SplitDict = dict()
    #     self._130SplitDict = dict()
    #     self._150SplitDict = dict()
    #     self._170SplitDict = dict()
    #     self._190SplitDict = dict()


# Looks to see of the first character is a negative sign
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False

