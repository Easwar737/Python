num1,num2=input("Enter num1:"),input("Enter num2:")
i=0
length_num1=len(num1)
length_num2=len(num2)
carry=0
count=0
while(length_num1!=0 and length_num2!=0):
    i+=1
    total=int(num1[-i])+int(num2[-i])+carry
    if(total>10):
        carry+=1
        count+=1
    length_num1-=1
    length_num2-=2
print(count)
