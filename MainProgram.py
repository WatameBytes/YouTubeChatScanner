import os
import threading
import subprocess

from CollectChat import ChatScan
from DownloadVideo import RunDownloader
from ComputeData import ComputeRawChatData
from Utilities import PrintFunctions, HelperFunctions
from Editor import EditVideos
from ComputeData import KMeans

PrintFunctions.print_list_of_choices()

while(True):
    os.chdir(HelperFunctions.MainDirectory)
    KMeans.k()
    input("Buffer to stop infinite loop")
    continue

    try:
        choice = (int(input("Please pick an option. Type '0' to view your options: ")))

        # Prints out the user choices
        if (choice == 0):
            PrintFunctions.print_list_of_choices()

        # Give a YouTube video link + name ==> get chat data timestamps
        elif (choice == 1):
            ChatScan.gather_video_info()

        # Give a YouTube video link + name ==> Download the video
        elif (choice == 2):
            RunDownloader.prerequisite_checklist()

        # Turn timestamp data into usable data with one of our algorithms
        elif (choice == 3):
            ComputeRawChatData.dataProcessing()

        # TODO: Implement an Algorithm choice and other user choices
        # Create a subclip using computed chat data [REQUIRES CHAT DATA + MP4]
        elif (choice == 4):
            EditVideos.subclip_prerequisite()

        # Print the number of threads
        elif (choice == 5):
            print("Number of jobs running: {}".format(threading.active_count() - 1))

        # TODO: Implement other file paths
        # Print out the contents of a directory
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

        # None of the choices were picked, display the choice again
        else:
            PrintFunctions.print_improper_choice()

    except ValueError as e:
        print(e)
        PrintFunctions.print_improper_choice()

    # except:
    #     print('An exception has occured')
    #     PrintFunctions.print_improper_choice()