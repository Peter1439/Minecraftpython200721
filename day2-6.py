# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:44:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

blockid = int(input("enter the block id:"))
mc.setBlock(x+1,y,z,blockid)