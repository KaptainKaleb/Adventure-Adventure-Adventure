import time
import lib.lib-save
import lib.lib-intro
#def fake_load():
#	print "Loading"
#	time.sleep(3)
#	print "Just a little while longer!"
#	time.sleep(2)
#fake_load()

def class_found():
	time.sleep(3)

	print "Wait... This cannot be"
		time.sleep(3)

	print "You are " + user_name + " of the " + user_class + "s?"
		time.sleep(3)

	print "Is this really you?"
		time.sleep(3)

	print "You... You are him?"
		time.sleep(3)

	print "Come with me. Quickly!"

def main():
	if lib-save.check():
		save = open("savegame.txt", "r")
		save_info = save.readlines()
		save.close()
	else if !lib-save.check():
		lib-save.new(lib-intro.get_user(),lib-intro.get_class())
	global user_class
	class_check()


if __name__ == "__main__":
	main()

# We're going to have to have one main file for each chapter, and try to avoid importing in circles
