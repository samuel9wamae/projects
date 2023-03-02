score=[]
a=int(input("state no of students"))
for b in range(0,a):
    total =int(input("state marks of students"))
    score.append(total)
for c in range(0,a):
    values=int(score[a])
    sum=0
    sum=sum+values
avg=sum//a
print(avg)
