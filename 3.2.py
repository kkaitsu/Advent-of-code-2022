# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 07:53:16 2022

@author: Kaisa Ylikoski
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:33:37 2022

@author: Kaisa Ylikoski
"""

data = open('3.txt', 'r')
#delete \n at the time of reading file (strip) and remove dublicate letters (set)
data = ["".join(set(x.strip())) for x in data.readlines()]



s = 0
for i in range(0,len(data),3):
    for letter in data[i]:
        if data[i+1].find(letter) != -1:
            for letter2 in data[i+2]:
                if letter == letter2:
                    #odr on hieno funktio, joka asciilla on jo numero
                    #pikkuaakkoset on ord()-96
                    #isot aakkoset on ord()-38
                    if letter.isupper():
                        s += ord(letter)-38
                        print(letter, ord(letter)-38 )
                        break
                        
                    else:
                        s += ord(letter)-96
                        print(letter, ord(letter)-96 )
                        break
                
print(s)
        