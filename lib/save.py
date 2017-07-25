def check():
	try:
		save = open("savegame.txt", "r")
		save.close()
		return True

	except:
		return False

def new(user, clss): #TODO
	newsave = open("savegame.txt", "w")

	newsave.write("user="+user)	# adds username
	newsave.write("clss="+str(clss))# adds class
	newsave.write("prgs=1")		# adds default progress

	newsave.close()
