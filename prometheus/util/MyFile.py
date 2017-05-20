isOpen=0
fObject=None
def get():
	global fObject
	if(not isOpen):
		isOpen +=1
		fileObj = open("logfile.log",'w')
		fObject = fileObj
		return(fileObj)
	else:
		return(fObject)
def log(strIn):
	if(isOpen):
		fObject.write(strIn)
	else:
		get()
