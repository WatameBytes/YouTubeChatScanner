
## Documentation

### Folders

#### ClippedVideos - The output for Editor > EditVideos.py
- <NameOfFile.mp4>_COMBINED.mp4
- Videos that have been clipped using the FillerGroup algorithm.

#### CollectChat - ChatScan.py
- Allows you to insert a YouTube link and have it scan it's archived chat for timestamps that will be placed in the RawYouTubeChatData folder

#### ComputeData

- ComputeHelperFunction.py: Helper functions used in our algorithm code.

- ComputeRawChatData.py: A file that allows us to call all three algorithms

##### Algorithm - How chat data gets computed
- [Preferred] FillerGroup: Creates timestamps from the **beginning** of the video to the **end** of the video. Count each chat timestamp instance. 
    Allowing us to group by SECONDS instead of just pure groups. Implemented a STREAM OFFSET variable. The only algorithm with an offset variable.
- GroupCount: **ONLY** look at timestamps that **occured** and count only those chat timestamp instances. Allowing us to group by occurance.
- PureCount: **NO GROUPING**. Will show us that timestamp occured the most.

#### DataComputed - Output for our Algorithms

##### FillerData - Output for FillerGroup Algorithm
##### GroupData - Output for GroupCount Algorithm
##### PureData - Output for PureCount Algorithm

#### DownloadVideo - Python Script to run ytDownload.sh

#### Editor - EditVideos.py
- Requires a CLEANED chatdata that appears after you run ComputeData
- Requires a downloaded YouTube video

- Using the FillerGroup Algorithm, we can turn timestamps into seconds and allow moviepy to create clips

#### RawYoutubeChatData
- RAW: Will be a file full of timestamps as is. Which includes timestamps from prechat.
- CLEANED: Negative values are removed and timestamps are normalized.

#### Utilities - Functions and Directorys used throughout the program
- HelperFunctions.py: Contains our splitters for our dictionary, how many lines we want to write, stream delay offset, 
    a round down value that makes timestamps multiples of that variable, paths for our folders, and other useful
        functions.

- PrintFunctions.py: Print functions

#### VideoDownloaded - Output for DownloadVideo > RunDownloader.py

### Main Directory

#### MainProgram.py - The main file for our program

#### requiements.txt - Text file containing the needed modules to run our program

