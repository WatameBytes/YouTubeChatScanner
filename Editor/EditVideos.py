import os
import threading
from itertools import islice

from moviepy.editor import VideoFileClip, concatenate_videoclips
from Utilities import HelperFunctions, PrintFunctions
from ComputeData.ComputeRawChatData import dataProcessing

DATA_SPLITTER = 30
NUM_OF_LINES = -abs(35)
VIDEO_SPLITTER = 45


def createClip(seconds_timestamp, clip, name):
    START_VIDEO = clip.start
    END_VIDEO = clip.end

    list_of_clips = []

    for i in seconds_timestamp:
        try:
            lower_bound = (i - VIDEO_SPLITTER) if (i - VIDEO_SPLITTER) > START_VIDEO else START_VIDEO
            upper_bound = (i + VIDEO_SPLITTER) if (i + VIDEO_SPLITTER) < END_VIDEO else END_VIDEO
            list_of_clips.append(clip.subclip(lower_bound, upper_bound))
        except: pass


    combined_clips = concatenate_videoclips(list_of_clips)

    combined_clips.write_videofile(HelperFunctions.ClippedVideo + "/" + name + "_COMBINED.mp4")


def subclip_prerequisite():

    seconds_timestamp = user_selects_data_to_convert_to_seconds()
    if(not seconds_timestamp):
        return

    clip, RawVideoFile, name = user_selects_video_to_clip()

    if (not clip):
        return
    Thread = threading.Thread(target=createClip, args=(seconds_timestamp, clip, name, ))
    Thread.start()

def user_selects_video_to_clip():
    RawVideoFile, name = files_displayed_to_user_and_user_selects_file(HelperFunctions.VideoDownloadedDir, "mp4")
    if(not RawVideoFile):
        return False

    clip = VideoFileClip(RawVideoFile.name)
    return clip, RawVideoFile, name


def user_selects_data_to_convert_to_seconds():
    RawChatDataFile, name = files_displayed_to_user_and_user_selects_file(HelperFunctions.RawChatDataDir, "txt")
    if(not RawChatDataFile):
        return False

    # Turn the File into a dictionary
    data_dict = convert_raw_time_data_to_dictionary(RawChatDataFile)
    split_dict = group_dict_values_by_splitter(data_dict, DATA_SPLITTER)
    seconds_timestamp = []
    split_dict = sorted(split_dict.items(), key=lambda x: x[1])
    sort_dict = dict(split_dict)
    for i in range(-1, NUM_OF_LINES - 1, -1):
        try:
            #print(list(sort_dict)[i])
            seconds_timestamp.append(HelperFunctions.string_time_to_seconds(list(sort_dict)[i]))
        except:
            pass
    seconds_timestamp.sort()
    return seconds_timestamp


def files_displayed_to_user_and_user_selects_file(file_directory, extension):
    print(file_directory)

    list_of_contents = HelperFunctions.getContents(file_directory, extension)

    for index, value in enumerate(list_of_contents):  # Display the files in the directory with a choice number
        print("\t[{}]: {}".format(index, value))

    try:
        i = input("Please select the text-file you want to compute: ")
    except:
        print("An exception was found!")
        return False

    try:  # Attempt to open the file the user selected
        File = open(file_directory + "\\" + list_of_contents[int(i)], "r")
    except:
        print("{} isn't a valid choice".format(i))
        return False

    name = list_of_contents[int(i)].split(".")[0]

    return File, name


def convert_raw_time_data_to_dictionary(file):
    dict_with_the_raw_time_data = dict()

    for line in file:  # Loop through each line of the file
        line = line.strip()  # Remove the leading spaces and newline character
        line = line.lower()  # Convert characters to lowercase
        # line = line.translate(line.maketrans("", "", string.punctuation)) # Removes the ':'
        words = line.split(" ")  # Split the line into words

        for word in words:  # Iterate over each word in line
            if (HelperFunctions.check_negative_sign(word)):
                pass  # Looks for a negative value and skips it

            elif word in dict_with_the_raw_time_data:  # Check if the word is already in dictionary
                dict_with_the_raw_time_data[word] = dict_with_the_raw_time_data[
                                                        word] + 1  # Increment count of word by 1

            else:
                dict_with_the_raw_time_data[word] = 1  # Add the word to dictionary with count 1

    return dict_with_the_raw_time_data


# We get splitter amount of values --> add them up --> place it
def group_dict_values_by_splitter(dict, splitter):
    new_dict = {}

    for item in chunks(dict, splitter):
        new_dict[list(item.keys())[0]] = sum(item.values())
    return new_dict


def chunks(data, SIZE=1000000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}
