import os, glob
from PIL import Image, ImageFont, ImageDraw

images = glob.glob('images/raw/*')

for image in images:
    image = Image.open(image)

    date_taken = image._getexif()[36867]
    str_time = date_taken.replace(':', '-').replace(' ', '-').split('-')

    year = str_time[0]
    month = str_time[1]
    day = str_time[2]
    hour = str_time[3]
    minute = str_time[4]
    second = str_time[5]

    date_time = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second

    font = ImageFont.truetype('fonts/SourceCodePro-Regular.ttf', 20)

    img_width, img_height = image.size
    x = 100
    y = img_height - 100

    draw = ImageDraw.Draw(image)
    draw.text((x, y), date_time, '#fff', font=font)

    new_file_path = os.path.join('images/processed', date_time + '.jpg')
    image.save(new_file_path)
