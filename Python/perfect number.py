# A perfect number is the one which is equal to the sum of its proper divisors.
number=input("Enter a number:")
total=0
for num in range(1,int(number)):
    if(int(number)%num==0):
        total=total+num

if(total==int(number)):
    print("perfect number")
else:
    print("imperfect")
