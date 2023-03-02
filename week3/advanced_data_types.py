#advanced data types

#mutable vs immutable
#mutable-are data types that can be edited during the program life cycle
#immutable-cant be edited during the program life cycle

#LIST(mutable)
friends=[]#names can also be put in the brackets
for i in range(0,4):
    d=(input("state your friends"))
    friends.append(d)
#add items= .append() or extend()
students=["sam","ruben","lily"]
friends.extend(students)
friends.append("mark")
#remove pop(),delete()
friends.sort()
friends.reverse()

#TUPLES(immutable)cant be changed
#initiated by normal brackets
stationaries=("pens","pencils","eraser","sharpener")
#you can replace the whole tuple
stationaries=("ruler","book","file")
for stationary in stationaries:
    print(stationary)
#can be used with any data type

#DICTIONARIES(mutable)
#uses key and value pair
student={"name":"sam","age":18,"gender":"male"}
#name(key) ,value(bob)is the format
print(student["name"])
print(student["age"])
print(student["gender"])

random={"colour":"black","hobby":"skating","course":"economis","weight":"60kg","height":"5.5ft"}
print(random["colour"])
print(random["hobby"])
print(random["course"])
print(random["weight"])
print(random["height"])
print(random.values())
print(random.keys())
#SETS(mutable)
#used to store multiple items in one variable
my_pains={"me","myself","and","i"}
for my_pain in my_pains:
    print(my_pain)
print(my_pain)
print(type(my_pains))
print(len(my_pains))




