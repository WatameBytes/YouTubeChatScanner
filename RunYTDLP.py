import os

# yt-dlp -F https://www.youtube.com/watch?v=rRgNdywle_0

url = "https://www.youtube.com/watch?v=rRgNdywle_0"
os.system("ytDownload.sh {link}".format(link = url))
