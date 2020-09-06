## Raspi Timelapse (Server)

Prerequisites: python3, ffmpeg, and the [client](https://github.com/reuixiy/raspi-timelapse/tree/master/client).

```sh
# 1. Get images
python3 get-images.py [ip]

# 2. Process images
python3 process-images.py

# 3. Generate video
python3 generate-video.py

# 4. Add audio
python3 add-audio.py audios/example.mp3

# 5. Clean
./clean.sh
```
