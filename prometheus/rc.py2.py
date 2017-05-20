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
			return(ret) #no error, carry on
	else:
		return(1) #connected as is
def fwLeft(pwr):
	ret = connect()
	if type(ret)!=type(None): #error check
		rc.ForwardM2(addr,int(pwr))
		returnStatus(0,"command:forwardLeft completed OK")
		return(0)
	else:
		returnStatus(1,"command: fwLeft failed.")
		return(1)
def fwRight(pwr):
	try:
		mPwr = int(pwr) #try and convert input to int
	except ValueError as e:
		returnStatus(1,"{} is not a valid number!".format(pwr))
		return(1)
	ret = connect()
	if type(ret)!=type(None): #error check
		rc.ForwardM1(addr,mPwr)
		return(0)
	else:
		returnStatus(1,"command: fwRight failed.")
		return(1)	


def duty(cycle):
	ret = connect()
	if type(ret)!=type(None): #error check
		cycle = cycle*10**3
		rc.DutyM1M2(addr,cycle,cycle)
		#rc.DutyM2(adr,cycle)
	else:
		returnStatus(1,"command: duty failed.")
		return(1)
def mixed(pwrA,pwrB):
	ret = connect()
	if type(ret)!=type(None): #error check
		rc.DutyM1(addr,pwrA)
		rc.DutyM2(addr,pwrB)
	else:
		returnStatus(1,"command: mixed failed.")
		return(1)
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
		returnStatus(0,[volts,cellV])
		return([volts,cellV])
	else:
		returnStatus(1,"unable to read voltage")
def getVersion():
	try:
		connect()
		ret = rc.ReadVersion(addr)
		returnStatus(0,ret)
	except Exception as e:
		returnStatus(1,"Unable to read version")
def returnStatus(isError,message):	
	"""prints message to stdout"""
	if isError: #if the message is an error message
		print("{dl}{status}{dl}{msg}{dl}".format(dl=status.deliminator,status=status.error,msg=message))
		print("{dl}{status}{dl}{msg}{dl}".format(dl=status.deliminator,status=status.error,msg=message))
	else: #if its a success message
		print("{dl}{status}{dl}{msg}{dl}".format(dl=status.deliminator,status=status.success,msg=message))
		print("{dl}{status}{dl}{msg}{dl}".format(dl=status.deliminator,status=status.success,msg=message))

if(len(argv)<=1): #if no no arguments are given
	returnStatus(1,"not enough arguments!")
	#raise ValueError("Not enough arguments!")
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
		x=fwRight(argv[2])
		if(x):
			returnStatus(1,"fwRight returned error state {}".format(x))
			pass #if the first command fails... don't bother with the other side
		else:
			returnStatus(0,"fwRight completed with status 0.")
			x = fwLeft(argv[2])
			if x:
				returnStatus(1,"fwLeft returned error state {}".format(x))
			else:
				returnStatus(0,"command '-forward' completed OK")
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
		print("{deliminator}{prefix}{deliminator}{theOutput}".format(prefix=status.success,deliminator=status.deliminator,theOutput=ret))
	else: #if the comand is not recognized, ignore it
		#print("unknown command: {cmd}".format(cmd=x))
		returnStatus(1,"unknown command: {cmd}".format(cmd=x))
		returnStatus(1,"unknown command: {cmd}".format(cmd=x))

