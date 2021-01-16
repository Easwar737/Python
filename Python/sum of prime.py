import itertools as it
n=int(input("Enter a number:"))
num_list=[]
total=0
for i in it.count(start=2):
    if(total==n):
        break
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num_list.append(i)
        total+=1 
print(sum(num_list))
