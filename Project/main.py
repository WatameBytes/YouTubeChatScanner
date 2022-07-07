from CollectChat import chatScan
import time
import threading

# def getChatFrequencyFromYoutubeVideo():
#     chatScan.dataCollector(videoOrFileNameEntry, youtubeLinkEntry)

choiceOneBuffer = False
choiceTwoBuffer = False
choiceThreeBuffer = False

def getChatData():
    global choiceOneBuffer
    choiceOneBuffer = True
    print("Getting chat data...")
    time.sleep(4)
    print("\nGot Chat Data")


def downloadVideo():
    print("Downloading YouTube Video")

def computeChatData():
    print("Computing Chat Data")


while(True):
    print("1: Get Chat Data\n2: Download YouTube Video\n3: Compute Chat Data\n4: Exit\n5: Current Threads")
    choice = (int(input("Please pick a number: ")))

    if(choice == 1):
        if(choiceOneBuffer):
            print("Already downloading chat data")
        else:
            Thread1 = threading.Thread(target=getChatData)
            Thread1.start()

    elif(choice == 2):
        print()

    elif(choice == 3):
        print()
    elif(choice == 4):
        if(not choiceOneBuffer and not choiceTwoBuffer and not choiceThreeBuffer):
            print("Exiting the program")
            break
        else:
            print("You have some programs running in the background!")

    elif(choice == 5):
        print("===================")
        print("Getting Chat Data: {}".format(choiceOneBuffer))
        print("Downloading Video: {}".format(choiceTwoBuffer))
        print("Computing Chat Data: {}".format(choiceThreeBuffer))
        print("================\n")
    else:
        print("Please type 1, 2, or 3")




