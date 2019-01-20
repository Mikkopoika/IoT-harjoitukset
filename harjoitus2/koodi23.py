import RPi.GPIO as GPIO
import time

LEDAP=16
LEDAK=20
LEDAV=21
LEDJP=23
LEDJV=24
PAINIKE=6
GPIO.setmode (GPIO.BCM)
GPIO.setup (LEDAP, GPIO.OUT)
GPIO.setup (LEDAK, GPIO.OUT)
GPIO.setup (LEDAV, GPIO.OUT)
GPIO.setup (LEDJP, GPIO.OUT)
GPIO.setup (LEDJV, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)

loppu = time.time() + 40
while time.time() < loppu:
	
	GPIO.output(LEDAV, 1)
	GPIO.output(LEDJP, 1)
	if (GPIO.input (PAINIKE)):
		GPIO.output(LEDAV, 0)
		GPIO.output(LEDAK, 1)
		time.sleep(1)
		GPIO.output(LEDAK,0)
		GPIO.output(LEDAP,1)
		GPIO.output(LEDJP,0)
		GPIO.output(LEDJV,1)
		time.sleep(4)
		GPIO.output(LEDJV,0)
		GPIO.output(LEDJP,1)
		time.sleep(0.5)
		GPIO.output(LEDAK, 1)
		time.sleep(0.5)
		GPIO.output(LEDAP,0)
		GPIO.output(LEDAK,0)
		GPIO.output(LEDAV,1)
	time.sleep (0.1) # ilman tata prossukaytto 100%

GPIO.cleanup ()
