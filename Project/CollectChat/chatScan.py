import os.path
import threading
import os

import pytchat
import json

from pathlib import Path

# from Project.Utilities.PrintFunctions import print_current_queue
from os.path import exists

videoId = int()
chat = None
rawDataFolder = './RawYoutubeChatData\\'
isKick = False
fileInstance = None
nameOfTextFile = None

def gather_video_info():
    global videoId
    global isKick
    global fileInstance
    global nameOfTextFile
    global choiceOneBuffer

    isKick = False

    youtubeVideoLinkParser()
    if(isKick):
        return

    fileNameParser()
    if (isKick):
        return

    Thread = threading.Thread(target=dataCollector, args=(nameOfTextFile, fileInstance, chat, ))
    Thread.start()



def dataCollector(nameOfTextFile, fileInstance, chat):

    print("Collecting data\n")

    while chat.is_alive():
        for c in chat.get().items:
            obj = c.json()
            obj2 = json.loads(obj)
            fileInstance.write(("{}".format(obj2['elapsedTime']) + "\n"))
    fileInstance.close()

    print('\nCompleted: Data saved in {}'.format(nameOfTextFile))

def checkIfEmpty(userInput, errorMessage):
    if(len(userInput) == 0):
        print(errorMessage)
        return True
    return False

def youtubeVideoLinkParser():
    global videoId
    global chat
    global isKick

    videoLink = input("Please enter the video URL or type 'return' to leave: ")

    tempLink = videoLink.lower()

    if (checkIfEmpty(videoLink, "We need a YouTube link!") or tempLink == "return"):
        isKick = True
        return

    try:
        videoId = videoLink.split("=")[1]
        chat = pytchat.create(videoId)

    except IndexError:
        isKick = True
        print("List index out of range! Please enter a valid YouTube Link!")

    except TypeError:
        isKick = True
        print("Please enter a valid YouTube link")

    except pytchat.exceptions.InvalidVideoIdException as pychatError:
        isKick = True
        videoId = "return"
        print(pychatError)

    except:
        print("Wildcard Error Occured")

def fileNameParser():
    global isKick
    global rawDataFolder
    global fileInstance
    global nameOfTextFile

    while (True):
        nameOfTextFile = input("Name the file, type 'list' to view all the current files, or type 'return' to leave: ")

        if (nameOfTextFile == "list"):
            res = []
            for rawDataPath in os.listdir(rawDataFolder):
                if (os.path.isfile(os.path.join(rawDataFolder, rawDataPath))):
                    res.append(rawDataPath + ".txt")
            print(res)
            continue

        elif (checkIfEmpty(nameOfTextFile, "Please enter a file name!") or nameOfTextFile == "return"):
            isKick = True
            return

        elif(os.path.exists(rawDataFolder + nameOfTextFile)):
            print("A file with {} already exist! Please pick a different name!".format(nameOfTextFile))
            continue

        break

    fileInstance = open(rawDataFolder + nameOfTextFile, 'w')