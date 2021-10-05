# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:37:51 2021

@author: mikej
"""
import sys

#function to get sum of all digits in a string
def getSum(n):
    
    sum = 0
    for digit in n:
        sum += int(digit)
    return sum

#function for creating sets in two digit intervals
def NumIter(x, y, z):
    
    for i in x:
        if y > len(x):
            break
        else:
            z.append(x[-y])
            y += 2

am = [34, 37]
mc = [51, 52, 53, 54, 55]
v = 4

num = input("Number: ")

#test if number is valid credit card
if len(num) < 13:
    print("INVALID")
    sys.exit()
else:
    pass

#this takes card number and applies Luhn's Algorithm check

nlist = []
nlistTwo = []
nlistThree = []
twoSum = ""

x = 2
y = 1

for i in num:
    nlist.append(int(i))

NumIter(nlist, x, nlistTwo)

NumIter(nlist, y, nlistThree)

for i in range(len(nlistTwo)):
    twoSum += str(nlistTwo[i] * 2)

digitSum = getSum(twoSum)

for j in nlistThree:
    digitSum += j
    
digitSum = str(digitSum)

#test what kind of credit card
check = int(num[:2])

if digitSum[-1] == "0":
    if check in am:
        print("AMEX")
    elif check in mc:
        print("MASTERCARD")
    else:
        print("VISA")
elif digitSum[-1] != "0":
    print("INVALID")
    