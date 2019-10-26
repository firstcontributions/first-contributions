import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
while 1:
	if GPIO.input(24)==0:
		GPIO.output(17,1)
		GPIO.output(27,0)
		print "Switch is off :)"
		sleep(0.6)
		GPIO.output(17,0)
		GPIO.output(27,1)
		print "Switch is off :)"
		sleep(0.6)
	else:
		GPIO.output(17,1)
		GPIO.output(27,1)
		print "Switch is ON"
		sleep(0.1)
		GPIO.output(17,0)
		GPIO.output(27,0)
		print "Switch is ON"
		sleep(0.1)
