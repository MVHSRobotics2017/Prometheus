# # #
# File: gps.py
# Function: module for handling GPS communications.
# #

#imports
import serial #for serial comms

#global vars
port = "" #set me via .setPort!

def setPort(arg):
	if(type(arg)==str): #sanity check
		port = arg
		return(port) #redunant but affirmative feedback
	else:
		raise TypeError("Expected a string!")

