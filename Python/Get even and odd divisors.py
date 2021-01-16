number=int(input("Enter number:"))
even=[]
odd=[]
for i in range(1,number+1):
    if(number%i==0):
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    else:
        continue            
print("Even divisors:",even)
print("Odd divisors:",odd)