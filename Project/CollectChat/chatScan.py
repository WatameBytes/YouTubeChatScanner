import pytchat
import json

def dataCollector(fileOrVideoName, youtubeLink):
    if(len(fileOrVideoName) == 0 or len(youtubeLink) == 0):
        if(len(fileOrVideoName) == 0):
            print("We need a file name!")
            return
        print("We need a YouTube link!")
        return
    video_id = str(youtubeLink).split('=')[1]
    chat = pytchat.create(video_id)
    file = open(str(fileOrVideoName), 'w')

    print("Video ID: {} has started collecting chat data".format(youtubeLink))
    print("Collecting data")

    while chat.is_alive():
        for c in chat.get().items:
            obj = c.json()
            obj2 = json.loads(obj)
            file.write(("{}".format(obj2['elapsedTime']) + "\n"))
    file.close()

    print("Video ID: {} has finished collecting chat data".format(video_id))
    print('nameOfSaveFile: {}'.format(fileOrVideoName))


    print(video_id)


