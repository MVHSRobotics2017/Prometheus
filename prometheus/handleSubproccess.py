from time import sleep
import subprocess
class status():
	success = "ok"
	error = "err"
	deliminator = ';'
def parseReturn(rawStr,delimChar):
	"""parses rc.py2.py return data"""
	#stage1 = rawStr.split('b\'')
	#print(stage1)
	stage2 = (rawStr.split(delimChar))
	status = stage2[1]
	stage3a = stage2[2].split('\\n') #exception type
	stage3b = stage2[5].split('\\n') #verbose error
#	print("========\nstage2={}\n========".format(stage2))
	return([[stage3a[0],stage3b[0]],status])
def call(args):
	"""makes the procces call and handles response"""
	try:
		x = subprocess.check_output(args)
	except Exception as e:
		print("========\nAn error occured!\n=============")
		raise e
	else:
		retn = parseReturn(str(x),status.deliminator)
#		print(retn)
		if retn[1] == status.error:
			print("==========\n!!!ERROR!!!\n----------\n\'{}\' with verbose note \' {}\'\n----------------".format(retn[0][0],retn[0][1]))
			return(0)
		elif retn[1] == status.success:
			print("Command returned OK, verbose message is: {}".format(retn[0][1]))
			return(1)
			#return(retn[0][1])
		else: #this really should not be possible, but just in case I want to know this occured
			raise ValueError("parse did not return a known status; found {} instead!".format(retn[0][0]))

#call(['python','rc.py2.py','-forward','30'])
#sleep(2)
call(['python','rc.py2.py','-fl','0'])
