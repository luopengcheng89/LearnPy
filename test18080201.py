#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('###################slice 00###################')
L = ['Mike','rose','jack','lily']
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

print('###################slice 01###################')
d={'mike':1,'jack':2,'rose':3}
for key in d:
	print(key)
for value in d.values():
	print(value)
for key,value in d.items():
  print(value,key)
  
print('###################Iteration 00###################')  
for x, value in enumerate(['a','b','c','d']):
	print(x,value)
	
for y,z in [(1,1,),(1,2),(1,3)]:
	print(y,z)