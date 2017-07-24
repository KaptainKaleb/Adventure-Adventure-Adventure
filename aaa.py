from chp import *
from lib import *

def main():
    #intro.fake_load()

	if save.check() == True:
		savegame = open("savegame.txt", "r")
		saveinfo = savegame.readlines()
		savegame.close()
	elif save.check() != True:
		save.new(intro.get_user(),intro.get_class())
	
	chp1.dialog00()

if __name__ == "__main__":
	main()
