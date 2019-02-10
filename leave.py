# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getGroupIdsJoined())
if int1 == 0:
    print("您還沒有加入群組")
else:
    for gid in yinmo.getGroupIdsJoined():
        print("已退出 " + yinmo.getGroup(gid).name)
        yinmo.leaveGroup(gid)
    print("\n您退出" + str(int1) + "個群組")
    