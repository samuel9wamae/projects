#functions are blocks of code excecuted together
#creating a function
#def is used to start a function 
#eg.def print():
def details():
    name=(input("state name"))
    age=(int(input("state age")))
    gender=(input("state gender"))
    print("name:{},/nage:{},/ngender{},".format(name,age,gender))
details()
def add_num(num1,num2):
    sum_num=num1+num2
    print(sum_num)
add_num(4,5)
def mult_num(num1,num2):
    product=num1*num2
    print(product)
a=int(input("state no"))
b=int(input("state no"))
mult_num(a,b)
def divide_num(num1,num2):
    product=num1/num2
    print(product)
divide_num(a,b)



