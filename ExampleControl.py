import RPi.GPIO as GPIO
import time
import GimbalController

# Pins to be used for tilt and pan motors are found in GimbalController.py
# GimbalController.py must be in the same directory to use it


GimbalController.panGimbal(90)
time.sleep(2)
GimbalController.tiltGimbal(90)
time.sleep(2)
GimbalController.panGimbal(45)
time.sleep(2)
GimbalController.tiltGimbal(180)
time.sleep(2)
GimbalController.panGimbal(230)
time.sleep(2)

GimbalController.resetGimbal()

GPIO.cleanup()
