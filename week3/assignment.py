#!/usr/bin/env/python3(tells machine that a program is a python script)
#practice on lists
#samuel wamae
#email;drexradiator@gmail.com
#17/02/2023
#file;assignment.py
#assignment
musicians=[]
a=int(input("stare no of musicians"))
for b in range(0,a):
    c=(input("state musicians"))
    musicians.append(c)
print(musicians)
musicians.sort()
print(musicians)
celebs=musicians.copy()
d=int(input("state no of  additional names"))
for e in range(0,d):
 celebs.append(input("state more names"))
print(celebs)
celebs.pop(2)
print(celebs)
print(len(celebs))
