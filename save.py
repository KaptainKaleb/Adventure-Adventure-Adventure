from configparser import RawConfigParser

def createsavefile(username, userclass, chapter):
    config = RawConfigParser()
    config.add_section('Main')
    config.set('Main', 'Class', userclass)
    config.set('Main', 'Username', username )
    config.set('Main', 'Current_Chaper', chapter)
    config.set('Character', 'Health', 100)
    with open('userdata.cfg', 'wb') as configfile:
        config.write(configfile)
def getchapter():
    config = RawConfigParser()
    config.read('userdata.cfg')
    chapter = config.get('Main', 'Current_Chapter')
    return chapter
def getusername():
    config = RawConfigParser()
    config.read('userdata.cfg')
    username = config.get('Main', 'Username')
    return username
def getclass():
    config = RawConfigParser()
    config.read('userdata.cfg')
    user_class = config.get('Main', 'Class')
    return user_class
def updatehitpoints(hitpoints):
    config = RawConfigParser()
    config.read('userdata.cfg')
    config.set('Character', 'Health', hitpoints)