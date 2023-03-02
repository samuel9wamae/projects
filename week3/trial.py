value=[]
n=int(input("state range"))
for i in range(0,n):
    value.append()
    value.append(1)
    for j in range(i,n):
        value[j].append(value[i]+value[j])
