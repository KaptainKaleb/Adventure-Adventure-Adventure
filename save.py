import ConfigParser
    class saveinfo():
        def createsavefile(username, userclass, chapter):
            config = ConfigParser.RawConfigParser()
            config.add_section('Main')
            config.set('Main', 'Class', userclass)
            config.set('Main', 'Username', username )
            congig.set('Main', 'Current_Chaper', chapter)
            with open('userdata.cfg', 'wb') as configfile:
                config.write(configfile)
        def getchapter():
            config = ConfigParser.RawConfigParser()
            config.read('userdata.cfg')
            chapter = config.get('Main', 'Current_Chapter')