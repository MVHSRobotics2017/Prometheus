# # #
# File: gps.py
# Function: module for handling GPS communications.
# #

#imports
import serial #for serial comms

class gps(port):
	"""handle GPS communications."""
	def __init__(self,arg):
		super(gps,self).__init()
		self.arg = arg
		self.port = port
