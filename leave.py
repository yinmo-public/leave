# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE()
int1 = len(yinmo.getGroupIdsJoined())
if int1 == 0:
    print("您還沒有加入群組")
else:
    for gid in yinmo.getGroupIdsJoined():
        print("已退出 " + yinmo.getGroup(gid).name)
        sleep(0.5)
        yinmo.leaveGroup(gid)
    print("\n您退出" + str(int1) + "個群組")
    
