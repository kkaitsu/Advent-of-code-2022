# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:08:51 2022

@author: Kaisa Ylikoski

a x kivi 1 p
b y paperi 2 p
c z sakset 3 p

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
 
points = 0
for row in l:
    #paperi voittaa kiven
    if row[0] == 'A' and row[1] == 'Y':
        points += 2 + 6
    #sakset voittaa paperin
    elif row[0] == 'B' and row[1] == 'Z':
         points += 3 + 6
    #kivi voittaa sakset
    elif row[0] == 'C' and row[1] == 'X':
        points += 1 + 6
    #kivi häviää paperin
    elif row[0] == 'B' and row[1] == 'X':
        points += 1
    #paperi häviää sakset
    elif row[0] == 'C' and row[1] == 'Y':
        points += 2
    #sakset häviää kiven
    elif row[0] == 'A' and row[1] == 'Z':
        points += 3
    #kivitasuri
    elif row[0] == 'A' and row[1] == 'X':
        points += 1 + 3
    #paperitasuri
    elif row[0] == 'B' and row[1] == 'Y':
        points += 2 + 3
    #saksettasuri      
    elif row[0] == 'C' and row[1] == 'Z':
        points += 3 + 3
        
        
print(points)
    

