number=int(input("Enter a number:"))
flag=0
for i in range(2,number):
    if(number%i==0):
        print("not a prime number")
        flag+=1
        break

if(flag==0):
    print("prime number")
