import os
import time
import datetime
from pause import until
import astral


# Collect and set up location for sunrise times
a = astral.Astral()
location = a['Columbia']
timezone = location.timezone

# Get actual date information and times for tomorrow's sunrise
dTom = datetime.date.today() #+ datetime.timedelta(days=1)
sun = location.sun(local=True, date=dTom)

# May want to subtract some time, get the before the actual sunrise
dt = sun['sunrise'] - datetime.timedelta(minutes=30)
print(sun['sunrise'])
print(dt)

#Temporary test to make sure everything works
# dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
# print(dt)

# Get files in folder to get next filename
x = int(os.popen('ls "/home/pi/Pictures/pycam/" | wc -l').read())

print(x)
until(dt)
os.system('sudo killall gvfs-gphoto2-volume-monitor')
for i in range(80):
    if i < 9 and i > 0:
        time.sleep(180)
    elif i == 9:
        time.sleep(150)
    elif i > 9:
        time.sleep(10)
    print(datetime.datetime.now())
    os.system('sudo gphoto2 --capture-image-and-download --filename "/home/pi/Pictures/pycam/pic' + str(i + x) + '.jpg"')

