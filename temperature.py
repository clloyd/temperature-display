#!/usr/bin/env python

import colorsys
import signal
import time
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd


temperature = 1

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

while True:
    image = Image.new("RGB", (width, height), (0,0,0))
    draw = ImageDraw.Draw(image)

    offset_left = 0

    draw.text((0, 0), str(temperature), (0,255,0,255), font=font)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]

            unicornhathd.set_pixel(width - x - 1, y, r, g, b)

    unicornhathd.show()
    time.sleep(100)
    temperature + 1

unicornhathd.off()