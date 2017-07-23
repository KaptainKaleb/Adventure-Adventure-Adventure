def main():
	import time
	def fake_load():
		print "Loading"
		time.sleep(3)
		print "Just a little while longer!"
		time.sleep(2)
	fake_load()
	print "Welcome To Some Cool Adventure Name!!"
	time.sleep(2)
	user_name = raw_input("Please State Your Name: ")
	print "Hello there " + user_name + "! Nice to meet you!"
	time.sleep(2)
	print "There are four classs..."
	time.sleep(1)
	print "The Class1 Class1, The Class2 class2, The Class3 Class3, and the Class4 Class!"
	time.sleep(3)
	def check_class():
		global user_class
		user_class = raw_input("Please choose your class: ")
		class_list = ['Class1', 'Class2', 'Class3', 'Class4']
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
main()
import chapter_one
