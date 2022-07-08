import os


url = "https://www.youtube.com/watch?v=AJ6ELAOM5zs"
title = "YowaneHaku"
os.system("ytDownload.sh {} {} &".format(url, title))

