####
# File: 'base.py'
# Author: theunkn0wn1
# Function: serve as foundation for everything Prometheus
###
import os #because 'system' exists elsewhere, to avoid confusion
from platform import python_version #less memory than importing the whole thing
import subprocess #for executing other programs

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

class prometheus():
	"""base class for prometheus"""
	roboLib = "" #perhaps i need to declare it before the init... (wip)
	#begin auto-generated stub...
	def __init__(self):
		super(prometheus, self).__init__()
		#self.arg = arg
		self.address = 128 #roboclaw address
		self.roboLib = 'rc.py2.py' #this is the roboclaw interface
	#end auto-generated stub...
	def placeHolder(self):
		pass
	def myInit(self):
		self.args = ['python',self.roboLib,'-v']
		self.proc = sb.open()		
	def getVersion(self):
		pass	
