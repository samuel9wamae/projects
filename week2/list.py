#how to make lists in python
names=["samuel","peter","john","philip","james"]#[] are used when making lists
#accessing items on a list
print(names[0])#each item has a numeric position starting from 0
print(names[-1])
print(names[2])
print(names[0:3])
fruits=["mangoes","banana","grapes","watermelon","apples","papaya","grapefruit"]
print("mt favourite fruit is",fruits[3].upper())
#adding 2 lists
vegetables=["kales","spinach","terere","carrot","brocoli"]
stationary=["ink","pens","tape","exerciseb book","eraser"]
shoppings=vegetables+stationary
print(shoppings[5])
for vegetable in vegetables:#a for loop can be used to access itrms in the lists
 print(vegetable)
for shopping in shoppings:
    print(shopping)
print("my name is ",names[0]+" "+"my favourite fruit is",fruits[4])