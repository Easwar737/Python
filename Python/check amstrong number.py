num=input("Enter a number:")
sum=0
for i in num:
    sum=sum+(int(i)**len(num))
if(sum==int(num)):
    print("amstrong number")
else:
    print("not an amstrong number")
