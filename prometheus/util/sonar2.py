import RPi.GPIO as GPIO
import sonarLib as sonar
from time import sleep
while(1):
	print(sonar.get_distance())
	sleep(.125/2.)
