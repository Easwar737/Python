"""Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?"""

# I have manually given the input. This one works perfectly for other testcases too.

n=3
if n==0 or n==1:
    return 0
else:
    zero=0
    powers=5
    while n>=5:
        zero+=(n//5)
        n=n//5
        powers*=5
    return zero