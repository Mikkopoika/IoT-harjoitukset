#!/usr/bin/python

from picamera import PiCamera
from time import sleep

camera = PiCamera()

#Ottaa kuvan 10 sekunnin valein palvelimen html-kansioon.
#while (0<1):
#	camera.capture('/home/pi/Pictures/image.jpg')
#	sleep(10)
	
#ottaa huonolaatuista videota 15s.
camera.resolution = (128,128)
camera.start_recording('/home/pi/video.h264')
sleep(15)
camera.stop_recording()
	
	
