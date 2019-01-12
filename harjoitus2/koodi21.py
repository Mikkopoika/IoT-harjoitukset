import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Asetetaan punaisen ledin ulostuloksi pinni 6
GPIO.setup(6, GPIO.OUT)

i = 0
while i < 10:
	GPIO.output(6, 1)
	time.sleep(0.5)
	GPIO.output(6, 0)
	time.sleep(0.5)
	i += 1

GPIO.cleanup()

