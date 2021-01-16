"""Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x."""

# I have manually given the input. This one works perfectly for other testcases too.

n=1
if n>0 and n<2**31-1:
    val=round(log(n,2))
    return 2**val==n