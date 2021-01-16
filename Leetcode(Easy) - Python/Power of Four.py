"""Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x."""

# I have manually given the input. This one works perfectly for other testcases too.

n=16
if n>0 and n<2**31-1:
    return log(n,4).is_integer()