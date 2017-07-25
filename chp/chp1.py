import sys
from time import sleep
#from user import weapon #Weapon? Gonna put that in chapter 0? # I guess I'll import it using my own method from the savegame.txt file

sys.path.insert(0, "/mnt/c/Users/James/Documents/projects/Adventure-Adventure-Adventure")

def dialog00():
	print "--In the Sewer--"
	sleep(1)

	print "*The sewer smells dank and musty*" # ayy lmao
	sleep(1)

	print "*You venture a few steps in, and you immediately spot a giant rat*"
	sleep(1)

	print "*Preparing yourself for combat, you approach the rat with " + weapon +" drawn*"
	sleep(2)
