"""Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x."""

# I have manually given the input. This one works perfectly for other testcases too.

n=27
if n>0 and n<2**31-1:
    val=round(log(n,3))
return 3**val==n