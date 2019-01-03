#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:00:50 2018

@author: michael
"""

#%% Chapter 5 | Sorting and Searching 

3 in [3,5,2,4,1]

#%% Sequential Search

def sequentialSearch(alist, item): 
    pos = 0
    found = False 
    
    while pos < len(alist) and not found: 
        if alist[pos] == item: 
            found = True 
        else: 
            pos = pos + 1
    
    return found 

#%%
    
testList = [1,2,32,8,17,19,42,13,0] 

print(sequentialSearch(testList, 3))
print(sequentialSearch(testList, 8))

#%% ordered sequential search 

def orderedSequentialSearch(alist, item): 
    pos = 0 
    found = False
    stop = False 
    
    while pos < len(alist) and not found and not stop: 
        if alist[pos] == item: 
            found = True
        else: 
            if alist[pos] > item: 
                stop = True 
            else: pos = pos + 1
    return found 

#%%
    
testList = [0,1,2,8,13,17,19,32,42]

print(orderedSequentialSearch(testList, 13))

#%% binary search

def binarySearch(alist, item): 
    first = 0
    last = len(alist) - 1
    found = False 
    
    while first <= last and not found: 
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else: 
            if item < alist[midpoint]: 
                last = midpoint - 1
            else: 
                first = midpoint + 1
    return found 

#%% 

print(binarySearch(testList, 8))

#%% Hash Functions

def hash(astring, tablesize): 
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) 
    return sum%tablesize
    
#%% Map abstract data type 

# Map(), put(key, val), get(key), del, len(), in 

class HashTable: 
    def __init__(self): 
        self.size = 11
        self.slots = [None] * self.size 
        self.data = [None] * self.size 
        
    def put(self, key, data): 
        hashvalue = self.hashfunction(key, len(self.slots)) 
        
        if self.slots[hashvalue] == None: 
            self.slots[hashvalue] = key 
            self.data[hashvalue] = data 
        else: 
            if self.slots[hashvalue] == key: 
                self.data[hashvalue] = data 
            else: 
                nextslot = self.rehash(hashvalue, len(self.slots)) 
                while self.slots[nextslot] != None and self.slots[nextslot] != key: 
                    nextslot = self.rehash(nextslot, len(self.slots))  
                if self.slots[nextslot] == None: 
                    self.slots[nextslot] = key
                    self.data[nextslot] = data 
                else: 
                    self.data[nextslot] = data 
    
    def hashfunction(self, key, size): 
        return key % size 
    
    def rehash(self, oldhash, size): 
        return (oldhash + 1) % size 
    
    def get(self, key): 
        startslot = self.hashfunction(key, len(self.slots)) 
        data = None
        stop = False
        found = False 
        position = startslot 
        
        while self.slots[position] != None and not found and not stop: 
            if self.slots[position] == key: 
                found = True
                data = self.data[position] 
            else: 
                position - self.rehash(position, len(self.slots)) 
                if position == startslot: 
                    stop = True 
        return data 
    
    def __getitem__(self, key): 
        return self.get(key) 
    
    def __setitem__(self, key, data): 
        self.put(key, data)
        
#%%
H = HashTable() 

H[54] = "cat" 
H[26] = "dog"
H[93] = "lion" 
H[17] = "tiger" 
H[77] = "bird" 
H[31] = "cow" 
H[44] = "goat" 
H[55] = "pig" 
H[20] = "chicken" 

H.slots 
H.data
                    
#%% Bubble Sort 

def bubbleSort(alist): 
    for passnum in range(len(alist) - 1, 0, -1): 
        for i in range(passnum): 
            if alist[i] > alist[i + 1]: 
                temp = alist[i] 
                alist[i] = alist[i + 1] 
                alist[i + 1] = temp 

#%% 
                
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20] 
bubbleSort(alist) 
print(alist)

#%% short bubble 

def shortBubbleSort(alist): 
    exchanges = True 
    passnum = len(alist) - 1
    
    while passnum > 0 and exchanges: 
        exchanges = False 
        for i in range(passnum): 
            if alist[i] > alist[i + 1]: 
                exchanges = True 
                temp = alist[i] 
                alist[i] = alist[i + 1]
                alist[i + 1] = temp 
            passnum = passnum - 1 
            
alist = [20,30,40,90,50, 60, 70, 80, 100, 110] 
shortBubbleSort(alist) 
print(alist)
