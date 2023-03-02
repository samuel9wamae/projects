#!/usr/bin/env/python3(tells machine that a program is a python script)
#to find prime no
#samuel wamae
#email;drexradiator@gmail.com
#17/02/2023
#file:ap.py
print("***The values below are prime numbers***")
for prime_numbers in range(1, 101):
   if prime_numbers > 1:
       for i in range(2, prime_numbers):
           if (prime_numbers % i) == 0:
                 break
       else:
           print(prime_numbers)