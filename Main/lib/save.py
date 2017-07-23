def check():
	save = open("savegame.txt", "r")
		if save.read(1) != None:
			return true
		else:
			return false
	save.close()

def new(usr, cls):
	newsave = open("savegame.txt", "w")
		newsave.write("1")			# validates savefile when check_save()
		newsave.write("usr="+usr)	# adds username
		newsave.write("cls="+cls)	# adds class
		newsave.write("pgs="+"1")	# adds default progress
	newsave.close()
