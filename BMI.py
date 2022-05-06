# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:20:19 2019

@author: ray34
"""

x=int(input("性別?(男=1 女=2)"))
y=float(input("BMI?"))
if x==1:
    if y>24:       
        print("過胖")
    elif y<20:
        print("過輕")
    else:
        print("正常")
if x==2:
    if y>22:
        print("過胖")
    elif y<18:
        print("過輕")
    else:
        print("正常")
    
