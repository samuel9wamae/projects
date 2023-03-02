#!/usr/bin/env/python3(tells machine that a program is a python script)
#lists
#samuel wamae
#email;drexradiator@gmail.com
#17/02/2023
#file:missed.py
#lists remastered
#camel case
myFavouriteFruits = ["mangos","apples","pineapple","passion","peaches"]
#snake case
my_favourite_fruits = ["mangos","apples","pineapple","passion","peaches"]
for my_favourite_fruit in  my_favourite_fruits :
    print(my_favourite_fruit)
print(len(my_favourite_fruit))#len()is used to dictate the lengh of a string
friends = ["Matthew","Brian","Rooney","Steve","Alexandria"]
print(friends)
friends[4] = "Anita"
print(friends) #Replaces the name on the index indicated
#copy
new_friends = friends.copy()
print(new_friends)
#sort
new_friends.sort()#puts in alphabetical order
print(new_friends)
#pop removes items at the last index
new_friends.pop()
print(new_friends)

#append

new_friends = ["Baraka","Mukiza"]

elem = str(input("Enter name : "))
new_friends.append(elem)#.append adds  something to te end of the list
print(new_friends)