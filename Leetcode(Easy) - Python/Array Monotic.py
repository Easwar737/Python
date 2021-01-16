"""An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic."""

# I have manually given the input. This one works perfectly for other testcases t

A=[1,2,2,3]
if ((all(A[i]<=A[i+1] for i in range(len(A)-1))) or (all(A[i]>=A[i+1] for i in range(len(A)-1)))):
    return True
else:
    return False