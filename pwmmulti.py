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

a.start(90)
b.start(50)
c.start(5)
#sada.stop()

print "starting pwm on pin 17,27,22 with 90 , 50 , 5 percent"                            
sleep(5)

while 1:
	print "pwm inside loop"    
	sleep(0.7)
	a.ChangeDutyCycle(90)
	b.ChangeDutyCycle(50)
	c.ChangeDutyCycle(5)
	print "pwm is 90"
	sleep(0.7)
	a.ChangeDutyCycle(80)
	b.ChangeDutyCycle(60)
	c.ChangeDutyCycle(10)
	print "pwm is 80"
	sleep(0.7)
	a.ChangeDutyCycle(70)
	b.ChangeDutyCycle(70)
	c.ChangeDutyCycle(20)
	print "pwm is 70"
	sleep(0.7)
	a.ChangeDutyCycle(60)
	b.ChangeDutyCycle(80)
	c.ChangeDutyCycle(30)
	print "pwm is 60"
	sleep(0.7)
	a.ChangeDutyCycle(50)
	b.ChangeDutyCycle(90)
	c.ChangeDutyCycle(40)
	print "pwm is 50"
	sleep(0.7)
	a.ChangeDutyCycle(40)
	b.ChangeDutyCycle(98)
	c.ChangeDutyCycle(50)
	print "pwm is 40"
	sleep(0.7)
	a.ChangeDutyCycle(30)
	b.ChangeDutyCycle(0)
	c.ChangeDutyCycle(60)
	print "pwm is 30"
	sleep(0.7)
	a.ChangeDutyCycle(20)
	b.ChangeDutyCycle(10)
	c.ChangeDutyCycle(70)
	print "pwm is 20"
	sleep(0.7)
	a.ChangeDutyCycle(10)
	b.ChangeDutyCycle(20)
	c.ChangeDutyCycle(80)
	print "pwm is 10"
	sleep(0.7)