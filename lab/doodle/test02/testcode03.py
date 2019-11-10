import RPi.GPIO as GPIO
import time

REDLEDlist = [4, 17, 18, 27, 22, 23, 24, 25]
GREENLEDlist = [6, 12, 13, 16, 19, 20, 26, 21]

fullLEDlist = [4, 17, 18, 27, 22, 23, 24, 25, 6, 12, 13, 16, 19, 20, 26, 21]

GPIO.setmode(GPIO.BCM)

for i in fullLEDlist:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)


time.sleep(0.5)
count = 1

for i in range(0, 16, 2):
	r = fullLEDlist[i]
	
	GPIO.output(r, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(r, GPIO.LOW)
	time.sleep(0.5)

for i in range(1, 16, 2):
	r = fullLEDlist[i]

	GPIO.output(r, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(r, GPIO.LOW)
	time.sleep(0.5)

#for i in fullLEDlist:
#	if (count % 2 == 1):
#		GPIO.output(i, GPIO.HIGH)
#		time.sleep(0.5)
#		GPIO.output(i, GPIO.LOW)
#		time.sleep(0.5)

GPIO.cleanup() 
		
