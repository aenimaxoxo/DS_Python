#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:04:32 2018

@author: michael
"""
import math
import turtle
#%% Ch 4 | Recursion

def listSum(numList): 
    theSum = 0
    for i in numList: 
        theSum = theSum + i
    return theSum 

print(listSum([1,3,5,7,9]))

#%% recursive version of above 

def listSum(numList): 
    if len(numList) == 1: 
        return numList[0] 
    else: 
        return numList[0] + listSum(numList[1:]) 

print(listSum([1, 3, 5, 7, 9]))

#%% 3 Laws of Recursion
# 1. A recursive algorithm must have a base case 
# 2. A recursive algorithm must change its state and move towards the base case 
# 3. A recursive algorithm must call itself, recursively 

#%% Convert Integer to any base using recursion

# 1. Reduce the original number of a series of single digit numbers 
# 2. convert the single digit number to a string using a lookup 
# 3. Concatenate the single digit strings together to form the final result 

def toStr(n, base): 
    convertString = "0123456789ABCDEF" 
    if n < base: 
        return convertString[n] 
    else: 
        return toStr(n // base, base) + convertString[n%base] 
    
print(toStr(1453, 16))

#%% 
# write a function that takes a string as a parameter and returns a new string that is reversed 

def revString(aString): 
    if len(aString) == 1:
        return aString[0]
    else: 
        return revString(aString[1:]) + aString[0]
    
#%% 
revString("You can't do that!")

#%% 

def checkPalindrome(aString): 
    if len(aString) == 0 or len(aString) == 1: 
        return True 
    else: 
        if aString[0] == aString[len(aString)-1]: 
            return checkPalindrome(aString[1:-1])
        else: 
            return False 
        
#%% 
checkPalindrome("")




#%% 

# implement fibonacci sequence using recursion

def fib(n): 
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

#%%

fib(5)                                                                           

#%% prime factorization
# primesList = primes(1000)
def primeFactors(n): 
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    factors = [] 
    
    if n in primes: 
        factors.append(n)
        return factors
    else: 
        for i in primes:
            if n%i == 0: 
                factors.append(i)
                break
        return primeFactors(n // factors[0]), factors

#%% 
primeFactors(81)

#%% prime generator

def primes(n): 
    nroot = int(math.sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    sieve = [x for x in sieve if x !=0]
    
#%% 
def divisiblebyprime(n):
    lisp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    for i in lisp:
        if n % i == 0:
            return divisiblebyprime(n//i), i
#%%
divisiblebyprime(77)

#%% Stack Frames: Implementing Recursion

rStack = Stack() 

def toStr(n, base): 
    convertString = "0123456789ABCDEF" 
    while n > 0: 
        if n < base: 
            rStack.push(convertString[n]) 
        else: 
            rStack.push(convertString[n%base]) 
        n = n // base 
    res = "" 
    while not rStack.isEmpty(): 
        res += str(rStack.pop()) 
    return res 

print(toStr(1453, 16))

#%% Visualizing Recursion

myTurtle = turtle.Turtle() 
myWin = turtle.Screen() 

def drawSpiral(myTurtle, lineLen): 
    if lineLen > 0: 
        myTurtle.forward(lineLen) 
        myTurtle.right(90) 
        drawSpiral(myTurtle, lineLen - 5) 

# drawSpiral(myTurtle, 100) 
# myWin.exitonclick()

#%% 

def tree(branchLen, t): 
    if branchLen > 5: 
        t.forward(branchLen) 
        t.right(20) 
        tree(branchLen - 15, t) 
        t.left(40) 
        tree(branchLen - 15, t) 
        t.right(20) 
        t.backward(branchLen) 
        
def main(): 
    t = turtle.Turtle() 
    myWin = turtle.Screen() 
    t.left(90) 
    t.up()
    t.backward(100) 
    t.down() 
    t.color("green") 
    tree(75, t) 
    myWin.exitonclick() 
    
main() 

#%% Towers of Hanoi 

def moveTower(height, fromPole, toPole, withPole): 
    if height >= 1: 
        moveTower(height - 1, fromPole, withPole, toPole) 
        moveDisk(fromPole, toPole) 
        moveTower(height - 1, withPole, toPole, fromPole) 

def moveDisk(fp, tp): 
    print("moving disk from", fp, "to", tp)
 
moveTower(3, 'A', 'B', 'C') 

#%% 
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

#%% Dynamic Programming 

def recMC(coinValueList, change): 
    minCoins = change 
    if change in coinValueList: 
        return 1
    else: 
        for i in [c for c in coinValueList if c <= change]: 
            numCoins = 1 + recMC(coinValueList, change - i) 
            if numCoins < minCoins: 
                minCoins = numCoins 
    return minCoins 

print(recMC([1, 5, 10, 25], 63))

#%% Memoization 

def recDC(coinValueList, change, knownResults):
    minCoins = change 
    
    if change in coinValueList: 
        knownResults[change] = 1
        return 1 
    elif knownResults[change] > 0: 
        return knownResults[change]
    else: 
        for i in [c for c in coinValueList if c <= change]: 
            numCoins = 1 + recDC(coinValueList, change - i, knownResults) 
            if numCoins < minCoins: 
                minCoins = numCoins 
                knownResults[change] = minCoins 
    return minCoins 

print(recDC([1,5,10,25], 63, [0]*64))

#%% proper DP 

def dpMakeChange(coinValueList, change, minCoins, coinsUsed): 
    for cents in range(change + 1): 
        coinCount = cents 
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]: 
            if minCoins[cents - j] + 1 < coinCount: 
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount 
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change): 
    coin = change
    while coin > 0: 
        thisCoin = coinsUsed[coin] 
        print(thisCoin) 
        coin = coin - thisCoin 
        
def main():
    amnt = 63
    clist = [1,5,10,21,25] 
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1) 
    
    print("Making change for", amnt, "requires") 
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins") 
    print("They are: ")
    printCoins(coinsUsed, amnt) 
    print("The used list is as follows: ") 
    print(coinsUsed)
    
main() 
