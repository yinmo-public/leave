# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getGroupIdsJoined())
if int1 == 0:
    print("Gouplist Empyt")
else:
    for gid in yinmo.getGroupIdsJoined():
        print("Leave " + yinmo.getGroup(gid).name)
        sleep(0.5)
        yinmo.leaveGroup(gid)
    print("\nYou leave" + str(int1) + "groups")
    
