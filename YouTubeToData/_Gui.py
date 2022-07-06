import PySimpleGUI as sg
from _CollectChat import collectChat

window = None
layout = None
streamer_video_divider = ":"

def display_The_Program():
    global layout
    global window

    # Gui Display box text
    gui_title = 'YouTube comment to data'
    user_display_one = 'YouTube Link?'
    user_display_two = 'nameOfStreamer:VideoName'
    keep_after_submission = True
    # ============================

    layout = [
        [sg.Text(user_display_one)],
        [sg.Input(do_not_clear=keep_after_submission)],
        [sg.Text(user_display_two)],
        [sg.Input(do_not_clear=keep_after_submission)],
        [sg.Button('Submit')]]

    window = sg.Window(gui_title, layout)

def gui():
    try:
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, userInput = window.read()

            # User can close the app
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            link_of_video = userInput[0]

            # userInput[0] is the YouTube link
            if userInput[0] == '':
                raise ValueError("First value can't be empty")

            # Grabs just the video id of a video [www.youtube.com/watch?v={WE WANT THIS PART ONLY}
            video_id = str(userInput[0]).split('=')[1]

            if userInput[1] == '':
                raise ValueError("Second value can't be empty")

            # [Amelia]:NameOfVideo <--- [IS WHAT WE STORE]
            streamer_name = str(userInput[1]).split(streamer_video_divider)[0]


            if not look_for_streamer_videoname_dividier(userInput[1]):
                raise ValueError("You forgot to place {}".format(streamer_video_divider))

            # Amelia:[NameOfVideo] <--- [IS WHAT WE STORE]
            video_name = str(userInput[1]).split(streamer_video_divider)[1]

            # if(video_name == ''):
            #     raise ValueError("Video name can't be empty")

            # YouTube Link --> https://www.youtube.com/watch?v=L30zTyxZ8mo
            # nameOfStreamer:Videoname --> fauna:faunaOnline

            # link_of_video: https://www.youtube.com/watch?v=L30zTyxZ8mo
            # video_id: L30zTyxZ8mo
            # streamer_name: fauna
            # video_name: faunaOnline
            # print("link:{}\nid:{}\nstreamer_name:{}\nvideo_name:{}".format(link_of_video, video_id, streamer_name, video_name))
            sg.popup('Collecting data')
            collectChat(link_of_video, video_id, streamer_name, video_name)
            sg.popup('Complete')
        window.close()

    # The catch statements for out try statements
    except ValueError as error:
        sg.popup_annoying(repr(error))
        gui()
    except IndexError:
        sg.popup_annoying('You forgot to place "="....')
        gui()

# A simple function to check TRUE: contains streamer_video_divider FALSE: doesn't contain streamer_video_divider
def look_for_streamer_videoname_dividier(s):
    try:
        s.index(streamer_video_divider)
        return True
    except ValueError:
        return False