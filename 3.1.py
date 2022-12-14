# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:33:37 2022

@author: Kaisa Ylikoski
"""

data = open('3.txt', 'r')
#delete \n at the time of reading file
data = [x.strip() for x in data.readlines()]

s = 0
for row in data:
    for letter in row[:int((len(row))/2)]:
        if row[int((len(row))/2):].find(letter) != -1:
        
            #odr on hieno metodi, joka asciilla on jo numero
            #pikkuaakkoset on ord()-96
            #isot aakkoset on ord()-38
            if letter.isupper():
                s += ord(letter)-38
                #print(ord(letter)-38)
                print(row[:int((len(row))/2)], ' ' ,row[int((len(row))/2):])
                print(letter, 'upper')
                break
            else:
                s += ord(letter)-96
                #print(ord(letter)-96)
                print(row[:int((len(row))/2)], ' ' ,row[int((len(row))/2):])
                print(letter, 'lower')
                break
            
print(s)
        