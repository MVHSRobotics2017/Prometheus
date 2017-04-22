####
# File: 'base.py'
# Author: theunkn0wn1
# Function: serve as foundation for everything Prometheus
###
import os #because 'system' exists elsewhere, to avoid confusion
from platform import python_version #less memory than importing the whole thing


# # Version test # #
def versionTest():
	"""Ensures the interpreter is python3"""
	strVersion = python_version() #define var strVersion for handling
	if int(strVersion[0])!=3: #if we are not running on the python 3.x.x interpreter
		#the int() is a type cast, i am casting the 1st
		#char of strVersion to the int type for checking
		raise ValueError("This program targets python3, please ensure you have the right path set!")
	else:
		return(0) #i don't really need a return because a fail will break the compile attempt...
		#but I will include it for the sake of clarity

#let's ensure script is executed with python3
versionTest()

os.system("python ../serial/mySerial.py") #explicit import
from roboclaw.roboclaw import Roboclaw #messy, but it appears to work
class prometheus():
	"""base class for prometheus"""
	#begin auto-generated stub...
	def __init__(self):
		super(prometheus, self).__init__()
		#self.arg = arg
		self.port = '/dev/ttyACM0'
		self.baud = 115200
		self.address = 128
	#end auto-generated stub...
	def placeHolder(self):
		pass
	def myInit(self):
		self.rc = Roboclaw(self.port,self.baud)
	def openCom(self):
		self.rc.Open() #opens the comport for usage
	def getVersion(self):
		print(self.rc.ReadVersion(self.address))	
pm = prometheus() #init prometheus class for use
pm.myInit() #init the roboClaw
pm.openCom()
pm.getVersion()