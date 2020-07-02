# Usage: python3 add-audio.py example.mp3

import os, sys

audio = sys.argv[1]

os.system("ffmpeg -i build/output.mp4 -i " + "'" + audio + "'" + " -c:v copy -c:a aac -shortest build/timelapse.mp4")
