# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
for gid in yinmo.getGroupIdsJoined():
    yinmo.leaveGroup(gid)
    print("已退出群組")