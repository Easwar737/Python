"""Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition."""

# I have manually given the input. This one works perfectly for other testcases too.

e=[]
o=[]
for i in A:
    if i%2 is 0:
        e.append(i)
    else:
        o.append(i)
A=[]
A+=e
A+=o
return A