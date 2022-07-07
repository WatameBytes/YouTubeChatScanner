from CollectChat import chatScan
import time
import threading

# def getChatFrequencyFromYoutubeVideo():
#     chatScan.dataCollector(videoOrFileNameEntry, youtubeLinkEntry)

choiceOneBuffer = False
choiceTwoBuffer = False
choiceThreeBuffer = False

def getChatData(test):
    global choiceOneBuffer
    choiceOneBuffer = True
    print("Getting chat data...")
    print( "\n" + test + "\n")
    time.sleep(4)
    print("\nGot Chat Data")


def downloadVideo():
    print("Downloading YouTube Video")

def computeChatData():
    print("Computing Chat Data")


while(True):
    print("1: Get Chat Data\n2: Download YouTube Video\n3: Compute Chat Data")
    choice = (int(input("Please pick a number: ")))
    if(choice == 1):
        if(choiceOneBuffer):
            print("Already downloading chat data")
        else:
            #test = "PASSED AN ARG"
            #Thread1 = threading.Thread(target=getChatData, args=(test, ))
            Thread1 = threading.Thread(target=getChatData)
            Thread1.start()






