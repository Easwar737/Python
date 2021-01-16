number=int(input("Enter a number:"))
def fact(number):
    if(number==0 or number==1):
        return 1
    else:
        return number*fact(number-1)

result=fact(number)
print(result)
result=str(result)
total=0
if(result.endswith('0')):
    for i in range(1,len(result)):
        if(int(result[-i:])!=0):
                break
        else:
            total+=1
            if(int(result[-i:])!=0):
                break
print(total)

