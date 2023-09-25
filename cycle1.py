#!/usr/bin/env python
# coding: utf-
import numpy as np
#qn 1
x = np.array([1,2,5,6])
y = np.array([7,4,5,3])
print(x)
print(y)
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))

#qn 2
z = np.arange(30,71,2)
print(z)

#qn 3
a = np.identity(3)
print('3x3 matrix')
print(a)
#qn 4

s = np.arange(21)
print("Original Array:\n",s)
print("After changing the sign of numbers in the range from 9 to 15: ")
s[(s>=9) & (s<=15)]*=-1
print(s)

#qn 5
print(np.diag([1,2,3,4,5]))

#qn 6
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Sum of all elements: ",np.sum(a))
print("Sum of each column: ",np.sum(a,axis=0))
print("Sum of each row: ",np.sum(a,axis=1))

#qn 7
np.savetxt('new.txt',a)
t = np.loadtxt('new.txt')
print(t)

#qn 8
a = np.array([7,2,3])
b = np.array([4,5,3])
res = np.array_equal(a,b)
print("Equal" if res==True else "Not Equal")

#qn 9
arr = np.array([[0,0,0,0],[2,2,2,2],[3,3,3,3],[1,1,1,1]])
print("Original array: \n", arr)
arr[[0,3]]=arr[[3,0]]
print("Swapped array: \n", arr)

#qn 10
a = np.array([[1,1,1],[1,2,3]])
print("Array 1: ",a)
b = np.array([[4,3,2],[1,1,1]])
print("Array 1: ",b)
print("Array after multiplying: ")
print(np.multiply(a,b))