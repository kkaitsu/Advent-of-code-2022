# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:08:51 2022

@author: Kaisa Ylikoski

a x kivi 1 p
b y paperi 2 p
c z sakset 3 p

x=hävitä
y=tasapeli
z=voittaa

voitto= 6p
tasapeli = 3p
"""
l = []
with open("2.txt") as f:
    data = f.read()
    data = data.split('\n')
    
    for row in data:
        row = row.split(' ')
        l.append((row[0],row[1]))   

#apurandomlista
a = ['C', 'A', 'B', 'C', 'A']    
points = 0
for row in l:
    index = a[1:4].index(row[0]) + 1
    if row[1] == 'X':
        index -= 1
    elif row[1] == 'Y':
        points += 3
    elif row[1] == 'Z':
        index += 1
        points += 6

    if a[index] == 'A':
        points += 1
    elif a[index] == 'B':
        points += 2
    elif a[index] == 'C':
        points += 3
        
print(points)
    

#8745 too low