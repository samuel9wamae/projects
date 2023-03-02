#when inputing the numbers for the mean
numbers=[]
sum=0
i=int (input("state range"))
for numbers in range(0,i):
  numbers=int(input("input the numbers") )
  sum=sum+numbers
  avg=sum/i
print(avg)