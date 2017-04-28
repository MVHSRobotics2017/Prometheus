# # #
# File: gps.py
# Function: module for handling GPS communications.
# #

#imports
import serial #for serial comms

#global vars
port = "" #set me via .setPort!
baud = 0
isPortDefined = 0 #Bool

#def hi():
#	print("hello!")
def init(Port,Baud):
	global isPortDefined
	global baud
	global port
	if(isPortDefined):
		return() # no need to waste CPU time repeating whats been done
	elif(type(Port)==str and not isPortDefined): #sanity check
		port = Port
		#return(port) #redunant but affirmative feedback
	elif(type(Port)!=str):
		raise TypeError("Expected a string!")
	elif(type(Baud)==int and not isPortDefined): #sanity check
		baud = Baud
	elif(type(Baud!=int)):
		raise TypeError("Expected an Int!")
	else:
		raise ValueError("Something unexpected occured!")
		#like, really. This should be unreachable
	isPortDefined = 1
	return([port,baud])

def getSerial():
	"""returns serial object for GPS"""
	if(isPortDefined): #sanity check
		return(serial.Serial(port, baud))
	else:
		raise ValueError("You need to init gps before attempting to get the object!")

