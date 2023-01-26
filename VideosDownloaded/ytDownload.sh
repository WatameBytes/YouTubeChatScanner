#!/bin/bash
#yt-dlp --embed-thumbnail -S res,ext:mp4:m4a --recode mp4 $1 -N 4 -o './'$2'.%(ext)s'
#yt-dlp --embed-thumbnail -S res,ext:mp4:m4a --recode-video MP4 $1 -N 4 -o './'$2'.%(ext)s'

# Below gave us a good video but not audio
# yt-dlp --ignore-config -f bestvideo+bestaudio --merge-output-format mp4 $1 -N 4 -o './'$2'.%(ext)s'
yt-dlp bestvideo+bestaudio --recode-video mp4 $1 -N 4 -o './'$2'.%(ext)s'



# Potential
#yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
echo "DONE"
