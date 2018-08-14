#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 14:48:22 2018

@author: michael
"""

import time
from timeit import Timer
import random

#%% 
def sumOfN(n): 
    theSum = 0 
    for i in range(1, n+1): 
        theSum = theSum + i 
    return theSum 

sumOfN(10)

#%% 

def sumOfN2(n): 
    start = time.time() 
    theSum = 0 
    
    for i in range(1, n+1): 
        theSum = theSum + i 
    
    end = time.time() 
    return theSum, end - start 

for i in range(5): 
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000000))
    
#%% 
# Done using mathematics

def sumOfN3(n): 
    start = time.time()
    end = time.time()
    return (1/2)*(n*(n+1)), end - start 

print(sumOfN3(10))

#%% benchmark
for i in range(5): 
    print("Sum is %d required %10.7f seconds"%sumOfN3(10000))
    
#%% 
    
# O(n)
def findMin(list):
    currentMin = 100
    for i in range(len(list)): 
        if list[i] < currentMin: 
            currentMin = list[i]
    return currentMin 

listOfNums = [16,32,12,14,96,8,7,12,14]

# print(listOfNums[1])
findMin(listOfNums)

#%% Anagram Solution: Checking Off

def anagramSolution1(s1, s2): 
    alist = list(s2) # convert to list
    pos1 = 0 # position 1 
    stillOK = True # state for anagram 
    
    while pos1 < len(s1) and stillOK: # loop through first word 
        pos2 = 0 
        found = False 
        while pos2 < len(alist) and not found: # look through list of second word to find single letter from word 1 
            if s1[pos1] == alist[pos2]: 
                found = True 
            else: 
                pos2 = pos2 + 1 
        if found: 
            alist[pos2] = None 
        else: 
            stillOK = False 
        pos1 = pos1 + 1
    return stillOK 

print(anagramSolution1('abcd', 'dcba'))

#%% Anagram Solution 2: Sort and Compare 

def anagramSolution2(s1, s2): 
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True 
    
    while pos < len(s1) and matches: 
        if alist1[pos] == alist2[pos]: 
            pos = pos + 1
        else: 
            matches = False 
    return matches
    
anagramSolution2('qbert', 'trasd')

#%% Anagram Solution 4: Count and Compare 

def anagramSolution4(s1, s2): 
    # create empty ticker arrays
    c1 = [0]*26 
    c2 = [0]*26
    
    for i in range(len(s1)): 
        pos = ord(s1[i]) - ord('a') 
        c1[pos] = c1[pos] + 1 
        
    for i in range(len(s2)): 
        pos = ord(s2[i]) - ord('a') 
        c2[pos] = c2[pos] + 1 
    
    j = 0
    stillOK = True 
    while j < 26 and stillOK: 
        if c1[j] == c2[j]: 
            j = j + 1
        else: 
            stillOK = False 
    return stillOK 

print(anagramSolution4('apple', 'pleap'))


#%% 2.6 | Lists 

def test1(): 
    l = [] 
    for i in range(1000): 
        l = l + [i] 

def test2(): 
    l = [] 
    for i in range(1000): 
        l.append(i) 
        
def test3(): 
    l = [i for i in range(1000)] 
    
def test4(): 
    l = list(range(1000)) 
    
#%% 
t1 = Timer("test1()", "from __main__ import test1") 
print("concat ", t1.timeit(number = 1000), "milliseconds") 

t2 = Timer("test2()", "from __main__ import test2") 
print("append ", t2.timeit(number = 1000), "milliseconds") 

t3 = Timer("test3()", "from __main__ import test3") 
print("comprehension ", t3.timeit(number = 1000), "milliseconds") 

t4 = Timer("test4()", "from __main__ import test4") 
print("list range ", t4.timeit(number = 1000), "milliseconds") 

#%% 

popzero = Timer("x.pop(0)", "from __main__ import x") 
popend = Timer("x.pop()", "from __main__ import x") 

x = list(range(2000000)) 
popzero.timeit(number = 1000) 

#%% 
x = list(range(2000000)) 
popend.timeit(number = 1000)

#%% Dictionaries 

for i in range(10000, 1000001, 20000): 
    t = Timer("random.randrange(%d) in x"%i, 
              "from __main__ import random, x") 
    x = list(range(i)) 
    lst_time = t.timeit(number = 1000) 
    x = {j: None for j in range(i)} 
    d_time = t.timeit(number = 1000) 
    print("%d, %10.3f, %10.3f"%(i, lst_time, d_time))

