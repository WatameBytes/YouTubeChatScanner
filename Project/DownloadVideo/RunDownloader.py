import os.path
import threading
import os

from Project.Utilities.HelperFunctions import getMainDirectory

videoLink = None
title = None
videoDownloadFolder = './VideosDownloaded'
prefix = "https://www.youtube.com/watch?v="

mainDirectory = str(getMainDirectory())


def prerequisite_checklist():
    global videoLink, title, prefix

    if(getUserInput()):
        return

    try:
        print("YouTube Link {}".format(videoLink))
        print("Title of the Video {}".format(title))
        Thread = threading.Thread(target=downloadScript, args=(videoLink, title))
        Thread.start()
    except:
        print("An exception has occurred!")


def getUserInput():
    global videoLink, title

    while(True):
        videoLink = input("Enter the YouTube URL you want to download, type 'list' to see downloaded videos, or type 'return' to leave: ")

        if(videoLink == "list"):
            listOfVideos = []
            for i in os.listdir():
                if i.endswith(".mp4"):
                    listOfVideos.append(i)
            print(listOfVideos)
            continue

        if(videoLink == "return" or not videoLink.startswith(prefix)):
            if(not videoLink.startswith(prefix) and videoLink != "return"):
                print("Please enter a valid YouTube Link or type 'return' to leave")
                continue
            return True

        title = input("Enter the title you want to give to the video or type 'return' to leave: ")

        if(title == 'return' or len(title) < 2):
            if(len(title) < 2 and title != "return"):
                print("Please type a title or make the title longer than TWO characters")
                continue
            return True
        break
    return False

def downloadScript(videoLink, title):
    os.chdir(mainDirectory)
    #os.chdir("./VideosDownloaded")
    os.chdir(videoDownloadFolder)

    os.system("ytDownload.sh {} {}".format(videoLink, title))