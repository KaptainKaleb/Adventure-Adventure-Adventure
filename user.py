from lib.save import check

class Character():
    def __init__(self, pos, name, level):
        """
            Represents any character(npc or pc), actual characters inherits from this base class

        :param pos: position as [x,y]
        :param name: string
        :param level: integer( or list of integers ? )
        """
        self.name = name
        self.level = level
        self.pos = pos

class Player(Character):
    def __init__(self, name, job, level, pos, stats):
        """
            Represents a playing Character

        :param job: class/job of the character TODO:what are they?Strings? Ints? Enum members?
        :param level: integer or list of integers
        :param pos: position as [x,y]
        :param name: string
        :param stats: list of integers? Dictionnary ? like {'strength':5, 'agility':12...}
        """
        super().__init__(pos, name, level)
        self.job=job
        self.stats=stats #TODO:What stats and how are they set?
        self.spells=[]
        self.inventory=[] #TODO:either an Inventory object, or just a list
        self.weapon="Fists"
        self.armor="Dirty shirt"
        self.progress=0
        self.health=100  #TODO:How much
        self.stamina=100 #TODO:How much?