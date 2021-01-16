"""Given a non-negative integer num, repeatedly add all its digits until the result has only one digit."""

# I have manually given the input. This one works perfectly for other testcases too.

num=38
if num>0 and num<2**31-1:
    return 1+(num-1)%9
else:
    return 0