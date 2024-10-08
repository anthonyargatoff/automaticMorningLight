#! /home/anthony/dev/automaticMorningLight/venv/bin/python3

import tinytuya
import time
from dotenv import load_dotenv
import os

load_dotenv()

startBulbPercentage = 1
maxBulbPercentage = 100
duration = 3600 # 1 hour in seconds

l = tinytuya.BulbDevice(os.environ.get('DEVICE_ID'), os.environ.get('DEVICE_IP'), os.environ.get('DEVICE_KEY'), version=3.3)
data = l.status() 
print('Device status: %r' % data)

l.turn_on()
l.set_white_percentage(0,0)
while startBulbPercentage <= 100:
    print(startBulbPercentage)
    l.set_brightness_percentage(startBulbPercentage)
    startBulbPercentage += 1
    time.sleep(duration/100) # run 100 over the duration for gradual wake up

l.turn_off()