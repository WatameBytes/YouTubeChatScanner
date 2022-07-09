import os

MainDirectory = os.getcwd()

RawChatDataDir = MainDirectory + "/RawYouTubeChatData"
VideoDownloadedDir = MainDirectory + "/VideosDownloaded"

def getMainDirectory():
    return os.getcwd()

def printContents(directory, hasFilter, customMessage):
    listOfContents = []

    for i in os.listdir(directory):
        if(hasFilter and i.endswith(".mp4")):
            listOfContents.append(i)
        elif(not hasFilter):
            listOfContents.append(i)

    print("{}: {}".format(customMessage, listOfContents))