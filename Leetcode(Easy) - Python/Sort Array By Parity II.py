"""Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition."""

# I have manually given the input. This one works perfectly for other testcases too.

A=[4,2,5,7]
e=[]
o=[]
length=len(A)
for i in A:
    if i%2 is 0:
        e.append(i)
    else:
        o.append(i)
A=[]
for j in range(length>>1):
    A.append(e[j])
    A.append(o[j])
return A