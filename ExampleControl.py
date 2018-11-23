import RPi.GPIO as GPIO
import time
#import GimbalController
import Compass

# Pins to be used for tilt and pan motors are found in GimbalController.py
# GimbalController.py must be in the same directory to use it

while 1:
	angle = Compass.getHeading()
	print ("HEADING: %5.2f" % (angle))
	#GimbalController.panGimbal(180)
	#GimbalController.tiltGimbal(45)
	time.sleep(0.05)

#GimbalController.resetGimbal()
#GPIO.cleanup()
