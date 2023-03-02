#if condition
age=int(input("enter age"))
gender=input("enter gender")
if (age > 18):
    print("under age")
else:
    print("an ID should be acquired immediately")
#compound  condition
if((age>16) & (gender=="male")&(age<45)):
    print("you are to be conscripted to military")
else:
    print("you are to report to factory for work")
income=int(input("state incomee"))
if((gender=="female") | (income>=30000)):
 print("when should we meet up")
else:
  print("oure not my type")
