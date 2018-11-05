# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()
heading = 0.0

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')

maxheading = 0.0
minheading =360.0
#runtimer = 0.0

t_end = time.time() + 60*1;

while time.time() < t_end:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
    accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))

    heading = (math.atan2(mag_y,mag_x)*180)/3.14159;

    if heading < 0:
     
      heading = heading + 360.0
     
    if heading < minheading:
        minheading = heading;
        
    if heading > maxheading:
        maxheading = heading;    
  
    print("Compass Heading: ");
    #Serial.println("Heading x: ",headingx,"Heading y:" headingy,"Heading z:" headingz);
    print(heading);
    print("/nMax Heading: ");
    print(maxheading);
    print("/nMin Heading: ");
    print(minheading);
    
    #runtimer = runtimer + .5;
    
    #print("/nRun Timer: ");
    #print(runtimer);
    
time.sleep(2);
print("/n/n/nTHE CALIBRATION PERIOD IS COMPLETE.  IT IS NOW TIME FOR REAL MEASUREMENTS./n/n/n");
time.sleep(2);
    
# We will now calculate the scale factor.
scalefactor = 360/(maxheading-minheading);

#We will now output actual headings.

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
    accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))

    
    # Wait half a second and repeat.
    time.sleep(0.5)

    heading = (math.atan2(mag_y,mag_x)*180)/3.14159;

    if heading < 0:
     
      heading = heading + 360.0

    heading = (heading-minheading)*scalefactor;
    
    if heading < 0:
     
      heading = 0;
      print("Calibration Issues");
      
    if heading > 360:
     
      heading = 360;
      print("Calibration Issues");
      
    print("Compass Heading: ");
    #Serial.println("Heading x: ",headingx,"Heading y:" headingy,"Heading z:" headingz);
    print(heading);
   
