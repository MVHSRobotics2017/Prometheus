import RPi.GPIO as gpio
from time import sleep
import time
trigger=20
echo=21
#gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(trigger,gpio.OUT)
gpio.setup(echo,gpio.IN)

def read(x,y):
	"""takes trigger x and echo y"""
	gpio.output(x,gpio.LOW)
	sleep(5./1000000.)
	gpio.output(x,gpio.HIGH)
	sleep(5./1000000.)
	gpio.output(x,gpio.LOW)
	inStart=0.0
	inEnd=0.0
	while(gpio.input(y)==0):
#		print("ping?")
		inStart = time.time() #reset timer waiting for pulsein
	while(gpio.input(y)):
		pass
#		print("pong!")
	inEnd = time.time() #wait for pulse to end
	delta=inEnd-inStart
	dist=delta/58.2
	print("inStart={x}\tend={y}\tdelta={z}".format(x=inStart,y=inEnd,z=delta))
	return delta

try:
	print("foo?")
	while(1==1):
		print("bar!")
		mea = read(trigger,echo)
		print("obersved value:\t{val}".format(val=mea))
		sleep(1)
except Exception as e:
	print("an exception occured!")
	print(e)
	gpio.cleanup()
	raise e
print("hello world!")
