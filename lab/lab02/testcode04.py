import RPi.GPIO as GPIO
import time


LEDlist = [4, 17, 18, 27, 22, 23, 24, 25, 6, 12, 13, 16, 19, 20, 26, 21]

GPIO.setmode(GPIO.BCM)

for i in LEDlist:
	GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)


time.sleep(0.5)

for i in range(0, 16, 2):
	r1 = LEDlist[i]
	r2 = LEDlist[i + 1]

	try:
		GPIO.output(r1, GPIO.HIGH)
		GPIO.output(r2, GPIO.HIGH)
		time.sleep(0.5)

		GPIO.output(r1, GPIO.LOW)
		GPIO.output(r2, GPIO.LOW)
		time.sleep(0.5)

	except KeyboardInterrupt:
		pass

GPIO.cleanup()

	
