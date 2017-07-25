 import ConfigParser
class saveinfo():
    def createsavefile(username, userclass, chapter):
        config = ConfigParser.RawConfigParser()
        config.add_section('Main')
        config.add_section('Inventory')
        config.add_section('Character')
        config.set('Main', 'Class', userclass)
        config.set('Main', 'Username', username )
        config.set('Main', 'Current_Chaper', chapter)
        config.set('Character', 'Health', 100)
        with open('userdata.cfg', 'wb') as configfile:
            config.write(configfile)
    def getchapter():
        config = ConfigParser.RawConfigParser()
        config.read('userdata.cfg')
        chapter = config.get('Main', 'Current_Chapter')
       return chapter
    def getusername():
        config = ConfigParser.RawConfigParser()
        config.read('userdata.cfg')
        username = config.get('Main', 'Username')
        return username
    def getclass():
        config = ConfigParser.RawConfigParser()
        config.read('userdata.cfg')
        user_class = config.get('Main', 'Class')
        return user_class
    def updatehitpoints(hitpoints):
        config = ConfigParser.RawConfigParser()
        config.read('userdata.cfg')
        config.set('Character', 'Health', hitpoints)
        with open('userdata.cfg', 'wb') as configfile:
            config.write(configfile)
    createsavefile("Turtle", "Knight", 1)
