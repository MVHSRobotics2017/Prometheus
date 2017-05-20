
import RPi.GPIO as GPIO
import time
def sonar(TRIG,ECHO):
	"""accepts int arrays TRIG and ECHO"""
	ret = [0.0]*len(TRIG)
	if (len(TRIG)!=len(ECHO)):
		raise ValueError("TRIG != ECHO!")
	GPIO.setmode(GPIO.BOARD)
	for pin in TRIG:
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.output(TRIG,0)
	for pin in ECHO:
		GPIO.setup(pin,GPIO.IN)

	time.sleep(0.1)
	print("Starting Measurements...")
	for x in range(0,len(TRIG)):
		print("beggining measurement on sensor:{i}\n\tusing input ({a},{b}).".format(i=x,a=TRIG[x],b=ECHO[x]))
		GPIO.output(TRIG[x],1)
		time.sleep(0.00001)
		GPIO.output(TRIG[x],0)
		while GPIO.input(ECHO[x]) == 0:
			start = time.time()
		while GPIO.input(ECHO[x]) == 1:
			pass
		stop = time.time()
		print("Mark!\tmeasured time= {delta}".format(delta=(stop-start)))
		ret[x] = stop - start
	#print (stop - start) * 17000
		print("adjusted = {adjRet}".format(adjRet = ret[x]*1.7E4))
	GPIO.cleanup()
