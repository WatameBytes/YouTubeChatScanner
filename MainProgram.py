import os
import threading
import subprocess

from CollectChat import ChatScan
from DownloadVideo import RunDownloader
from ComputeData import ComputeRawChatData
from Utilities import PrintFunctions, HelperFunctions
from Editor import EditVideos

PrintFunctions.print_list_of_choices()


while(True):
    os.chdir(HelperFunctions.MainDirectory)
    #print(os.getcwd())

    try:
        #choice = (int(input("Please pick an option. Type '0' to view your options: ")))
        choice = 4

        # Display user choices
        if (choice == 0):
            PrintFunctions.print_list_of_choices()

        # Gather chat data
        elif (choice == 1):
            ChatScan.gather_video_info()

        # Download a YouTube video
        elif (choice == 2):
            RunDownloader.prerequisite_checklist()

        # Turn raw chat data into computed data
        elif (choice == 3):
            ComputeRawChatData.dataProcessing()

        # Create a subclip [REQUIRES CHAT DATA + MP4)
        elif (choice == 4):
            EditVideos.subclip_prerequisite()

        # List number of threads
        elif (choice == 5):
            print("Number of jobs running: {}".format(threading.active_count() - 1))

        # List contents of raw char data, mp4, and computed data
        elif(choice == 6):
            HelperFunctions.printContents(HelperFunctions.RawChatDataDir, ".txt", "[RAW] Chat Data: ")
            HelperFunctions.printContents(HelperFunctions.VideoDownloadedDir, ".mp4", "Video Content: ")
            HelperFunctions.printContents(HelperFunctions.ComputedDataDir, "txt", "Computed Data: ")

        # Open File Explorer
        elif(choice == 7):
            subprocess.Popen('explorer {}'.format(HelperFunctions.MainDirectory))

        # Exit the program
        elif(choice == 8):
            if (threading.active_count() > 1):
                print("You have some programs running in the background!")
                continue
            break

        else:
            PrintFunctions.print_improper_choice()

    except ValueError as e:
        print(e)
        PrintFunctions.print_improper_choice()

    finally:
        user = input("PLACE HOLDER: WILL INPUT {} AFTER YOU TYPE SOMETHING".format(choice))

