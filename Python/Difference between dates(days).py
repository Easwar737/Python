from datetime import date
print("---DATE 1:---")
y1,m1,d1=int(input("Enter year:")),int(input("Enter month:")),int(input("Enter day:"))
date_1=date(y1,m1,d1)
print("---DATE 2:---")
y2,m2,d2=int(input("Enter year:")),int(input("Enter month:")),int(input("Enter day:"))
date_2=date(y2,m2,d2)
result=(date_1-date_2).days
print("---DAY DIFFERENCE:---")
if(result<0):
    print (-result)
else:
    print(result)

