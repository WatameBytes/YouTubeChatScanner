import threading
import time

from CollectChat import ChatScan
from DownloadVideo import RunDownloader
from Project.Utilities import PrintFunctions

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
            ChatScan.gather_video_info()

        elif (choice == 2):
            RunDownloader.prerequisite_checklist()

        elif (choice == 3):
            print()

        elif (choice == 4):
            if (threading.active_count() > 1):
                print("You have some programs running in the background!")
                continue

            break

        elif (choice == 5):
            print("Number of jobs running: {}".format(threading.active_count() - 1))

        else:
            PrintFunctions.print_improper_choice()
    except ValueError:
        PrintFunctions.print_improper_choice()