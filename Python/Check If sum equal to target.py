num=input("Enter values for list:").split(",")
k=int(input("Enter Target sum value:"))
flag=0
for i in range(len(num)):
    for j in range(i,len(num)):
        total=int(num[i])+int(num[j])
        if(total==k):
            flag+=1
            print(num[i],num[j])
            break
    if(flag>1):
        break