list1=[]
n=int(input("Enter range:"))
count=1
i=1
temp=[]
while i<n+1:
    temp.append(i)
    if(count==5):
        list1.append(temp)
        temp=[]
        count=1
        i+=1
    else:
        count+=1
        i+=1
print(list1)