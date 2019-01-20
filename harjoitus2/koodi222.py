import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Luetaan pinnissa 12 kiinni olevaa PIR sensoria.
GPIO.setup(12, GPIO.IN)

loppu = time.time() + 10
while time.time() < loppu:
    i=GPIO.input(12)
    if i==0:
        print "Ei havaita liiketta"
        time.sleep(0.1)
    elif i==1:
        print "Liiketta havaittu"
        time.sleep(0.1)

GPIO.cleanup()
