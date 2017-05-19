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
connected = 0 #bool if roboclaw has already run connect()

class status(object):
	"""docstring for status"""
	success = "ok"
	error = "err"
	deliminator = ';'
		

deliminator = ';'
success = "done" #successful commands will start with this prefix
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
	global connected
	if(connected == 0):#if we haven't connected already
		#global connected
		connected = 1
		if(debug):
			print("Opening connection now.")
		ret = rc.Open()
		try:
			rc.ReadVersion(addr)
		except AttributeError as e:
			returnStatus(1,"AttributeError, check if roboclaw is online.")
			return(None)
	else:
		return(ret)
def fwLeft(pwr):
	ret = connect()
	if type(ret)!=type(None): #error check
		pass
	else:
		returnStatus(1,"command: fwLeft failed.")
		return(-1)
	return(rc.ForwardM2(addr,pwr))
def fwRight(pwr):
	ret = connect()
	if type(ret)!=type(None): #error check
		pass
	else:
		returnStatus(1,"command: fwRight failed.")
		return(-1)
	return(rc.ForwardM1(addr,pwr))
def duty(cycle):
	ret = connect()
	if type(ret)!=type(None): #error check
		cycle = cycle*10**3
		rc.DutyM1M2(addr,cycle,cycle)
		#rc.DutyM2(adr,cycle)
	else:
		returnStatus(1,"command: duty failed.")
		return(-1)
def mixed(pwrA,pwrB):
	ret = connect()
	if type(ret)!=type(None): #error check
		rc.DutyM1(addr,pwrA)
		rc.DutyM2(addr,pwrB)
	else:
		returnStatus(1,"command: mixed failed.")
		return(-1)
def stop():
	ret = [0,0]
	ret[0] = fwLeft(0)
	ret[1] = fwRight(0)
	return(ret)
def getVolt():#this is a debug function!
	"""reads battery volatage"""
	ret = connect()
	if (type(ret)!=type(None)):
		voltage=(rc.ReadMainBatteryVoltage(addr))
		volts=voltage[1]/10.#to scale into volts
		cellV = volts/cells#so we get an aprox Volt per cell (debug)
		if(debug):
			print("main battery voltage: raw=\t{raw},\tCell=\t{cell}".format(raw=volts,cell=cellV))
		return([volts,cellV])
	else:
		returnStatus(1,"unable to read voltage")
def getVersion():
	try:
		connect()
		rc.ReadVersion(addr)
	except Exception as e:
		returnStatus(1,"Unable to read version")
def returnStatus(isError,message):	
	"""prints message to stdout"""
	if isError: #if the message is an error message
		print("{dl}{status}{dl}{msg}".format(dl=deliminator,status=status.error,msg=message))
	else: #if its a success message
		print("{dl}{status}{dl}{msg}".format(dl=deliminator,status=status.success,msg=message))

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
		fwLeft(int(argv[2]))
	elif(x=="-volt" or x=="-V"):
		if(len(argv)>=2 and x == "r"): #if i want it to repeat
			while(1):
				print(getVolt())
				sleep(.1)
		else:
			print(getVolt())
	elif(x=="-v" or x =="-version"):
		print(getVersion())
	elif(x=="--run"):#Run test
		if(len(argv))<=2:
			raise ValueError("This argument requires an additional argument.")
		getVolt()
		fwRight(45)
		fwLeft(45)
		sleep(int(argv[2]))
		stop()
		print(";Done")
	elif(x=='-mixed'):
		mixed(int(argv[2]),int(argv[3]))
	elif(x=='duty'):
		ret = duty(int(argv[2]))
		print("{deliminator}{prefix}{deliminator}{theOutput}".format(prefix=success,deliminator=deliminator,theOutput=ret))
	else: #if the comand is not recognized, ignore it
		#print("unknown command: {cmd}".format(cmd=x))
		returnStatus(1,"unknown command: {cmd}".format(cmd=x))
