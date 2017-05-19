import subprocess
class status(object):
	success = ""
	error = "err"
def parseReturn(rawStr,delimChar):
	"""parses rc.py2.py return data"""
	stage1 = rawStr.split('b\'')
	print(stage1[1])
	stage2 = (stage1[1].split(delimChar))
	status = stage2[1]
	stage3a = stage2[2].split('\\n')
	stage3b = stage2[4].split('\\n')
	print("========\nstage2={}\n========".format(stage2))
	return([[stage3a[0],stage3b[0]],status])
def call(args):
	try:
		x = subprocess.check_output(args)
	except Exception as e:
		print("========\nAn error occured!\n=============")
		#raise e
	else:
		retn = parseReturn(str(x),';')
		print(retn)
		if retn[1] == status.error:
			print("==========\n!!!ERROR!!!\n==========\n\'{}\' with verbose note \' {}\' occured!".format(retn[0][0],retn[0][1]))
	

call(['python','rc.py2.py','-V'])