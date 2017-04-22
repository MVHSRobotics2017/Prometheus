####
# Author: TheUnkn0wn1
# Function: control Roboclaw motor controller
# Python Version: Python2
###

#Imports
from sys import argv #for command-line paramaters ('Arguments')
from roboclaw.roboclaw import Roboclaw
#config
debug=1
port='/dev/ttyACM0'
addr=128
baud=115200
#globals
rc = Roboclaw(port,baud) #init Roboclaw instance

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

if(len(argv)<=1): #if no no arguments are given
	raise ValueError("Not enough arguments!")
else:#if we have an argument, lets figure out the command we received...
	x=argv[1] #we only care about the first arg as it is our command
	if(x == "-default"):
		#connect()
		fwLeft(30)
		fwRight(30)
	elif(x == "-forwardLeft"):
		fwLeft(int(argv[2]))
	elif(x == "-stop"):
		stop()
	elif(x =="-forwardRight"):
		fwRight(int(argv[2]))
	else: #if the comand is not recognized, ignore it
		print("unknown command: {cmd}".format(cmd=x))

