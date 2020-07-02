import os

os.system("ffmpeg -r 24 -pattern_type glob -i 'images/processed/*.jpg' -s hd1080 -vcodec libx264 build/output.mp4")
