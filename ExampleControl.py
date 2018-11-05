import RPi.GPIO as GPIO
import time
import Compass
import GimbalController

# Pins to be used for tilt and pan motors are found in GimbalController.py
# GimbalController.py must be in the same directory to use it


while True:
	
	angle = Compass.getHeading()
	# GimbalController.panGimbal(angle)
	time.sleep(1)

GimbalController.resetGimbal()

GPIO.cleanup()
