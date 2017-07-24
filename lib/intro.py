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

    user_shorthand = raw_input("Please choose your class (Please use the first letter of each class): ")
    user_shorthand.upper
    
    class_list = ['Knight', 'Wizard', 'Monk', 'Thief']
    shorthand_list = ['K', 'W', 'M', 'T']

    if user_shorthand in shorthand_list:
        if user_shorthand == 'K':
            user_class = 'Knight'
        elif user_shorthand == 'W':
            user_class = 'Wizard'
        elif user_shorthand == 'M':
            user_class = 'Monk'
        elif user_shorthand == 'T':
            user_class = 'Thief'
        else:
            get_class()

    #if user_class in class_list:
        #return user_class
    #else:
        #get_class()
