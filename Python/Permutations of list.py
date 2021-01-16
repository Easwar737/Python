from itertools import permutations as p
n=int(input("Enter the size:"))
num_list=list(map(int,input("Enter values:").split(",")))
perm=list(p(num_list))
print(perm)
