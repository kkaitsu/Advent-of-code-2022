# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:01:27 2022

@author: Kaisa Ylikoski
"""

calories_l = []
with open("1.1.txt") as f:

    calories = f.read()
    calories = calories.split('\n')
    i = 0
    calories_l.append([])
    for row in calories:
        if row == "":
            i += 1
            calories_l.append([])
        else:
            calories_l[i].append(int(row))
            
s = 0   
for i in calories_l:
    if sum(i) > s:
        s = sum(i)
        
print("How many total Calories is that Elf carrying?: ", s)

    
