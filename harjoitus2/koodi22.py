import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

#Asetetaan nappi sisaantuloksi pinniin 5
GPIO.setup(5, GPIO.IN)

#Asetetaan punaisen ledin ulostuloksi pinni 6
GPIO.setup(6, GPIO.OUT)


loppu = time.time() + 10
while time.time() < loppu:
	GPIO.output(6, GPIO.input (5))
	time.sleep (0.1) # ilman tata prossukaytto 100%

GPIO.cleanup ()
