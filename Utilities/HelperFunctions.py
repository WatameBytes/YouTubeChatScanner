import os
# USE THIS WHEN WE ARE RUNNING IN OUR MAIN PROGRAM

MainDirectory = os.getcwd()

#MainDirectory = "../../../julyProject"

#MainDirectory = "../julyProject/" # USE THIS WHEN RUNNING TEST DIR


# Algo testing
#MainDirectory = "../../../julyProject"
#print(MainDirectory)

# script_dir = os.path.dirname(__file__)
# rel_path = "2091/data.txt"
# abs_file_path = os.path.join(script_dir, rel_path)

RawChatDataDir = MainDirectory + "\\RawYouTubeChatData"
VideoDownloadedDir = MainDirectory + "\\VideosDownloaded"
ComputedDataDir = MainDirectory + "\\DataComputed"
ClippedVideo = MainDirectory + "\\ClippedVideos"

PureChatComputeDataDir = MainDirectory + "\\DataComputed\\PureData"
GroupChatComputeDataDir = MainDirectory + "\\DataComputed\\GroupData"
FilterChatComputeDataDir = MainDirectory + "\\DataComputed\\FillerData"

splitValues = [1, 5, 10, 15, 20, 25, 30]
NUMBER_OF_LINES = -abs(30)
STREAM_DELAY = 5
ROUND_DOWN_VALUE = 10

def getMainDirectory():
    return os.getcwd()


def printContents(directory, extension, customMessage = None):
    if(extension.startswith(".")):
        extension[1:]

    listOfContents = []

    for i in os.listdir(directory):
        if(i.endswith(extension)):
            listOfContents.append(i)

    if customMessage is None:
        print("{}".format(listOfContents))
    else:
        print("{}: {}".format(customMessage, listOfContents))

def getContents(directory, extension):
    listOfContents = []

    for i in os.listdir(directory):
        if (i.endswith(extension)):
            listOfContents.append(i)

    return listOfContents


# Checks to see if the first "number" is a negative
def check_negative_sign(s):
    if(s[0] == '-'):
        return True
    else:
        return False

def string_time_to_seconds(timestamp):
    try:
        h, m, s = map(int, timestamp.split(':'))
    except ValueError:
        m, s = map(int, timestamp.split(':'))
        h = 0
    return h * 3600 + m * 60 + s

