import os

from moviepy.editor import VideoFileClip, concatenate_videoclips
from Utilities import HelperFunctions
from ComputeData.ComputeRawChatData import dataProcessing

# clip1 = VideoFileClip("yoimiya.mp4").subclip(55, 65)
# clip2 = VideoFileClip("ganyu.mp4").subclip(80, 100)
# clip3 = VideoFileClip("yoimiya.mp4").subclip(195, 225)

#combined = concatenate_videoclips([clip1, clip2, clip3])

#combined.write_videofile("combined.mp4")


def subclip_prerequisite():
    print("GATHERING DATA")
    print(os.getcwd())
    print(HelperFunctions.RawChatDataDir)









