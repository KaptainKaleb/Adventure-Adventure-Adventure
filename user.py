from aaa import userInfo
from lib.save import check

def update():
    if check() == true:
        savegame = open("savegame.txt", "r")
        global name
        name = savegame.readline(0)              # Character Name
        global clss
        clss = savegame.readline(1)              # Character Class
        global wpn1
        wpn1 = savegame.readline(2)              # Weapon 1 (Main)
        global wpn2
        wpn2 = savegame.readline(3)              # Weapon 2 (Offhand)
        global inv
        inv[0] = savegame.readline(4)            # Inventory 1
        inv[1] = savegame.readline(5)            # Inventory 2
        inv[2] = savegame.readline(6)            # Inventory 3
        inv[3] = savegame.readline(7)            # Inventory 4
        inv[4] = savegame.readline(8)            # Inventory 5
        inv[5]= savegame.readline(9)             # Inventory 6
        global lvl
        lvl[0] = savegame.readline(10)           # Main Level
        lvl[1] = savegame.readline(11)           # Fighting Level
        lvl[2] = savegame.readline(12)           # Speech Level
        lvl[3] = savegame.readline(13)           # Crafting Level
        lvl[4] = savegame.readline(14)           # Agility Level

        if clss == 3:
            global spl
            spl[0] = savegame.readline(15)       # Spell 1
            spl[1] = savegame.readline(16)       # Spell 2
            spl[2] = savegame.readline(17)       # Spell 3

        global pgrs
        pgrs = savegame.readline(18)             # Progress
        global htpt
        htpt = savegame.readline(19)             # Hitpoints (Health)
