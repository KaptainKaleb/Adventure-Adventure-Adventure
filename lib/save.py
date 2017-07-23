def check():
	try:
		save = open("savegame.txt", "r")
		save.close()
		return True

	except:
		return False

def new(usr, cls):
	newsave = open("savegame.txt", "w")

	newsave.write("1")			# validates savefile when check_save()
	newsave.write("usr="+usr)	# adds username
	newsave.write("cls="+cls)	# adds class
	newsave.write("pgs="+"1")	# adds default progress

	newsave.close()
