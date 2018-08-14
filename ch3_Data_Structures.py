#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:41:23 2018

@author: michael
"""

from pythonds.basic.stack import Stack

#%% 3.5 | Implementing a Stack in Python 

class Stack: 
    def __init__(self): 
        self.items = [] 
    
    def isEmpty(self): 
        return self.items == [] 
    
    def push(self, item): 
        self.items.append(item) 
    
    def pop(self):
        return self.items.pop() 
    
    def peek(self): 
        return self.items[len(self.items) - 1] 
    
    def size(self): 
        return len(self.items) 
    
#%% 

s = Stack() 

print(s.isEmpty())

s.push(4) 
s.push('dog') 
print(s.peek()) 
s.push(True) 
print(s.size()) 
print(s.isEmpty()) 
s.push(8.4) 
print(s.pop()) 
print(s.pop()) 
print(s.size())

#%% revstring

def revString(string):
    reversedString = ""
    oldString = Stack()
    
    for i in range(len(string)): 
        oldString.push(string[i])

    for i in range(len(string)): 
        reversedString = reversedString + oldString.pop() 
    
    return reversedString 
    

#%% 
strang = "bilbobaggins"

print(revString(strang))

#%% Simple Balanced Parentheses 

def parChecker(symbolString): 
    s = Stack() 
    balanced = True 
    index = 0 
    
    while index < len(symbolString) and balanced: 
        symbol = symbolString[index] 
        if symbol == "(": 
            s.push(symbol) 
        else: 
            if s.isEmpty(): 
                balanced = False 
            else: 
                s.pop() 
        index = index + 1
        
    if balanced and s.isEmpty(): 
        return True
    else: 
        return False 
    
#%%
print(parChecker('((()))')) 
print(parChecker('(()'))

