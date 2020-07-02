# Usage: python3 get-images.py [ip]
#    eg: python3 get-images.py 192.168.1.2

import os, sys, time

ip = sys.argv[1]
url = 'http://' + ip + ':8080/static/out.jpg'

while True:
    os.system('wget ' + url + ' -P images/raw/')
    time.sleep(10)
