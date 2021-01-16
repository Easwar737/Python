"""In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times."""

# I have manually given the input. This one works perfectly for other testcases too

A=[1,2,3,3]
for i in A:
    if A.count(i)==len(A)>>1:
        return i