####
# File: 'base.py'
# Author: theunkn0wn1
# Function: serve as foundation for everything Prometheus
###
import os #because 'system' exists elsewhere, to avoid confusion
from platform import python_version #less memory than importing the whole thing
import handleSubproccess as sb
import time
import util.gps as gps
import util.geofence as geoFence
import util.geofence as geofence #because typos occured and this was the simplest solution...
import util.sonar as sonar
import sys
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
geo_points = 4
class commands():
	py = 'python'
	getVolt = '-volt'
	getVersion = '-v'
	driveRight = '-fr'
	driveLeft = '-fl'
	driveForward = '-forward'
	stop = '-stop'
class prometheus():
	"""base class for prometheus"""
	#begin auto-generated stub...
	def __init__(self):
		super(prometheus, self).__init__()
		#self.arg = arg
		self.address = 128 #roboclaw address
		self.roboLib = 'rc.py2.py' #this is the roboclaw interface
		self.fence = gps.initGeoFence(geo_points) # prompts for the geofence to be defined
			#must occur at startup (perhaps cached for brownouts?)		
	#end auto-generated stub...
	def placeHolder(self):
		pass
	def myInit(self):
		self.args = [commands.py,self.roboLib,commands.getVersion]
		return(sb.call(self.args))		
	def getVersion(self):
		self.args = [commands.py,self.roboLib,commands.getVersion]
		return(sb.call(self.args))
	def getVoltage(self):
		self.args = [commands.py,self.roboLib,commands.getVoltage]
		return(sb.call(self.args))
	def setRight(self,pow):
		loc = gps.getLocation()
		if(geofence.pip(loc[0],loc[1],self.fence)):
			self.args = [commands.py,self.roboLib,commands.driveRight,pow]
			return(sb.call(self.args))
	def setLeft(self, pow):
		loc = gps.getLocation()
		if(geofence.pip(loc[0],loc[1],self.fence)):
			self.args = [commands.py,self.roboLib,commands.driveLeft,str(pow)]
			print(self.args)
			return(sb.call(self.args))
		else:
			print("exceeded fence!\nStopping!")
			self.stop()
	def forward(self,pow):
		loc = gps.getLocation()
		print("my location is {}",format(loc))
		if(geofence.pip(loc[0],loc[1],self.fence)):
			self.args = [commands.py,self.roboLib,commands.driveForward,str(pow)]
			return(sb.call(self.args))
		else:
			self.stop()
			print("Exceeded fence!\nStopping!")
			return(2)
	def stop(self):
		self.args = [commands.py,self.roboLib,commands.stop]
		return(sb.call(self.args))
	def collisionTest(self):
		"""test if unit can avoid crashing via sonar eyes"""
		dist = sonar.read()
		print(dist)
		while(dist[2]>=45.0):
			dist = sonar.read()
			print(dist)
			ret = self.forward(30)
#			time.sleep(1)
			if(ret==2):
				try:
					break
				except Exception as e:
					pass
		self.stop()
	def scan(self):
		retn = [0,0,0]
		dist = sonar.read()
		if(dist[0] <=60):
			retn[0] = not retn[0]
		elif(dist[1] <=60):
			retn[1] = not retn[1]
		elif(dist[2] <= 55):
			retn[2] = not retn[2]
		return(retn)
	def search(self):
		"""search algorithm"""
		cruse = 60
		loc = gps.getLocation()
		if(geofence.pip(loc[0],loc[1],self.fence)):
			self.forward(cruse)
			scanRet = self.scan()
			if(scanRet[0]): #obj off the right sensor
				self.setRight(cruse/2)
				sleep(1)
				self.setRight(cruse)
			elif(scanRet[1]):#obj off left sensor
				self.setLeft(cruse/2)
				sleep(1)
				self.setLeft(cruse)
			elif(scanRet[2]):#obj ahead
				self.stop
				logMgr.log(gps.getLocation)
				self.setRight(cruse/2)
				sleep(1)
				self.setRight(0)
				self.setLeft(cruse/2)
				sleep(1)
			self.forward(cruse)
rc = prometheus()
print("======\nInit complete\n-----\nHit <enter> to run the program")
sys.stdin.readline()
#rc.forward(30)
#time.sleep(2)
#rc.stop()
#time.sleep(1)
#rc.setLeft(30)
#time.sleep(2)
#rc.forward(30)
#time.sleep(2)
#rc.stop()
while(1):
	try:
		rc.search()
	except Exception as e:
		rc.stop()
		break 
