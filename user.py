from aaa import userInfo
from lib.save import check

if check() == true:
    global name
    name = userInfo[0]              # Character Name
    global clss
    clss = userInfo[1]              # Character Class
    global wpn1
    wpn1 = userInfo[2]              # Weapon 1 (Main)
    global wpn2
    wpn2 = userInfo[3]              # Weapon 2 (Offhand)
    global inv
    inv[0] = userInfo[4]            # Inventory 1
    inv[1] = userInfo[5]            # Inventory 2
    inv[2] = userInfo[6]            # Inventory 3
    inv[3] = userInfo[7]            # Inventory 4
    inv[4] = userInfo[8]            # Inventory 5
    inv[5]= userInfo[9]             # Inventory 6
    global lvl
    lvl[0] = userInfo[10]           # Main Level
    lvl[1] = userInfo[11]           # Fighting Level
    lvl[2] = userInfo[12]           # Speech Level
    lvl[3] = userInfo[13]           # Crafting Level
    lvl[4] = userInfo[14]           # Agility Level

    if clss == 3:
        global spl
        spl[0] = userInfo[15]       # Spell 1
        spl[1] = userInfo[16]       # Spell 2
        spl[2] = userInfo[17]       # Spell 3

    global pgrs
    pgrs = userInfo[18]             # Progress
    global htpt
    htpt = userInfo[19]             # Hitpoints (Health)
