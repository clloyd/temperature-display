#!/usr/bin/python

import colorsys
import signal
import time
import random
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd

import requests

# Use `fc-list` to show a list of installed fonts on your system,
# or `ls /usr/share/fonts/` and explore.

FONT = ("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 14)

# sudo apt install fonts-droid
# FONT = ("/usr/share/fonts/truetype/droid/DroidSans.ttf", 12)

# sudo apt install fonts-roboto
# FONT = ("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf", 12)



unicornhathd.rotation(0)
unicornhathd.brightness(1.0)

width, height = unicornhathd.get_shape()

font_file, font_size = FONT

font = ImageFont.truetype(font_file, font_size)

text_width, text_height = width, 7

def pickColour(temp):
    colours = {
        18: (11, 36, 250, 255),
        19: (38, 150, 190, 255),
        20: (42, 252, 130, 255),
        21: (42, 252, 130, 255),
        22: (72, 210, 90, 255),
        23: (100, 169, 55, 255),
        24: (100, 169, 55, 255),
        25: (141, 185, 55, 255),
        26: (224, 173, 45, 255),
        27: (224, 173, 45, 255),
        28: (245, 144, 37, 255),
        29: (245, 144, 37, 255), 
        30: (246, 94, 36, 255), 
        31: (246, 94, 36, 255),
        32: (248, 40, 34, 255)
    }

    if temp < 18:
        return colours[18]

    if temp > 32:
        return colours[32]

    return colours[temp]


temp = 15

while True:

    # r = requests.get("http://localhost:8367/")

    # temp = float(r.text)

    image = Image.new("RGB", (width, height), (0,0,0))
    draw = ImageDraw.Draw(image)

    offset_left = 0

    draw.text((0, 0), str(round(temp, 0)), pickColour(temp), font=font)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]

            unicornhathd.set_pixel(width - x - 1, y, r, g, b)

    unicornhathd.show()
    time.sleep(1)

    temp = temp + 1

    if temp > 35:
        temp = 15

unicornhathd.off()