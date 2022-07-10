import os

MainDirectory = os.getcwd()

RawChatDataDir = MainDirectory + "\\RawYouTubeChatData"
VideoDownloadedDir = MainDirectory + "/VideosDownloaded"
ComputedDataDir = MainDirectory + "/DataComputed"

def getMainDirectory():
    return os.getcwd()


def printContents(directory, extension, customMessage = None):
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