import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
	
# Setup pins that motors are connected to
PanPins = [7,11,13,15]
for pin in PanPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)
TiltPins = [29,31,33,35]
for pin in TiltPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

panAngle = 0
tiltAngle = 0

# Sequence of motor outputs for forward motion
sequence = [ [1, 0, 0, 0],
			 [1, 1, 0, 0],
			 [0, 1, 0, 0],
			 [0, 1, 1, 0],
			 [0, 0, 1, 0],
			 [0, 0, 1, 1],
			 [0, 0, 0, 1],
			 [1, 0, 0, 1] ]
			 
tilt_seq = [ [1, 0, 0, 1],
			 [0, 0, 0, 1],
			 [0, 0, 1, 1],
			 [0, 0, 1, 0],
			 [0, 1, 1, 0],
			 [0, 1, 0, 0],
			 [1, 1, 0, 0],
			 [1, 0, 0, 0] ]
			   
currentStep = 0

# Rotates the camera gimbal in a panning motion.
# Takes in degrees to rotate the camera to [0, 360]
def panGimbal(angle):
	global panAngle
	global currentStep
	if angle < 0 or angle > 360:
		raise ValueError('angle must be between 0 and 360 degrees inclusive')
	panCommand = angle - panAngle
	stepsToGo = panCommand * (4096.0/360.0)
	#stepsToGo = round(stepsToGo, 0)
	#print("Steps to go: "+str(stepsToGo))
	
	# If the direction the gimbal needs to move is positive
	if panCommand > 0:
		
		# Account for last step the motor was on
		stepsTravelled = currentStep
		stepsToGo = stepsToGo + currentStep
		
		# while there are still steps left to go
		while stepsTravelled < stepsToGo: 
			
			currentStep = int(stepsTravelled % 8)
			#print("Current Step: "+str(currentStep))
			
			# Change the pins for every step
			for pin in range(4):
				GPIO.output(PanPins[pin], sequence[currentStep][pin])
			time.sleep(0.001)
			
			stepsTravelled += 1 
			
	# If the direction the gimbal needs to move is negative	
	elif panCommand < 0:
		#while stepsTravelled > stepsToGo:
		# Account for last step the motor was on
		stepsToGo = stepsToGo*-1
		stepsTravelled = stepsToGo + currentStep
		
		# while there are still steps left to go
		while stepsTravelled > 0: 
			
			currentStep = int(stepsTravelled % 8)
			
			# Change the pins for every step
			for pin in range(4):
				GPIO.output(PanPins[pin], sequence[currentStep][pin])
			time.sleep(0.001)
			
			stepsTravelled -= 1 
		
	panAngle = angle

# Tilts the camera to the given angle
# Takes in degrees to rotate the camera to [0, 180]
def tiltGimbal(angle):
	global tiltAngle
	global currentStep
	if angle < 0 or angle > 180:
		raise ValueError('angle must be between 0 and 180 degrees inclusive')
	tiltCommand = angle - tiltAngle
	stepsToGo = tiltCommand * (4096.0/360.0)
	#stepsToGo = round(stepsToGo, 0)
	#print("Steps to go: "+str(stepsToGo))
	
	# If the direction the gimbal needs to move is positive
	if tiltCommand > 0:
		
		# Account for last step the motor was on
		stepsTravelled = currentStep
		stepsToGo = stepsToGo + currentStep
		
		# while there are still steps left to go
		while stepsTravelled < stepsToGo: 
			
			currentStep = int(stepsTravelled % 8)
			#print("Current Step: "+str(currentStep))
			
			# Change the pins for every step
			for pin in range(4):
				GPIO.output(TiltPins[pin], tilt_seq[currentStep][pin])
			time.sleep(0.001)
			
			stepsTravelled += 1 
			
	# If the direction the gimbal needs to move is negative	
	elif tiltCommand < 0:
		#while stepsTravelled > stepsToGo:
		# Account for last step the motor was on
		stepsToGo = stepsToGo*-1
		stepsTravelled = stepsToGo + currentStep
		
		# while there are still steps left to go
		while stepsTravelled > 0: 
			
			currentStep = int(stepsTravelled % 8)
			
			# Change the pins for every step
			for pin in range(4):
				GPIO.output(TiltPins[pin], tilt_seq[currentStep][pin])
			time.sleep(0.001)
			
			stepsTravelled -= 1 
		
	tiltAngle = angle

# Called during gimbal control shutdown to reset the gimbal motors to their origin
# positions.
def resetGimbal():
	panGimbal(0)
	tiltGimbal(0)

