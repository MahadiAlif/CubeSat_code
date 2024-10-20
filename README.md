# CubeTech Hackathon Solutions

This repository contains the solutions developed for the CubeTech Hackathon, organized by the CubeSat Team of Politecnico di Torino in collaboration with Leva. The challenges revolve around simulating a spacecraft's operation using Raspberry Pi, a camera module, an IMU, and other hardware components to solve real-world space problems.

## Problem Overview

CubeTech Hackathon challenged us to solve two primary tasks:

1. **Basic Problem**: 
   - Using the IMU, detect the right moment to capture a photo based on the magnetic field values during the rotation of a simulated satellite.
   - After capturing the image, estimate the distance between the center of the picture and the center of the image using a segmentation algorithm.

2. **Advanced Problem**: 
   - Identify what the camera is looking at from a provided image database.
   - Handle both partial and full painting recognition with constraints on time and energy consumption.

## Equipment

The following equipment was used during the hackathon:
- Raspberry Pi Zero 2W
- Raspberry Pi Camera Module V2
- IMU Adafruit LSM6DSOX + LIS3MDL 9 DOF
- Breadboard and jumpers
- Monitor

## Solution Approach

### Basic Problem
- **Magnetic Field Detection**: A Python script captures the IMU data and calculates the magnetic field to detect the right moment for the photo.
- **Image Segmentation**: After capturing the image, the algorithm calculates the center of the image using the formula:  
  `distance = sqrt((|Xdistance − 1640|)^2 + (|Ydistance − 1232|)^2) / 3280`
  
  This formula computes the pixel-based distance between the center of the image and the captured photo.

### Advanced Problem
- **Image Identification**: A machine learning model identifies paintings from a given database. The identification process prioritizes accuracy, energy consumption, and time efficiency.
  
## Folder Structure
├── BasicProblem │ ├── imu_photo.py # Code for capturing photos based on IMU magnetic field data │ ├── image_segmentation.py # Code for calculating image center │ ├── requirements.txt # Dependencies for running the project ├── AdvancedProblem │ ├── image_identification.py # Code for identifying images from the database │ ├── image_database/ # Folder containing the painting dataset ├── README.md # This file

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cubetech-hackathon-solutions.git
Navigate to the respective challenge directory and install the dependencies:

cd BasicProblem
pip install -r requirements.txt
Run the code:

python imu_photo.py
For the advanced problem, navigate to the AdvancedProblem folder and run the image identification code.

Testing and Scoring
The testing for both problems was conducted in a simulated space environment with magnetic fields and rotating platforms. Points were awarded based on time, energy consumption, and accuracy of image capture and identification.

License
This project is licensed under the MIT License - see the LICENSE file for details.

You can copy this directly into your `README.md` file on GitHub. Just remember to replace the link to the repository with your actual GitHub URL!






