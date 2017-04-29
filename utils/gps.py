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


#Word Enums
class words():
	latLong = "$GPGGA" #lat long data follows
	#format: dddMM.MMMM where d = deg, M = minutes
#def hi():
#	print("hello!")
def formatLatLong(rawStr):
	"""converts GPGGA data to Degrees, Seconds"""
	#init locals
	latDD = 0
	longDD = 0
	latMM = 0
	longMM=0
	tempString = "" #needed for the concat steps
	#parse rawStr into better format
	delimStr = rawStr.split(',') #splits str over delim into list(str)
	latV = delimStr[2] #raw value
	latD = delimStr[3] #north/south
	longV = delimStr[4]#raw value
	longD = delimStr[5]#West/East
	#now for the ugly bit...
	print("latv={lv}".format(lv = latV))
	if(len(latV) ==10): #if the first Deg is zero (not outputted)
		tempString = (latV[0])+(latV[1]) #concat the first two bytes
		print(tempString)
		latDD = int(tempString)
		i=0 #reset itterator
		for x in latV: #for each char byte
			if(i>1):
				tempString+=x
			i +=1
		latMM = float(tempString)
	elif(len(latV) == 11): #if we have all the LatDD bytes
		i=0
		for x in xrange(0,2):
			tempString+=x
			i+=1
		#latDD = int(latV[0])*100+int(latV[1])*10+int(latV[2])
		latDD = int(tempString)
	if(len(longV)==10): #possible contingency
		raise NotImplementedError("the contignency arrised. FIX ME!")
	elif(len(longV)==11): # if we have all the LongDD bytes
		i=0
		tempString = ""
		#longDD
		tempString = longV[0]+longV[1]
		longDD = int(tempString)
		print(tempString)
		#LongMM
		tempString = ""
		i=0
		for x in longV: #concat the longitudinal minute value into a single string
			if(i>1):
				tempString+=x
			i+=1
		longMM = float(tempString) #and convert to float (because decimals)
	return([latDD,latMM,longDD,longMM])
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
	elif(type(Baud)!=int):
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

#Purge before committing!
