from aaa import userInfo

global name
name = userInfo[0]              	# Character Name
global clss
clss = userInfo[1]              # Character Class
global wpn1
wpn1 = userInfo[2]              # Weapon 1 (Main)
global wpn2
wpn2 = userInfo[3]              # Weapon 2 (Offhand)
global inv[0]
inv[0] = userInfo[4]            # Inventory 1
global inv[1]
inv[1] = userInfo[5]            # Inventory 2
global inv[2]
inv[2] = userInfo[6]            # Inventory 3
global inv[3]
inv[3] = userInfo[7]            # Inventory 4
global inv[4]
inv[4] = userInfo[8]            # Inventory 5
global inv[5]
inv[5]= userInfo[9]            # Inventory 6
global lvl[0]
lvl[0] = userInfo[10]           # Main Level
global lvl[1]
lvl[1] = userInfo[11]           # Fighting Level
global lvl[2]
lvl[2] = userInfo[12]           # Speech Level
global lvl[3]
lvl[3] = userInfo[13]           # Crafting Level
global lvl[4]
lvl[4] = userInfo[14]           # Agility Level

if clss == "Mage":
    global spl[0]
	spl[0] = userInfo[15]       # Spell 1
    global spl[1] 
	spl[1] = userInfo[16]       # Spell 2
    global spl[2] 
	spl[2] = userInfo[17]       # Spell 3

global pgrs
pgrs = userInfo[18]             # Progress
global htpt
htpt = userInfo[19]             # Hitpoints (Health)
 
