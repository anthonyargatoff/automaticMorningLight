import tinytuya
import time
from dotenv import load_dotenv
import os

load_dotenv()

startBulbPercentage = 0
maxBulbPercentage = 100
duration = 3600 # 1 hour in seconds

l = tinytuya.BulbDevice(os.environ.get('DEVICE_ID'), os.environ.get('DEVICE_IP'), os.environ.get('DEVICE_KEY'), version=3.3)

l.set_white_percentage(0,0)
while startBulbPercentage <= 100:
    l.set_brightness_percentage(startBulbPercentage)
    startBulbPercentage += 1
    time.sleep(duration/100) # run 100 over the duration for gradual wake up