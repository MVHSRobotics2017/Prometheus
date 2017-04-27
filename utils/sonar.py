###
# File: sonar.py
# function: act as an interface with a HC-SR04 Ultrasonic
##
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #sets pin numbering
def isArray(obj):
	"""tests if obj is a list"""
	if(type(obj)==list):
		return(1)
	else:
		raise TypeError("Function requires list.")

class sonar(trigger,echo):
	"""docstring for sonar"""
	def __init__(self, arg):
		super(sonar, self).__init__()
		self.arg = arg
		if(isArray(trigger) and isArray(echo)):
			self.pinTrigger = trigger #must be arrays!
			self.pinEcho = echo #must be arrays!
		for pin in self.pinTrigger:#set up each trigger pin
			GPIO.setup(pin,GPIO.OUT)
		for pin in self.pinEcho:#set up each echo pin
			GPIO.setup(pin,GPIO.IN)


