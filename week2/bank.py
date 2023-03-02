#!/usr/bin/env/python3(tells machine that a program is a python script)
#tax retun
#samuel wamae
#email;drexradiator@gmail.com
#17/02/2023
#file:bank.py
#write program that calculates 
#19% tax 150-300k
#30% for above 300k
#5% below 100k
#print gross income and net income
income=int(input("state income"))
if(income>300000):
    net=income-(income*0.3)
elif((income>150000) & (income<300000)):
    net=income-(income*0.19)
elif(income<150000):
    net=income-(income*0.1)
print(income)
print(net)