import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
GPIO.output(5,0)
sleep(3.0)
a = GPIO.PWM(17,1000) 
b = GPIO.PWM(27,1000) 
c = GPIO.PWM(22,1000) 
a.start(5)
b.start(5)
c.start(5)
print "starting pwm on pin 17,27,22 with 90 , 50 , 5 percent"                            
sleep(2)
while 1:

	for i in range (0,100,10):
		print "forward loop" 
		print i   
		sleep(1.5)
		a.ChangeDutyCycle(i)
		b.ChangeDutyCycle(i)
		c.ChangeDutyCycle(i)
	for i in range (100,0,-10):
		print "reverse loop"
		print i    
		sleep(1.5)
		a.ChangeDutyCycle(i)
		b.ChangeDutyCycle(i)
		c.ChangeDutyCycle(i)