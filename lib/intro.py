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

    user_class = raw_input("Please choose your class: ")
    class_list = ['Knight', 'Wizard', 'Monk', 'Thief']

    if user_class in class_list:
        return user_class
    else:
        get_class()
