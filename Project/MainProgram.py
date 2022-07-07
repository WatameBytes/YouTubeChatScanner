import threading

from CollectChat import chatScan
import time
from Project.Utilities import PrintFunctions

# def getChatFrequencyFromYoutubeVideo():
#     chatScan.dataCollector(videoOrFileNameEntry, youtubeLinkEntry)

choiceOneBuffer = False
choiceTwoBuffer = False
choiceThreeBuffer = False

def get_chat_data():
    global choiceOneBuffer
    choiceOneBuffer = True

    print("Getting chat data...")
    time.sleep(4)
    print("\nGot Chat Data")

def download_video():
    print("Downloading YouTube Video")

def compute_chat_data():
    print("Computing Chat Data")


PrintFunctions.print_list_of_choices()

while(True):

    try:
        choice = (int(input("Please pick an option. Type '0' to view your options: ")))
        if (choice == 0):
            PrintFunctions.print_list_of_choices()

        elif (choice == 1):
            chatScan.gather_video_info()

        elif (choice == 2):
            print("Option 2")

        elif (choice == 3):
            print()

        elif (choice == 4):
            if (threading.active_count() > 1):
                print("You have some programs running in the background!")
                continue

            break

        elif (choice == 5):
            PrintFunctions.print_current_queue(choiceOneBuffer, choiceTwoBuffer, choiceThreeBuffer)

        else:
            PrintFunctions.print_improper_choice()
    except ValueError:
        PrintFunctions.print_improper_choice()