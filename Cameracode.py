from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

# Set the resolution (optional)
camera.resolution = (1024, 768)

# Capture an image
camera.capture('imageT.jpg')



# Close the camera
camera.close()

