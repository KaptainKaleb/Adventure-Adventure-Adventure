def main():
	import time
	def fake_load():
		print "Loading"
		time.sleep(3)
		print "Just a little while longer!"
		time.sleep(2)
	def create_man():
			print "Welcome To ADVENTUE ADVENTURE ADVENTURE!!"
			time.sleep(2)
			user_name = raw_input("Please State Your Name: ")
			print "Hello there " + user_name + "! Nice to meet you!"
			time.sleep(2)
			print "There are four classes..."
			time.sleep(1)
			print "The Knight class, The Wizard class, The Monk class, and the Theif class!"
			class_list = ["Knight", "Wizard", "Monk", "Theif"]
			time.sleep(3)
			user_class = raw_input("Please choose your class: ")
			while True:
				if user_class != class_list:
					print "You entered somehting wrong! Make sure you type in your class exactly how it is displayed!"
					time.sleep(3)
			return
			
			time.sleep(3)
			print "Wait..... This cant be"
			time.sleep(3)
			print user_name + " of the " + user_class + "s" + "????"
			time.sleep(3)
			print "Is this really you???"
			time.sleep(3)
	fake_load()
	create_man()
main()
		



		
