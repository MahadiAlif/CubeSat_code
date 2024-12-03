import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL
import csv
import matplotlib.pyplot as plt
from adafruit_lis3mdl import LIS3MDL
from picamera import PiCamera
from time import sleep

i2c = board.I2C()  # uses board.SCL and board.SDA
accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)

def reader() :
    magnetic_value = mag.magnetic
    return magnetic_value
    # Format :  x y z

def capture_pic():


    # Initialize the camera
    camera = PiCamera()

    # Set the resolution (optional)
    camera.resolution = (1024, 768)
    # Capture an image
    vn=time.time()
    vn = str(vn)+".jpg"
    camera.capture(vn)
    # Close the camera
    camera.close()

vvb=[]
elapsed=0
cycles=0
maxV_x=0
maxV_y=0

try:
    while True:
        magnetic_value = reader(),
        maglist = list(magnetic_value)
        xValue=magnetic_value[0][0]+400
        #yValue=magnetic_value[0][1]+400
        while xValue > 380 and xValue <420 :
            capture_pic()
            print(xValue)
            time.sleep(0.3)
        
        
  
      
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Measurement stopped by the user")



