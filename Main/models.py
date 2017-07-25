


class User(object):
    """Defines user object"""

    health = 100
    inventory = []
    current_chapter = 1

    def __init__(self, username, userclass):
        
        self.username = username
        self.userclass = userclass


class Item(object):
    """Defines item object"""