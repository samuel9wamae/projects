#program to list prime no
#write a program to list odd no
#write one to list odd no
#to write the arithmetic progression
#for odd and even no
for i in range(1,100):
    if(i%2==0):
        print(i,"is even ")
    else:
        print(i,"is odd")
 #to state prime no
    for a in range(1,100):
        for b in range(2,a//2):
         if(a%b==0):
           break
        else:
           print(a)
