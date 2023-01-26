#!/bin/bash
# Original Code, but downloaded AV01 videos, which Adobe doesn't accept
#yt-dlp --embed-thumbnail -S res,ext:mp4:m4a --recode mp4 $1 -N 4 -o './'$2'.%(ext)s'


#yt-dlp --embed-thumbnail -S res,ext:mp4:m4a --recode-video MP4 $1 -N 4 -o './'$2'.%(ext)s'

# Below gave us a good video BUT no audio
# yt-dlp --ignore-config -f bestvideo+bestaudio --merge-output-format mp4 $1 -N 4 -o './'$2'.%(ext)s'

# This resolved the issue and doesn't give us a AV1
yt-dlp bestvideo+bestaudio --recode-video mp4 $1 -N 4 -o './'$2'.%(ext)s'

echo "DONE"
