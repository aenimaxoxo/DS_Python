#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 18:04:16 2018

@author: michael
"""
import math 
import random
from string import ascii_lowercase

#%% Built-in Atomic Data Types 

print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7%3)
print(3/6)
print(3//6) # integer division 
print(3%6)
print(2**100)

print(5 == 10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

#%% 
theSum = 0
theSum

#%% 
theSum = theSum + 1 
theSum 

#%% 
theSum= True 
theSum

#%% Built-in Collection Data Types 

myList = [1, 3, True, 6.5] 
myList

myList = [0] * 6 
myList

#%% 
myList = [1, 2, 3, 4] 
A = [myList]*3 
print(A) 
myList[2] = 45 
print(A)

#%% List Operations 

myList = [1024, 3, True, 6.5] 
myList.append(False) 
print(myList)

#%% 
myList.insert(2, 4.5) 
print(myList) 
print(myList.pop()) 
print(myList) 
print(myList.pop(1))

#%% 
myList.pop(2) 
print(myList) 
myList.sort()
print(myList) 
print(myList.count(6.5)) 
print(myList.index(4.5)) 
myList.remove(6.5) 
print(myList) 
del myList[0] 
print(myList)

#
# Method Name	Use	Explanation
# append	alist.append(item)	Adds a new item to the end of a list
# insert	alist.insert(i,item)	Inserts an item at the ith position in a list
# pop	alist.pop()	Removes and returns the last item in a list
# pop	alist.pop(i)	Removes and returns the ith item in a list
# sort	alist.sort()	Modifies a list to be sorted
# reverse	alist.reverse()	Modifies a list to be in reverse order
# del	del alist[i]	Deletes the item in the ith position
# index	alist.index(item)	Returns the index of the first occurrence of item
# count	alist.count(item)	Returns the number of occurrences of item
# remove	alist.remove(item)	Removes the first occurrence of item


#%% 
(54).__add__(21)

#%% 
range(10)
list(range(10)) 
range(5, 10)
list(range(5, 10))
list(range(5, 10, 2))
list(range(10, 1, -1))

#%% 
"David"
myName = "Michael"
myName[3]
myName*2
len(myName)

#%% 
myName.upper()
myName.center(10) 
myName.find('a')
myName.split('e')

# center astring.center(w)  returns a string centered in a field of size w 
# count  astring.count(item)  returns the number of occurences of item in the string 
# ljust  astring.ljust(w)  returns a string left justified in a field of size w 
# lower  astring.lower()  returns a string in all lower case 
# rjust  astring.rjust(w)  returns a string right justified in a field of size w 
# find  astring.find(item)  returns the undex of the first occurrence of item 
# split  astring.split(schar)  splits a string into substrings at schar 

#%% 
# a major difference between lists and strings is that strings are immutable 

myList = [1, 3, True, 6.5]

myList[0] = 2**10 

myList

myName 
myName[0]

#%% Tuples 
# tuples are immutable, like strings 

myTuple = (2, True, 4.96) 
myTuple

len(myTuple) 
myTuple * 3 
myTuple[0:2] 

#%% Sets 

mySet = {3, 6, "cat", 4.5, False}

mySet

# membership  in  set membership
# length  len  returns the cardinality of a set
# |  aset \ otherset  returns a new set with all elements from both sets 
# &  aset & otherset  returns a new set with only those elements from both sets 
# -  aset - otherset  returns a new set with all items from the first set not in second 
# <=  aset <= otherset  asks whether all elements of the first set are in the second 
# union  aset.union(otherset)  returns a new set with all elements from both sets 
# intersection  aset.intersection(otherset)  returns a new set with only those elements common to both sets 
# difference  aset.difference(otherset)  returns a new set with all items from the first set not in the second set 
# issubset  aset.issubset(otherset)  asks whether all elements of one set are in the other 
# add  aset.add(item)  adds items to the set 
# remove  aset.remove(item)  removes items from the set 
# pop  aset.pop() removes an arbitrary element from the set 
# clear  aset.clear()  removes all elements from the set 


len(mySet) 
False in mySet 
"dog" in mySet 
 
yourSet = {99, 3, 100} 
mySet.union(yourSet) 

mySet | yourSet 
mySet.intersection(yourSet) 
mySet & yourSet 
mySet.difference(yourSet) 
mySet - yourSet 
{3, 100}.issubset(yourSet) 
{3, 100} <= yourSet  
mySet.add("house") 
mySet 

mySet.remove(4.5) 
mySet 

mySet.pop() 
mySet 

mySet.clear() 
mySet 

#%% Dictionaries 
# Dictionaries are collections of associated pairs of items where each pair consists of a key and value 

capitals = {'Iowa':'DesMoines', 
            'Wisconsin':'Madison'}
capitals

#%% 
print(capitals['Iowa'])
capitals['Utah'] = 'SaltLakeCity' 
capitals['California'] = 'Sacramento' 

for k in capitals: 
    print(capitals[k], "is the capital of ", k) 
    
#%% 
# []  myDict[]  returns the value associated with k, otherwise its an error 
# in  key in adict  returns true if the key is in the dictionary, false otherwise 
# del del adict[key]  removes the entry from the dictionary 
# keys  adict.keys()  returns the keys of the dictionary in a dict_keys object 
# values  adict.values()  returns the values of the dictionary in a dict_values object 
# items   adict.items()  returns the key-value pairs in a dict_items object 
# get  adict.get(k)  returns the value associated with k, None otherwise 
# get  adict.get(k, alt)  returns the value associated with k, alt otherwise 
    
#%% 
phoneExt = {'Michael': 115, 'brad': 1137} 
phoneExt.keys()
phoneExt.values()
phoneExt.items()
phoneExt.get("Kent", "NO ENTRY")

#%% 1.9 | Input and Output 

aName = input('Please enter your name: ') 
print("Your name in all caps is", aName.upper(), "and has length", len(aName))

#%% input in a type besides string 
sradius = input("Please enter the radius of the circle ") 
radius = float(sradius) 
diameter = 2 * sradius  

#%% 1.9.1 | String Formatting 

print("Hello") 
print("Hello", "World") 
print("Hello", "World", sep = "***") 
print("Hello", "World\n", end = "***") 
age = 26
print(aName, "is", age, "years old. ")

#%% 

price = 24 
item = "banana" 
print("The %s costs %d centers"%(item, price)) 

print("The %+10s costs %5.2f cents"%(item, price)) 

itemDict = {"item":"banana", "cost":24} 
print("The %(item)s costs %(cost)7.1f cents"%itemDict) 

#%% 1.10 | Control Structures 

counter = 1
while counter <= 5: 
    print("Hola, Gaia")
    counter = counter + 1 

#%% 
for item in [1, 3, 6, 2, 5]: 
    print(item)
    print(item**2)

#%% 
wordlist = ['cat', 'dog', 'rabbit'] 
letterlist = [] 
for aword in wordlist: 
    for aletter in aword: 
        if aletter in letterlist: 
            continue 
        else: 
            letterlist.append(aletter) 
print(letterlist)

#%% list comprehensions

sqlist = [] 
for x in range(1, 11): 
    sqlist.append(x*x)

#%% 
sqlist = [x*x for x in range(1, 11)]
sqlist

#%% 
[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']

#%% 1.11 | Exception Handling 

anumber = int(input("Please enter an integer ")) 
try: 
    print(math.sqrt(anumber))
except: 
    print("Bad value for square root") 
    print("Using absolute value instead") 
    print(math.sqrt(abs(anumber)))

#%% 
anumber = int(input("Please enter an integer ")) 

if anumber < 0: 
    raise RuntimeError("You can't use a negative number") 
else: 
    print(math.sqrt(anumber)) 
    
#%% 1.12 | Defining Functions 
    
def square(x): 
    return x**2 

square(2)
square(square(2)) 
 
#%% 

def squareRoot(n): 
    root = n / 2
    for k in range(20): 
        root = (1/2) * (root + (n / root)) 
    return root 

squareRoot(4563)

#%% Infinite Monkey Theorem 

def genLetters(wordLength): 
    word = "" 
    letters = ascii_lowercase
    for i in range(wordLength):
        choice = math.floor(random.uniform(0, wordLength))
        word = word + letters[choice]
    return word

def scoreFunction(word): 
    objective = 'methinksitislikeaweasel'
    score = 0
    for letter in range(len(objective)):
        if (word[letter] == objective[letter]): 
            score = score + 1
    return score
    

def genAndScore(letterFun, scoreFun): 
    count = 0 
    topScore = 0 
    topWord = ''
    while topScore < 10: 
        word = genLetters(23) 
        score = scoreFunction(word)
        if score > topScore: 
            topScore = score
            topWord = word
        if count % 1000 == 0: 
            print("The top score so far is %d and the word is %s. Current count: %d"%(topScore, topWord, count))
        count = count + 1
        
genAndScore(genLetters, scoreFunction)
# scoreFunction(genLetters(5))
# genLetters(5)

#%% Object Oriented Programming 

def gcd(m, n): 
    while m%n != 0: 
        oldm = m
        oldn = n 
        m = oldn 
        n = oldm%oldn 
    return n 

class Fraction: 

    def __init__(self, top, bottom): 
        self.num = top 
        self.den = bottom 
    
    def show(self): 
        print(self.num, "/", self.den)
        
    # controls string output 
    def __str__(self): 
        return str(self.num) + "/" + str(self.den) 
    
    # makes sure fraction is in lowest terms, allows for fraction addition
    def __add__(self, other): 
        newnum = self.num * other.den + self.den * other.num 
        newden = self.den * other.den 
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common) 
    
    # compares two objects and returns true if their values are the same, false ow 
    def __eq__(self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum == secondnum 
    
    def __mul__(self, other): 
        newnum = self.num * other.num 
        newden = self.den * other.den 
        common = gcd(newnum, newden) 
        return Fraction(newnum//common, newden//common)
    
    def __truediv__(self, other): 
        newnum = self.num * other.den 
        newden = self.den * other.num 
        common = gcd(newnum, newden) 
        return Fraction(newnum//common, newden//common)

    def __sub__(self, other): 
        tempSelfDen = self.den 
        newselfnum = self.num * other.den 
        newselfden = self.den * other.den 
        newothernum = tempSelfDen * other.num
        newnum = newselfnum - newothernum 
        newden = newselfden 
        common = gcd(newnum, newden) 
        return Fraction(newnum//common, newden//common)
        

#%% 
myFraction = Fraction(3, 5) 
myFraction.show()
print(myFraction)
f1 = Fraction(1, 32)
f2 = Fraction(1, 8) 
f3 = f2 - f1
print(f3)

#%% 
print(gcd(200, 5))
x_var = Fraction(1, 2)
y_var = Fraction(2, 3) 
print(x_var + y_var)
print(x_var == y_var)

#%% Inheritance: Logic Gates and Circuits 

class LogicGate: 
    
    def __init__(self, n):
        self.label = n 
        self.output = None 
    
    def getLabel(self): 
        return self.label 
    
    def getOutput(self): 
        self.output = self.performGateLogic() 
        return self.output 
    
class BinaryGate(LogicGate): 
    
    def __init__(self, n): 
        LogicGate.__init__(self, n) 
        self.pinA = None 
        self.pinB = None 
        
    def getPinA(self):
        if self.pinA == None: 
            return int(input("Enter Pin A input for gate " + self.getLabel() + "--> ")) 
        else: 
            return self.pinA.getFrom().getOutput() 
        
    def getPinB(self): 
        return int(input("Enter Pin B input for gate " + self.getLabel() + "--> ")) 
    
    def setNextPin(self, source): 
        if self.pinA == None: 
            self.pinA = source 
        else: 
            if self.pinB == None: 
                self.pinB = source 
            else: 
                raise RuntimeError("Error: NO EMPTY PINS") 
    
class UnaryGate(LogicGate): 
    
    def __init__(self, n): 
        LogicGate.__init__(self, n) 
        self.pin = None 
        
    def getPin(self): 
        return int(input("Enter Pin input for gate " + self.getLabel() + "--> "))
    
    def setNextPin(self, source): 
        if self.pin == None: 
            return int(input("Enter pin input for gate " + self.getLabel() + " --> "))
        else: 
            return self.pin.getFrom().getOutput() 

class AndGate(BinaryGate): 
    
    def __init__(self, n): 
        BinaryGate.__init__(self, n) 
        
    def performGateLogic(self): 
        a = self.getPinA()
        b = self.getPinB() 
        if a == 1 and b == 1: 
            return 1 
        else: 
            return 0 
        
class OrGate(BinaryGate): 
    
    def __init__(self, n):
        BinaryGate.__init__(self, n) 
        
    def performGateLogic(self): 
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 or b == 1: 
            return 1
        else: 
            return 0 

class NotGate(UnaryGate): 
    
    def __init__(self, n): 
        UnaryGate.__init__(self, n) 
    
    def performGateLogic(self): 
        a = self.getPin() 
        if a: 
            return 0
        else: 
            return 1

class Connector: 
    
    def __init__(self, fgate, tgate): 
        self.fromgate = fgate 
        self.togate = tgate 
        
        tgate.setNextPin(self)
        
    def getFrom(self): 
        return self.fromgate
    
    def getTo(self): 
        return self.togate


#%% 

# g1 = AndGate("G1")
# g1.getOutput()

# g2 = OrGate("G2")
# g2.getOutput()

# g3 = NotGate("G3") 
# g3.getOutput() 
        
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3") 
g4 = NotGate("G4")
c1 = Connector(g1, g3) 
c2 = Connector(g2, g3) 
c3 = Connector(g3, g4) 
g4.getOutput()