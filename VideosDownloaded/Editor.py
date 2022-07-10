from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("yoimiya.mp4").subclip(55, 65)
clip2 = VideoFileClip("ganyu.mp4").subclip(80, 100)
clip3 = VideoFileClip("yoimiya.mp4").subclip(195, 225)

combined = concatenate_videoclips([clip1, clip2, clip3])

combined.write_videofile("combined.mp4")