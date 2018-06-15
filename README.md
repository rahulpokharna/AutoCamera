# AutoCamera
Project to take pictures automatically, and do some image manipulation using python and gphoto2 on a Raspberry Pi 3.

### What you need
1. Raspberry Pi 3
2. Camera compatible with gphoto2, list here: http://www.gphoto.org/proj/libgphoto2/support.php
3.  Anything additional to set up and maintain the camera position and power to the system.

### Setup
In order to have my camera take pictures from the command line, I used Gphoto2 libraries to do this. Gphoto2 is constantly updated as a command-line controller for digital cameras through the linux OS.
To install, run ` sudo apt-get install gphoto2`
This will take care of the dependencies that are needed. 

The program will be based in Python 3.4, as that is the version I am currently running.
Some additional python packages needed are the Astral package, to take care of sunrise and sunset times. 
This can be installed with ` sudo pip3 install astral`
 The next package needed will be datetime, to take care of the format and retrieval of dates and times. 
 This can be installed with `sudo pip3 install datetime`
 
The rest of the program should run without additional packages. 

### Testing 
To make sure that gphoto2 works properly on your setup, first make sure the camera is turned on and connected to your pi.
Once everything is turned on and set up, on the terminal run the command `gphoto2 --auto-detect`
This should show a list of cameras and USB connections available for gphoto2.
The next command to try would be `gphoto2 --summary`
This will display a summary for all cameras connected to the system.

If you run into an error here regarding not being able to claim the USB port, the run the command `sudo killall gvfs-gphoto2-volume-monitor`
After this, restart your camera and retry the commands. 

The first way to test the system and make it capture the image `gphoto2 --capture-image-and-download`
This would then take the photo, and store it in the location your terminal currently is in. This will be the basis of the program later.


### Major Files
The main files in use will be imageManip.py, to interpret and modify images, currently just to aggregate the brightest pixel over all images passed to it.
 