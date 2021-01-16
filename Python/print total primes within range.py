n=int(input("Enter range:"))
total=0
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
       total+=1 
print(total)