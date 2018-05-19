#!/usr/bin/python

import datetime
import time

from microdotphat import write_string, set_decimal, clear, show
import requests

temp = None

last_temp = None
last_change_time = None

while True:

    r = requests.get("http://localhost:8367/")

    new_temp_float = float(r.text)

    new_temp = round(new_temp_float, 2)

    if new_temp != temp:
        last_temp = temp
        last_change_time = datetime.datetime.now()
        temp = new_temp

    write_string( "%.2f" % temp + "c", kerning=False)

    show()

    time.sleep(5)


