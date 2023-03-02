rows = int(input("Enter number of rows "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
x=[]
n=int(input("state no"))
for i in range(n): 
    x.append([])
    x[i].append(1)
    for j in range(1,i):
        x[i].append(x[i-1][j-1]+x[i-1][j])
    if(n!=0):
        x[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(x[i][j]),end=" ",sep=" ")
    print()
