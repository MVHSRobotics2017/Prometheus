####
# Author: TheUnkn0wn1
# Function: control Roboclaw motor controller
# Python Version: Python2
###

#Imports
from sys import argv #for command-line paramaters ('Arguments')
from sys import exit #for exiting with status codes
from roboclaw.roboclaw import Roboclaw
from time import sleep
#config
debug=0
port='/dev/ttyACM0'
addr=128
baud=460800
#globals
rc = Roboclaw(port,baud) #init Roboclaw instance
cells =3 #reffering to battery cell count, just for debug reasons...

if(debug):
	print("{hello_world}".format(hello_world="Hello, world!"))#just because :3
	print("Number of arguments={num}".format(num=len(argv)))
	print("ArgList:")
	i=0
	for arg in argv: #prints out each argument in order
		print("\targv[{i}]\t=\t{val}".format(i=i,val=arg))
		i=i+1
#function wrappers, because i don't like their naming convention
def connect():
	return(rc.Open())
def fwLeft(pwr):
	connect()
	return(rc.ForwardM2(addr,pwr))
def fwRight(pwr):
	connect()
	return(rc.ForwardM1(addr,pwr))
def stop():
	ret = [0,0]
	ret[0] = fwLeft(0)
	ret[1] = fwRight(0)
	return(ret)
def getVolt():#this is a debug function!
	"""reads battery volatage"""
	connect()
	voltage=(rc.ReadMainBatteryVoltage(addr))
	volts=voltage[1]/10.#to scale into volts
	cellV = volts/cells#so we get an aprox Volt per cell (debug)
	if(debug):
		print("main battery voltage: raw=\t{raw},\tCell=\t{cell}".format(raw=volts,cell=cellV))
	return([volts,cellV])

if(len(argv)<=1): #if no no arguments are given
	raise ValueError("Not enough arguments!")
else:#if we have an argument, lets figure out the command we received...
	x=argv[1] #we only care about the first arg here as it is our command
	if(x == "-default"):
		fwLeft(30)
		fwRight(30)
	elif(x == "-fl"):#forward left side motors set to argv[2]
		fwLeft(int(argv[2]))
	elif(x == "-stop"):
		stop()
	elif(x =="-fr"):#forward right side motors set to argv[2]
		fwRight(int(argv[2])) #the arg needs to be cast from str to int
	elif(x=="-forward"):
		fwRight(int(argv[2]))
		sleep(1./16.) #attempt to remidy motor desync issue
		fwLeft(int(argv[2]))
	elif(x=="-volt" or x=="-v"):
		if(len(argv)>=2 and x == "r"): #if i want it to repeat
			while(1):
				print(getVolt())
				sleep(.1)
		else:
			print(getVolt())
	elif(x=="--run"):#Run test
		if(len(argv))<=2:
			raise ValueError("This argument requires an additional argument.")
		getVolt()
		fwRight(45)
		fwLeft(45)
		sleep(int(argv[2]))
		stop()
	else: #if the comand is not recognized, ignore it
		print("unknown command: {cmd}".format(cmd=x))
		exit(42)
