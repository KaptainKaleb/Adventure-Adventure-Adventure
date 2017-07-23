def main():
	import time
	#def fake_load():
	#	print "Loading"
	#	time.sleep(3)
	#	print "Just a little while longer!"
	#	time.sleep(2)
	#fake_load()
	print "Welcome To ADVENTURE ADVENTURE ADVENTURE!!"
	time.sleep(2)
	user_name = raw_input("Please State Your Name: ")
	print "Hello there " + user_name + "! Nice to meet you!"
	time.sleep(2)
	print "There are four classes..."
	time.sleep(1)
	print "The Knight class, The Wizard class, The Monk class, and the Thief class!"
	time.sleep(3)
	def check_class():
		global user_class
		user_class = raw_input("Please choose your class: ")
		class_list = ['Knight', 'Wizard', 'Monk', 'Thief']
		if user_class in class_list:
			time.sleep(3)
			print "Wait..... This cant be"
			time.sleep(3)
			print "You are " + user_name + " of the " + user_class + "s?"
			time.sleep(3)
			print "Is this really you???"
			time.sleep(3)
			print "You.... You are him?"
			time.sleep(3)
			print "Come with me. Quickly!"
		else:
			print "You've Entered Something Wrong! Please Try Again!"
			user_class = raw_input("Please choose your class: ")
			check_class()
		return user_class
	check_class()
if __name__ == "__main__":
	main()

# We're going to have to have one main file each chapter, and try to avoid importing in circles

import chapter_one
