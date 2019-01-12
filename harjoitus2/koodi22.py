import RPi.GPIO as GPIO

#Asetetaan nappi sisääntuloksi pinniin 5
GPIO.setup(5, GPIO.IN)

#Asetetaan punaisen ledin ulostuloksi pinni 6
GPIO.setup(pin, GPIO.OUT)

if GPIO.input(5)
	GPIO.output(6) = true
else 
	GPIO.output(6) = false

