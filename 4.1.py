# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:54:33 2022

@author: Kaisa Ylikoski
"""

l = []
with open("4.txt") as f:
    data = f.read()
    data = data.split('\n')
    
    for row in data:
        tuple1 = row.split(',')[0].split('-')
        tuple2 = row.split(',')[1].split('-')
        l.append(((int(tuple1[0]),int(tuple1[1])),(int(tuple2[0]),int(tuple2[1]))))

i = 0
for row in l:
    if ((row[0][0] >= row[1][0]) and (row[0][1] <= row[1][1])) or (row[0][0] <= row[1][0] and row[0][1] >= row[1][1]):
        i += 1
        
        
print(i)
        