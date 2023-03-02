p=3.142
r=input("state radius")
h=input("state height")
d=int (r)*2
s_s=4*p*(int (r)**2)
v_s= 4/3*p*(int (r)**3)
s_c=(2*float(p)*(int (r)**2))+(p*d*int (h))
v_c=p*(int (r)**2)*int (h)
print("surface area of sphere is",s_s)
print("volume of sphere is",v_s)
print("surface area  of cylinder is",s_c)
print("colume of cylinder is",v_c)