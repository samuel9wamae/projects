#create a function to print factorial of a no
def factorial():
 x=int(input("state initial"))
 n=x
 for a in range(1,x):
    x=x*(n-a)
 print(x)
factorial()
#function for simple interest
def simple_interest():
    p=int(input("state principal"))
    r=int(input("state rate"))
    t=int(input("state time"))
    product=p*r*t
    ans=product/100
    print(ans)
simple_interest() 
#function for quadratic equation
def quad():
    a=int(input("enter value"))
    b=int(input("enter value"))
    c=int(input("enter value"))
    m=(b**2)-(4*a*c)
    print(m)
    y1=(-b+((m)**0.5))/(2*a)
    y2=(-b-((m)**0.5))/(2*a)
    print(y1)
    print(y2)
quad()



