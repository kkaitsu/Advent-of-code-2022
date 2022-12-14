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

total_l = []            
for i in calories_l:
    total_l.append(sum(i))

#missä maximikalorit
max_cal1 = max(total_l)
#sen indeksi
max_cal1_i = total_l.index(max_cal1)    
total_l[max_cal1_i] = 0

max_cal2 = max(total_l)
max_cal2_i = total_l.index(max_cal2) 
total_l[max_cal2_i] = 0
        
max_cal3 = max(total_l)
max_cal3_i = total_l.index(max_cal3)

s = max_cal1 + max_cal2 + max_cal3

print("How many Calories are those Elves carrying in total: ", s)

    
