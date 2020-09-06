import os, time

while True:
    os.system('raspistill --nopreview -w 1920 -h 1080 -rot 180 -o static/out.jpg')
    time.sleep(10)
