#write a program that solves a quadratic equation
#using for loop draw a diamond,triangle,pascalstriangle

#used for quadratic equations
a=int(input("state no"))
b=int(input("state no"))
c=int(input("state no"))
m=(b**2)-(4*a*c)#can also use math.pow(b,2)
print(m)
y1=(-b+((m)**0.5))/(2*a)#can also use math,sqrt()
y2=(-b-((m)**0.5))/(2*a)
print(y1)
print(y2)
#shapes using for loop 
# triangle 
du=[]

a=int(input("state length"))
for i in range (0,a):
    s=('*')
    du.append(s)
    print(du)
for b in range (0,a):
     du.pop()
     print(du)
#diamond
diamonds=["   *   ","  ***  "," **** ","******"]
for diamond in diamonds:
    print(diamond)
diamonds.pop()
diamonds.reverse()
for diamond in diamonds:
    print(diamond)

