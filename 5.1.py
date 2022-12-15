# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:20:20 2022

@author: Kaisa Ylikoski
"""


def transpose(l1, l2):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

def mirror(seq):
    output = list(seq[::-1])
    return output

def parsi_data():
    #create table of each move
    #movements = [move],[from],[to]
    movements = []
    with open("5.1.txt") as f:
        data = f.read()
        data = data.split('\n')
        for row in data:
            row = row.split(' ')
            movements.append([int(row[1]),int(row[3]),int(row[5])])
            
    
    #create table of starting positions    
    with open("5.2.txt") as f:
        data = f.read()
        data = data.split('\n')
        positions = []
        #transpoosaa taulukko kivasti
        data = transpose(data,data)
        for i,row in enumerate(data[1::4]):
            row = mirror(row)
            #remove empty spaces at end of list
            row = list(filter(str.strip, row))
            positions.append(row)
            
    return positions, movements

def move_palikka(move, from1, to, positions):
    for i in range(0,move):
        #pop(): Remove an item by index and get its value
        positions[to-1].append(str(positions[from1-1].pop(-1)))
    return positions
        

positions, movements = parsi_data()
for move in movements:
    positions = move_palikka(move[0],move[1],move[2],positions)
for position in positions:
    print(position[-1])
    
