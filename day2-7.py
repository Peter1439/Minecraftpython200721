# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:13:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("Please enter your name")
message = input("Enter the message")
while True :
    mc.postToChat("["+username+"]"+message)