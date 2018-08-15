#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:41:23 2018

@author: michael
"""
import random

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

#%% 

def parChecker(symbolString): 
    s = Stack()
    balanced = True 
    index = 0 
    while index < len(symbolString) and balanced: 
        symbol = symbolString[index] 
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty(): 
                balanced = False 
            else: 
                top = s.pop() 
                if not matches(top, symbol): 
                    balanced = False 
        index = index + 1 
    if balanced and s.isEmpty(): 
        return True
    else: 
        return False 
    
def matches(open, close):
    opens = "([{" 
    closers = ")]}" 
    return opens.index(open) == closers.index(close) 

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

#%% Divide by Two Algorithm 

def divideByTwo(decNumber): 
    remStack = Stack() 
    
    while decNumber > 0: 
        rem = decNumber % 2 
        remStack.push(rem) 
        decNumber = decNumber // 2 
    
    binString = "" 
    
    while not remStack.isEmpty(): 
        binString = binString + str(remStack.pop()) 
    
    return binString 

print(divideByTwo(42))

#%% Generalized, we get a base converter 


def baseConverter(decNumber, base): 
    digits = '0123456789ABCDEF' 
    remStack = Stack() 
    
    while decNumber > 0: 
        rem = decNumber % base 
        remStack.push(rem) 
        decNumber = decNumber // base 
        
    newString = "" 
    while not remStack.isEmpty(): 
        newString = newString + digits[remStack.pop()] 
    
    return newString
    
print(baseConverter(25, 2)) 
print(baseConverter(256, 16))
print(baseConverter(199, 8))

#%% infix to postfix 

# 1. Create an empty stack called opstack for keeping operators. Create an empty list for output 
# 2. Convert the input infix string to a list by using the method split 
# 3. Scan a token list from left to right 
#       - If the token is an operand, append to the end of the output list
#       - If the token is a left parenthesis, push it on the opstack 
#       - If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. append each operator to the end of the output list
#       - If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
# 4. When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list 

def infixToPostfix(infixexpr):
    
    prec = {} 
    prec["*"] = 3 
    prec["/"] = 3 
    prec["+"] = 2
    prec["-"] = 2 
    prec["("] = 1 
    
    opStack = Stack() 
    postfixList = [] 
    tokenList = infixexpr.split() 
    
    for token in tokenList: 
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": 
            postfixList.append(token) 
        elif token == "(": 
            opStack.push(token) 
        elif token == ")": 
            topToken = opStack.pop() 
            while topToken != '(': 
                postfixList.append(topToken) 
                topToken = opStack.pop() 
        else: 
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop()) 
            opStack.push(token) 
            
    while not opStack.isEmpty(): 
        postfixList.append(opStack.pop()) 
    return " ".join(postfixList) 

print(infixToPostfix("A * B + C * D")) 
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))

#%% 

# 1. Create an empty stack called operandStack.
# 2. Convert the string to a list by using the string method split.
# 3. Scan the token list from left to right.
#       - If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
#       - If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operandStack.
# 4. When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.

def postfixEval(postfixExpr): 
    operandStack = Stack() 
    tokenList = postfixExpr.split() 
    
    for token in tokenList: 
        if token in "0123456789": 
            operandStack.push(int(token)) 
        else: 
            operand2 = operandStack.pop() 
            operand1 = operandStack.pop() 
            result = doMath(token, operand1, operand2) 
            operandStack.push(result) 
    return operandStack.pop() 

def doMath(op, op1, op2): 
    if op == "*": 
        return op1 * op2 
    if op == "/": 
        return op1 / op2
    if op == "+": 
        return op1 + op2
    else: 
        return op1 - op2
    
print(postfixEval('7 8 + 3 2 + /'))

#%% Queues 

# isEmpty(), enqueue(), size(), dequeue() 

class Queue: 
    def __init__(self): 
        self.items = [] 
    
    def isEmpty(self): 
        return self.items == [] 
    
    def enqueue(self, item): 
        self.items.insert(0, item) 
    
    def dequeue(self): 
        return self.items.pop() 
    
    def size(self): 
        return len(self.items)
    
#%% 

q = Queue() 
q.enqueue(4)
q.enqueue('Dog')
q.enqueue(True) 
print(q.size())

#%% 
q.isEmpty() 
q.enqueue(8.4) 
#%% 
q.dequeue() 
#%% 
q.size()

#%% Josephus Problem 

def hotPotato(nameList, num): 
    simQueue = Queue() 
    
    for name in nameList: 
        simQueue.enqueue(name) 
        
    while simQueue.size() > 1: 
        for i in range(num): 
            simQueue.enqueue(simQueue.dequeue())
        simQueue.dequeue() 
        
    return simQueue.dequeue() 

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'John', 'Kent', 'Brad'], 7))
 
#%% Simulation: Printing Tasks 

# Main Simulation Steps

# 1.  Create a queue of print tasks. Each task will be given a timstamp upon its arrival. The queue is empty to start 
# 2. For each second(currentSecond): 
#       - Does a new print task get created? If so, add it to queue with currentSecond as timestamp 
#       - If print not busy and task is waiting: 
#           - remove next task from the print queue and assign it to the printer 
#           - subtract the timestamp from the currentSecond to compute the waiting time for that task 
#           - append the waiting time for that task to a list for later processing 
#           - based on the number of pages in the print task, figure out how much time is required 
#       - The printer now does 1 second of printing if necessary. It also subtracts 1 second from time for task 
#       - If task completed, time has reached 0, the printer is no longer busy 
# 3. After sim complete, compute the avg waiting time from the list of waiting times generated 

class Printer: 
    def __init__(self, ppm): 
        self.pagerate = ppm 
        self.currentTask = None 
        self.timeRemaining = 0 
        
    def tick(self): 
        if self.currentTask != None: 
            self.timeRemaining = self.timeRemaining - 1 
            if self.timeRemaining <= 0: 
                self.currentTask = None 
    
    def busy(self): 
        if self.currentTask != None: 
            return True
        else: 
            return False 
    
    def startNext(self, newTask): 
        self.currentTask = newTask 
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate
        
#%% 
class Task: 
    def __init__(self, time): 
        self.timestamp = time 
        self.pages = random.randrange(1, 21) 
    
    def getStamp(self): 
        return self.timestamp 
    
    def getPages(self): 
        return self.pages 
    
    def waitTime(self, currentTime): 
        return currentTime - self.timestamp 
    
#%% 

def simulation(numSeconds, pagesPerMinute): 
    
    labprinter = Printer(pagesPerMinute) 
    printQueue = Queue() 
    waitingTimes = [] 
    
    for currentSecond in range(numSeconds): 
        
        if newPrintTask(): 
            task = Task(currentSecond) 
            printQueue.enqueue(task) 
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()): 
            nexttask = printQueue.dequeue() 
            waitingTimes.append(nexttask.waitTime(currentSecond)) 
            labprinter.startNext(nexttask) 
        labprinter.tick() 
    
    averageWait = sum(waitingTimes) / len(waitingTimes) 
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size())) 
    
def newPrintTask():
    num = random.randrange(1, 181) 
    if num == 180: 
        return True
    else: 
        return False 

for i in range(10): 
    simulation(3600, 10)
    
#%% Dequeues
    
# Deque(), addFront(item), addRear(item), removeFront(), removeRear(), isEmpty(), size() 
    
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    

    
#%% 
d = Deque() 
print(d.isEmpty()) 

d.addRear(4) 
d.addRear('Dog') 
d.addFront('cat') 
d.addFront(True)
print(d.size()) 
print(d.isEmpty())
d.addRear(8.4) 
print(d.removeRear()) 
print(d.removeFront())

#%% Palindrome Checker

def palChecker(aString): 
    charDeque = Deque() 
    
    for ch in aString: 
        charDeque.addRear(ch) 
    
    stillEqual = True 
    
    while charDeque.size() > 1 and stillEqual: 
        first = charDeque.removeFront()
        last = charDeque.removeRear() 
        if first != last: 
            stillEqual = False 
    return stillEqual 

print(palChecker('lsdkjfskf'))
print(palChecker('radar'))
print(palChecker('amanaplanacanalpanama'))

#%% Unordered List Abstract Data Type

# List(), add(item), remove(item), search(item), isEmpty(), size(), append(item), index(item), insert(pos, item), pop(), pop(pos)

class Node: 
    def __init__(self, initdata): 
        self.data = initdata 
        self.next = None 
    
    def getData(self): 
        return self.data
    
    def getNext(self): 
        return self.next
    
    def setData(self, newdata): 
        self.data = newdata
        
    def setNext(self, newnext): 
        self.next = newnext 

#%%

temp = Node(93)
temp.getData()

#%% 

class UnorderedList: 
    def __init__(self): 
        self.head = None 
        
    def isEmpty(self): 
        return self.head == None 
    
    def add(self, item): 
        temp = Node(item)
        temp.setNext(self.head) 
        self.head = temp 
    
    def size(self):
        current = self.head
        count = 0
        while current != None: 
            count = count + 1
            current = current.getNext() 
        return count 
    
    def search(self, item):
        current = self.head 
        found = False
        while current != None and not found: 
            if current.getData() == item: 
                found= True
            else:
                current = current.getNext() 
        return found 
    
    def remove(self, item): 
        current = self.head 
        previous = None 
        found = False 
        
        while not found: 
            if current.getData() == item: 
                found = True 
            else: 
                previous = current 
                current = current.getNext() 
        
        if previous == None: 
            self.head = current.getNext() 
        else: 
            previous.setNext(current.getNext()) 
            
    def append(self, item): 
        current = self.head
        previous = None
        found = False
        
        while not found: 
            if current == None: 
                found = True 
            else: 
                previous = current
                current = current.getNext()
                
        previous.setNext = self.add(item) 
    
    
#%% 
        
myList = UnorderedList()

myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)

myList.append(12)

#%% 
myList.search(12)

#%% Ordered List 

# OrderedList(), add(item), remove(item), search(item), isEmpty(), size(), index(item), pop(), pop(pos)

class OrderedList: 
    def __init__(self): 
        self.head = None 
    
    def search(self, item): 
        current = self.head
        found = False
        stop = False 
        
        while current != None and not found and not stop: 
            if current.getData() == item: 
                found = True
            else: 
                if current.getData() > item: 
                    stop = True 
                else: 
                    current = current.getNext() 
        return found 
    
    def add(self, item):
        
        current = self.head 
        previous = None
        stop = False 
        
        while current != None and not stop: 
            if current.getData() > item: 
                stop = True 
            else: 
                previous = current 
                current = current.getNext() 
        
        temp = Node(item) 
        if previous == None: 
            temp.setNext(self.head) 
            self.head = temp 
        else: 
            temp.setNext(current)
            previous.setNext(temp)
        
