from chp import *
from lib import *
from user import Player


def main():
    userInfo=None
    user = None

    if save.check():
        savegame = open("savegame.txt", "r")
        userInfo = savegame.readlines()
        userInfo = [l.split(',') for l in [userInfo[i] for i in range(len(userInfo))]]
        print(userInfo)
        savegame.close()
    else:
        user=Player(intro.get_user(), intro.get_class(), 1, [0,0], [10,10,10,10])
        save.new(user.name, user.job)

    chp0.dialog00(user)
    chp1.dialog00(user)


if __name__ == "__main__":
    main()
