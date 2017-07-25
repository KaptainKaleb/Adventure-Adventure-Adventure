import time

def fake_load():
    print "Loading"
    time.sleep(3)
    print "Just a little while longer!"
    time.sleep(2)

def get_user():
    print "Welcome to ADVENTURE ADVENTURE ADVENTURE!!"
    time.sleep(2)
    user_name = raw_input("Please State Your Name: ")
    print "Hello " + user_name + "! Welcome!"
    time.sleep(2)
    return user_name

def get_class():
    print "There are four classes..."
    time.sleep(1)

    print "The Knight class, The Wizard class, The Monk class, and the Thief class!"
    time.sleep(3)

    user_choice = raw_input("Please choose your class: ")
    user_choice = str.upper(user_choice)

    class_list = ['K', 'W', 'M', 'T']

    if user_choice[0] in class_list:
        if user_choice[0] == "K":
            return 0
        elif user_choice[0] == 'W':
            return 1
        elif user_choice[0] == 'M':
            return 2
        elif user_choice[0] == 'T':
            return 3
        else:
            get_class()
    else:
        get_class()
